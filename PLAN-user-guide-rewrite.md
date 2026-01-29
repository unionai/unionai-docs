# User Guide Rewrite Plan: Sections 2-5

> **Status: IMPLEMENTED** - All changes have been made. See summary below.

## Target Audience
- Data scientists familiar with workflow orchestration (Airflow/Prefect) but new to Flyte
- Intermediate Python proficiency
- Not familiar with async/await (stick to sync code initially)
- Familiar with Docker/containers and cloud concepts through usage (not expert)

---

## New Structure Overview

| Order | Current Name | New Name | Weight | Purpose |
|-------|--------------|----------|--------|---------|
| 1 | `getting-started.md` | **Quickstart** | 2 | Minimal hello world, 5-minute success |
| 2 | `local-setup.md` | **Local setup** | 3 | Complete dev environment setup |
| 3 | `basic-concepts.md` | **Flyte basics** (folder) | 4 | Working examples + concepts for tasks |
| 4 | `first-project/` | **First project** (folder) | 5 | End-to-end intermediate project |

---

## Section 1: Quickstart (weight: 2)

**File:** `quickstart.md` (rename from `getting-started.md`)

**Purpose:** Get a task running on the backend in under 5 minutes. Immediate success.

**Content (minimal changes needed):**
- Inline minimal setup (already present)
- Hello world task example
- Run it remotely
- View in UI (screenshot already present)
- Link to "Local setup" and "Flyte basics" for next steps

**Changes from current:**
- Rename file from `getting-started.md` to `quickstart.md`
- Update title in frontmatter
- Review for any unnecessary content that can be trimmed
- Ensure links point to new section names

**Status:** Mostly done, minimal changes needed.

---

## Section 2: Local Setup (weight: 3)

**File:** `local-setup.md`

**Purpose:** Complete development environment setup for ongoing work.

**Content:**
- Prerequisites (Python, uv/pip)
- Installing the flyte package
- Configuration file basics:
  - `endpoint`
  - `project` and `domain`
  - `image.builder` (local vs remote, briefly)
- Authentication (flyte login)
- Verifying setup works

**Changes from current:**
- Move detailed config.yaml options to API reference (create ticket/TODO)
- Keep only essential settings inline
- Remove any content that duplicates Quickstart
- Add clear "what you'll need" prerequisites section

**Content to offload to reference:**
- Full config.yaml schema
- All `image.*` options
- Environment variable overrides
- Advanced authentication options

---

## Section 3: Flyte Basics (weight: 4)

**Folder:** `flyte-basics/` (replaces `basic-concepts.md`)

**Purpose:** Learn core Flyte concepts through working examples. Practical, not just definitions.

### Structure:

```
flyte-basics/
├── _index.md          # Overview: what you'll learn
├── task-environment.md # TaskEnvironment concept + example
├── tasks.md           # Defining and configuring tasks
└── runs-and-actions.md # Executing tasks, understanding runs and actions
```

### Page 1: `_index.md`
- Brief intro: "Now that you're set up, let's understand how Flyte works"
- Overview of concepts to be covered
- NO app content here

### Page 2: `task-environment.md`
**Concepts:** TaskEnvironment, container images, resources

**Content:**
- What is a TaskEnvironment?
- Hardware environment (CPU, memory, GPU)
- Software environment (container image, dependencies)
- Working example: define an environment with specific resources
- When to use one environment vs multiple

### Page 3: `tasks.md`
**Concepts:** Task, @env.task decorator, inputs/outputs, type hints

**Content:**
- What is a task? (A Python function that runs remotely)
- The `@env.task` decorator
- Parameters and return types
- Type hints and why they matter
- Working example: a task that processes data
- Brief mention: unlike Flyte 1, no separate `@workflow` - tasks call tasks

### Page 4: `runs-and-actions.md`
**Concepts:** Run, Action, execution hierarchy

**Content:**
- What is a Run? (User-initiated execution + all descendants)
- What is an Action? (Single task execution)
- How runs and actions relate
- Working example: run a multi-task workflow, observe in UI
- Understanding the UI: runs list, action details, logs

**What moves here from current content:**
- Definitions from `basic-concepts.md` (TaskEnvironment, Task, Run, Action)
- Content about running tasks from `first-project/running.md`

**What does NOT go here:**
- App, AppEnvironment (moved to First Project)
- Deployment (`flyte deploy`) - covered elsewhere

---

## Section 4: First Project (weight: 5)

**Folder:** `first-project/`

**Purpose:** End-to-end intermediate project. Train a model, serve it via an app.

### Structure:

```
first-project/
├── _index.md                # Overview: what we're building
├── introducing-apps.md      # Apps concept (moved from basic-concepts)
├── training-pipeline.md     # Part 1: Training tasks
├── serving-the-model.md     # Part 2: FastAPI app
└── connecting-training-to-serving.md  # Part 3: RunOutput, putting it together
```

### Page 1: `_index.md`
**Content:**
- What we're building: end-to-end ML workflow
- Architecture diagram: training pipeline → model artifact → serving app
- Prerequisites (completed Flyte Basics)

### Page 2: `introducing-apps.md`
**Concepts:** App, AppEnvironment, App vs Task distinction

**Content:**
- What is an App? (Long-running service vs run-to-completion task)
- AppEnvironment configuration
- When to use Apps vs Tasks
- App-specific concepts: ports, scaling, authentication

**What moves here:**
- App and AppEnvironment definitions from current `basic-concepts.md`
- Conceptual content from current `serving-apps.md`

### Page 3: `training-pipeline.md`
**Content:**
- Define training TaskEnvironment
- Data preparation task
- Model fine-tuning task
- Orchestrating the pipeline (task calling task)
- Running the training

**Based on:** Current `model-training-and-serving.md` training sections

### Page 4: `serving-the-model.md`
**Content:**
- Define AppEnvironment with FastAPIAppEnvironment
- Create FastAPI application
- Request/response models
- Loading the model on startup
- Serving the app

**Based on:** Current `model-training-and-serving.md` serving sections + `serving-apps.md`

### Page 5: `connecting-training-to-serving.md`
**Content:**
- The RunOutput pattern
- Parameter configuration to reference training output
- Deploying the complete system
- Testing the API
- Best practices

**Based on:** Current `model-training-and-serving.md` connection sections

---

## Files to Remove/Merge

| File | Action |
|------|--------|
| `first-project/running.md` | **Remove** - content absorbed into Flyte Basics |
| `first-project/serving-apps.md` | **Remove** - content merged into `introducing-apps.md` and `serving-the-model.md` |
| `first-project/model-training-and-serving.md` | **Remove** - content split across 3 new pages |
| `basic-concepts.md` | **Remove** - replaced by `flyte-basics/` folder |

---

## Redundancy Removal Summary

1. **Running tasks remotely** - Currently explained in:
   - `getting-started.md` ✓ (keep in Quickstart)
   - `first-project/running.md` ✗ (remove, merge to Flyte Basics)
   - `task-deployment/_index.md` (separate section, OK to keep)

2. **Basic concepts definitions** - Currently scattered:
   - `basic-concepts.md` → **consolidate into Flyte Basics with examples**

3. **App serving basics** - Currently in:
   - `basic-concepts.md` (definitions)
   - `serving-apps.md` (hello world app)
   - `model-training-and-serving.md` (advanced)
   → **consolidate into First Project with proper intro**

---

## Style Guidelines for Rewrite

1. **Friendly, direct tone** - "Let's build..." not "The user should..."
2. **Show, then explain** - Code example first, then explanation
3. **Practical focus** - Every concept illustrated with working code
4. **Progressive complexity** - Build on previous sections
5. **No async in early sections** - Stick to sync code until explicitly introducing async
6. **Assume intelligence, not knowledge** - They're smart, just new to Flyte

---

## Open Questions / TODOs

1. [ ] Should `prefetching-models.md` stay in First Project or move elsewhere?
2. [ ] Create ticket to move detailed config.yaml docs to reference section
3. [ ] Verify example code in unionai-examples covers all needed scenarios
4. [ ] Decide on exact file naming conventions (kebab-case vs underscores)

---

## Implementation Order

1. ✅ Rename `getting-started.md` → `quickstart.md` (minimal changes)
2. ✅ Slim down `local-setup.md` (added Next steps section)
3. ✅ Create `flyte-basics/` folder and pages
4. ✅ Restructure `first-project/` folder
5. ✅ Remove deprecated files
6. ✅ Update all cross-references
7. Review for consistency (manual review recommended)

---

## Implementation Summary

**Files Created:**
- `content/user-guide/quickstart.md` (renamed from getting-started.md)
- `content/user-guide/flyte-basics/_index.md`
- `content/user-guide/flyte-basics/task-environment.md`
- `content/user-guide/flyte-basics/tasks.md`
- `content/user-guide/flyte-basics/runs-and-actions.md`
- `content/user-guide/first-project/introducing-apps.md`
- `content/user-guide/first-project/training-pipeline.md`
- `content/user-guide/first-project/serving-the-model.md`
- `content/user-guide/first-project/connecting-training-to-serving.md`

**Files Updated:**
- `content/user-guide/local-setup.md` (added Next steps)
- `content/user-guide/first-project/_index.md` (complete rewrite)
- `content/user-guide/_index.md` (link card updated)
- `content/user-guide/flyte-2/_index.md` (link updated)
- `content/user-guide/task-configuration/_index.md` (link updated)
- `content/user-guide/build-apps/_index.md` (link updated)

**Files Removed:**
- `content/user-guide/getting-started.md`
- `content/user-guide/basic-concepts.md`
- `content/user-guide/first-project/running.md`
- `content/user-guide/first-project/serving-apps.md`
- `content/user-guide/first-project/model-training-and-serving.md`
