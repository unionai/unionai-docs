---
title: Self-play league for Connect Four
icon: grid-3x3
description: Train a Connect Four agent by self-play against a league of its past selves, rate every snapshot with Elo, and serve the champion as an app you can play against.
weight: 4
variants: -flyte +union
mermaid: true
---

# Self-play league for Connect Four

> [!NOTE]
> Code available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/self_play_league).

In a two-player game there is no fixed environment to beat: the opponent is the environment,
and the best opponent for a learner is usually another copy of itself. Self-play
trained AlphaGo Zero, OpenAI Five, and AlphaStar. It comes with a well-known failure: a learner
that only plays its current self can go in circles, learning to beat today's habits while
forgetting how to beat yesterday's. AlphaStar's answer was a *league*: keep every past snapshot
as an opponent, train against the ones the learner finds hardest, and rate everyone against
everyone so progress is measured instead of assumed.

This tutorial builds a small league for Connect Four. The game and the training both run as
batched tensors, so a generation plays tens of thousands of games on one GPU in a few seconds
per iteration. Union.ai runs everything around it:

- a warm GPU learner that keeps its CUDA context between generations;
- a fan-out of head-to-head matches on a pool of CPU workers after every generation;
- a joint Elo fit over every result, and a live report with the ladder and the score matrix;
- the champion, published as an artifact and served as a FastAPI app you can play in the browser.

## How a generation works

```mermaid
flowchart LR
    D["league<br/>CPU driver"] --> P["pick_opponents<br/>bots + strongest snapshots"]
    P --> T["train_generation<br/>warm GPU, PPO self-play"]
    T -- "snapshot (File)" --> M1["play_match<br/>vs random"]
    T --> M2["play_match<br/>vs tactical"]
    T --> M3["play_match<br/>vs gen-1 ... gen-n"]
    M1 & M2 & M3 --> E["fit Elo<br/>update report"]
    E --> D

    classDef gpu fill:#3b82f633,stroke:#3b82f6,stroke-width:1.5px
    classDef cpu fill:#94a3b826,stroke:#94a3b8,stroke-width:1px
    class T gpu
    class D,P,M1,M2,M3,E cpu
```

1. The driver picks the learner's opponents for this generation: two scripted bots, and the
   three highest-rated snapshots so far.
2. `train_generation` plays 2,048 games per iteration against those opponents and itself, and
   runs a PPO update on the learner's moves. After 25 iterations it saves a snapshot.
3. The new snapshot plays every member of the league, 400 games per pairing, all at once on
   the CPU pool.
4. The driver refits Elo over every match so far and redraws the report.

| Need | Construct |
| --- | --- |
| Keep the GPU learner warm between generations | `flyte.ReusePolicy(replicas=1)` on the training environment |
| Rate a snapshot against the whole league at once | `asyncio.gather` over `play_match` calls on a reusable CPU pool |
| Don't redo work after a driver crash | A `flyte.Cache` on training and matches, salted with the helper modules, and `retries=2` on the driver |
| One view per generation | `flyte.group` |
| Watch the ladder while it trains | `report=True` on the driver and on every training generation |
| Keep and serve the champion | `flyte.artifacts`, and a `FastAPIAppEnvironment` that loads the latest league output |

## Getting started

You need a Union.ai cluster with an NVIDIA L4, or any CUDA GPU (change `train_env` in
`league.py`), and a Flyte config that points at it (see the
[quickstart](../../../user-guide/get-started/quickstart)). Each script declares its
dependencies in an inline header, so `uv run` installs them.

```bash
git clone https://github.com/unionai/unionai-examples
cd unionai-examples/v2/tutorials/self_play_league
uv run league.py            # 20 generations
uv run league.py --smoke    # 2 short generations
uv run app.py               # serve the champion of the latest successful league run
```

## The game as tensors

Every board is stored from the point of view of the player to move, so one network plays both
sides. A move places a stone, checks for four in a row with a 2D convolution, and flips the
board for the other player. Thousands of games step together on the GPU.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/connect4.py" fragment=env lang=python >}}

The league starts with two scripted opponents. The tactical bot wins when it can, blocks when it
must, and otherwise prefers the center. It beats a random player almost every time, and it is
the bar the learner has to clear.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/connect4.py" fragment=bots lang=python >}}

The network is a small residual convolutional network with a policy head and a value head.
Illegal moves are masked out of the policy.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/connect4.py" fragment=net lang=python >}}

## Self-play training

A training iteration plays one batch of games against the opponents, splitting the games evenly
between them. Within each opponent's games the learner moves first in every other game, so it
moves first in half the games against every opponent. Only the learner's moves are kept, and
each one gets the final outcome of its game as its return.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/selfplay.py" fragment=collect lang=python >}}

The update is PPO with the value head as the baseline. Because the return is the game's
outcome, the advantage of a move is how much better the game went than the value head expected
from that position.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/selfplay.py" fragment=update lang=python >}}

`train_generation` wraps this in a task. It loads the learner and its Adam optimizer state from
the previous generation's checkpoint, trains, and returns the new checkpoint as a `flyte.io.File`.
Its live report shows the score against each opponent as the iterations go by.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/league.py" fragment=train lang=python >}}

## The league

The environments make the split between the two kinds of work explicit. Training is one warm
GPU replica that every generation of a run reuses. Matches are a pool of CPU replicas that grows
while a new snapshot plays the league, and shrinks after. Both cache their results, so a driver
that is retried after a crash replays finished generations from the cache instead of training
them again.

`cache="auto"` hashes only a task's own body, not the modules it imports. The training and match
tasks call into `connect4.py` and `selfplay.py`, so the cache is salted with a hash of those two
files: editing the game or the trainer invalidates the cached generations and matches instead of
replaying stale ones.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/league.py" fragment=envs lang=python >}}

A match is a batch of games between two players. The first move alternates and the first four
moves are random, so that two deterministic players don't replay the same game 400 times.
Snapshots play greedily after the opening. The bots play as they always do: the tactical bot
samples its center-weighted moves.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/selfplay.py" fragment=match lang=python >}}

### Elo

Each match gives a score from one side's point of view. The ratings are fitted jointly over all
of them, Bradley-Terry style, with the random bot pinned at 0. A difference of 400 points means
the stronger player is expected to score 10 to 1.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/elo.py" fragment=fit lang=python >}}

### Choosing opponents

The learner's opponents are itself, the two bots, and the three highest-rated snapshots, with
the games split evenly six ways (fewer ways in the first generations, before there are three
snapshots). The strongest snapshots are the opponents it has the most to learn from, and they
stay in the mix even after newer snapshots arrive. Training against the most recent snapshots
instead lets the learner forget how to beat older styles of play.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/league.py" fragment=opponents lang=python >}}

### The driver

{{< code file="/unionai-examples/v2/tutorials/self_play_league/league.py" fragment=driver lang=python >}}

## Results

A run with the defaults, 20 generations of 25 iterations of 2,048 games, took 39 minutes end to
end: 19 minutes of training on one L4, and 231 matches (92,400 rated games) on the CPU pool. The
final Elo fit rates every snapshot against every other:

| | Elo | Score against the tactical bot |
| --- | --- | --- |
| Random bot | 0 (pinned) | |
| Tactical bot | 473 | |
| Generation 1 | 176 | 16% wins |
| Generation 10 | 487 | |
| Champion (generation 20) | 623 | 73% wins, 2% draws, greedy play |

The learner passes the tactical bot by generation 10, and the ratings keep rising, more slowly,
to generation 20. The top three snapshots are generations 20, 19 and 17, at 623, 594 and 593. In
training, where both sides sample their moves, the learner's score against the tactical bot
climbs from 2% in the first iteration to 91% in the last, and its score against itself stays at
50%, as it should when it moves first in half the games.

Elo summarizes every result at once, so a single pairing can differ from what the rating gap
predicts. The champion's 150-point lead over the tactical bot predicts a 70% score; head to head
it scores 74%, counting draws as half.

The report's "Elo of the newest snapshot" chart is a different number: each point is the newest
snapshot's rating in the fit made when it joined, against a league that was weaker then. It
jumps in the first generations and then levels off, because each new snapshot is rated against
stronger opponents.

The driver's report shows the ladder, a sample game against the tactical bot, and the training
curves:

![The league report: champion Elo, score against the tactical bot, the Elo ladder, a sample game, and training curves](../../../_static/images/tutorials/self-play-league/league-report.png)

The score matrix shows every pairing. Each row is a player's score against each column: later
generations (lower rows) score higher against earlier ones (left columns), and the bots' rows
darken as the league grows.

![The score matrix of the 20-generation league](../../../_static/images/tutorials/self-play-league/score-matrix.png)

Because training and matches are cached, running the same league again replays every
generation from the cache. The rerun took 25 seconds instead of 39 minutes, and only the driver
did any work. A driver that crashes partway through resumes the same way.

![A rerun of the league in the UI: every action is a cache hit, and the run takes 25 seconds](../../../_static/images/tutorials/self-play-league/cached-rerun.png)

## Play the champion

`app.py` serves the champion as a FastAPI app. The champion's checkpoint is an app parameter
whose value is a `RunOutput`: when the app is deployed, Flyte resolves it to the output of the
latest successful `league` run, so a new league run followed by a redeploy serves the new
champion with no code change. That includes `--smoke` runs: if a smoke run is the latest, the
app serves its two-generation champion. The app scales to zero when nobody is playing, and
only users signed in to your Union.ai tenant can open it. To let anyone with the URL play, add
`requires_auth=False` to the app environment.

{{< code file="/unionai-examples/v2/tutorials/self_play_league/app.py" fragment=app lang=python >}}

The page sends the board after each of your moves, and the app answers with the champion's
move, its move probabilities, and its value estimate for the position:

{{< code file="/unionai-examples/v2/tutorials/self_play_league/app.py" fragment=move lang=python >}}

Here the champion has just blocked both ends of a three-in-a-row:

![Playing the champion in the browser](../../../_static/images/tutorials/self-play-league/arena-app.png)

## Going further

- **Add search.** Use the policy as the prior and the value head as the evaluator for a few
  plies of lookahead, as in AlphaZero's Monte Carlo tree search.
- **A bigger league.** Add main exploiters, learners whose only job is to beat the current
  champion, as AlphaStar did. Each one is another `train_generation` call in the same loop.
- **Other games.** Any game that can be written as batched tensor steps, from Othello to
  simple card games, can replace `connect4.py`. The league, matches, and Elo fit don't depend on
  the game. The network's input shape and the app's 6×7 board do, so change those too.

## Related

- [Reinforcement learning](../../../user-guide/reinforcement-learning/_index) in the user guide
- [Reusable containers](../../../user-guide/tasks/task-configuration/reusable-containers)
- [Caching](../../../user-guide/tasks/task-configuration/caching)
- [FastAPI apps](../../../user-guide/apps/native-app-integrations/fastapi-app)
- [Passing parameters to apps](../../../user-guide/apps/configure-apps/passing-parameters)
