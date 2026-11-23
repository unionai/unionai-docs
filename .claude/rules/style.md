---
paths:
  - "content/**/*.md"
  - "content/**/*.ipynb"
---

# Voice and style

The docs are for developers who came to get something done. Write for that reader: say what
to do and what will happen, then get out of the way.

Mechanics (shortcodes, notices, autolinking, frontmatter) are in `authoring.md`. Generated pages
under `content/api-reference/` take their prose from docstrings upstream and are exempt.

The contributor-facing version of this guide is
`content/community/contributing-docs/writing-guidelines.md`. Change both together.

## Content

- **Lead with the task.** Open with one or two sentences on what the feature does and when to use
  it, then the smallest working example. Concepts and background come after, and only as much as
  the reader needs to use the feature correctly.
- **Describe the current product.** No history ("previously", "we changed", "the bug that
  shipped"), no roadmap ("coming soon", "will support"), no time-relative words ("new",
  "currently", "now"). When behavior depends on a version, state the requirement: "Requires
  `flyte` 2.10 or later."
- **Explain only what the reader can act on.** A clause of *why* is useful when it helps the
  reader choose or avoid a mistake. Design rationale, trade-offs the reader can't change, and
  arguments for the API's shape belong in the PR or a design doc.
- **Don't editorialize.** No commentary on how surprising, common, interesting, or painful
  something is, and no predictions about how the reader will feel. State the fact.
- **State gotchas plainly.** Non-obvious behavior is the most valuable thing a page carries. Name
  the symptom and the cause together: "If the handler never fires, check that `scopes` includes
  the event's repository."
- **Say it once.** Put a shared fact on one page, usually the section landing page, and link to
  it. Don't copy setup steps or explanations across sibling pages.
- **Be accurate.** Verify behavior against the SDK source or by running the code. Don't
  document from memory or from Flyte 1.x material.

## Page structure

A typical feature page follows this order. Omit sections that don't apply.

1. What it is and when to use it (one or two sentences)
2. Installation or prerequisites
3. Minimal working example
4. Configuration and options
5. Common patterns
6. Gotchas and limitations
7. Related pages

- **Headings** are sentence case and name the content: `## Configure retries`, not
  `## Retries: what you need to know`. Use imperative verbs for task sections ("Deploy the app")
  and nouns for reference sections ("Event fields").
- **One topic per page.** If a page covers two features a reader would look for separately,
  split it.
- **Prefer lists and tables** for steps, options, and comparisons. Use prose to explain how
  things relate.

## Voice

- **Second person, present tense, active voice.** "You define the environment once." "The app
  verifies each delivery." Not "the delivery is verified" or "the app will verify".
- **Imperative for instructions.** "Set `scopes`." Not "You should set `scopes`" or "You can
  now set `scopes`."
- **Product voice, not author voice.** Don't use "we" to mean the people who built the product.
  "We" is fine in tutorials for steps the reader is doing alongside the text ("Next, we add a
  cache").
- **Contractions are fine.** Use them where they read naturally.
- **Don't soften or pad.** Cut "simply", "just", "easily", "please", "note that", "in order to",
  and "it's worth mentioning". If something is important, the sentence should show it.

## Sentences and words

- **Keep sentences short.** Aim for under 25 words, one idea each. Split sentences that chain
  clauses with dashes or semicolons.
- **Condition before instruction.** "If the run fails, check the logs."
- **One term per concept.** Choose a name and keep it on the page. Don't alternate "app",
  "server", and "service" for the same thing.
- **Plain words.** "use", not "utilize"; "before", not "prior to"; "for example", not "e.g.";
  "make sure", not "ensure that".
- **Be specific.** Give the value, the limit, the name: "times out after 10 seconds", not "times
  out quickly".
- **Product names.** Use `{{< key product_name >}}` for text that differs between variants.
  Write "Union.ai" (not "Union AI" or "UnionAI") and "Flyte"; lowercase `flyte` only for the
  package, CLI, or module, in code. Write third-party names as their owners do: GitHub,
  Kubernetes (not "k8s"), Hugging Face. Say "data plane", never "compute plane".
- **Concepts are lowercase nouns.** "Create a task", "the environment". Capitalize only the
  literal API class, in backticks: `flyte.TaskEnvironment`.
- **Use the Oxford comma.** "tasks, apps, and triggers".

## Formatting

- **Code formatting** for anything the reader types or reads in code: identifiers, parameters,
  values, file names, paths, commands, environment variables. Write API identifiers fully
  qualified so the autolinker can link them.
- **Bold** for UI labels ("Click **Save**") and for the term being defined. Not for emphasis
  in prose.
- **UI paths** use bold labels and arrows: **Settings → Webhooks → Add webhook**.
- **Em dashes sparingly**, at most one per paragraph. A period is usually better.
- **Numbers:** numerals for values and units (`512Mi`, 10 seconds, 3 retries); words for one
  to nine in ordinary prose ("two options").

## Code examples

- **Runnable and tested.** Prefer embedding from `unionai-examples` with `{{< code >}}` and
  fragments, so CI exercises the code. Inline snippets must still be correct.
- **Complete enough to copy.** Include imports and the environment definition the snippet
  depends on, or show them once earlier on the page.
- **Realistic but minimal.** Use plausible names (`octo/repo`, `train_model`), not `foo` and
  `bar`, and leave out anything that doesn't serve the point.
- **Comments say what, not why we built it this way.** Example comments render in the docs and
  follow this guide.
- **Shell commands** go in `bash` blocks without a `$` prompt. Show output in a separate block
  when it matters.
- **Placeholders** are explicit: `<your-project>`, and say what to replace them with.

## Notices

- **Use sparingly.** If every reader needs it, it belongs in the prose. More than two notices
  on a page usually means the page needs restructuring.
- **NOTE** adds useful context. **WARNING** prevents harm: data loss, a security exposure, a
  failed deployment, or a cost surprise.
- **Titles are optional.** If you use one, make it a short label ("Python 3.10 or later"), not
  a sentence. Text on the `[!NOTE]` line renders as the bold title.

## Links

- **Descriptive link text** that names the destination, such as "Caching", not "here" or
  "this page".
- **Link the first mention** of a related concept on a page, not every mention.
- **Relative links** within the docs; `{{< docs_home >}}` across variants. Never absolute
  URLs to `union.ai/docs`.

## Images

- **Alt text** that says what the image shows.
- **Screenshots** only where text can't do the job, cropped to the relevant area. They go stale
  with every UI change.

## Before you finish

Read the page as a new user would. Then:

- Remove sentences that recount history, defend a design, or tell the reader how to feel.
- Remove anything stated earlier on the page or on its landing page.
- Check that the first screen tells the reader what the feature does and shows how to use it.
- Check that every code block runs.
