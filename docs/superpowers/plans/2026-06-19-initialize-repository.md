# Self-Media Compliance Review Repository Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a standalone Git repository for the self-media compliance review Codex skill.

**Architecture:** Keep the reusable skill under `skills/self-media-compliance-review/`, with platform-specific policies in one-level reference files. Project-level docs explain installation, sources, validation, and maintenance without duplicating the rule catalogs.

**Tech Stack:** Markdown, Bash, Codex skill metadata, Git.

## Global Constraints

- Preserve the existing `self-media-compliance-review` skill content.
- Keep platform rule catalogs inside `skills/self-media-compliance-review/references/`.
- Provide a local validation command before GitHub push.
- Do not modify the existing `capsule-cinema` repository.

---

### Task 1: Repository Scaffold

**Files:**
- Create: `/Users/june2/code/github/self-media-compliance-review/README.md`
- Create: `/Users/june2/code/github/self-media-compliance-review/docs/sources.md`
- Create: `/Users/june2/code/github/self-media-compliance-review/scripts/validate.sh`
- Create: `/Users/june2/code/github/self-media-compliance-review/.gitignore`
- Create: `/Users/june2/code/github/self-media-compliance-review/LICENSE`
- Copy: `/Users/june2/.codex/skills/self-media-compliance-review/` to `/Users/june2/code/github/self-media-compliance-review/skills/self-media-compliance-review/`

**Interfaces:**
- Consumes: local Codex skill at `$HOME/.codex/skills/self-media-compliance-review`.
- Produces: a Git-ready project with `./scripts/validate.sh`.

- [x] **Step 1: Create the repository directory and skill folder**

Run:

```bash
mkdir -p /Users/june2/code/github/self-media-compliance-review/skills
```

- [x] **Step 2: Copy the existing skill**

Run:

```bash
cp -R /Users/june2/.codex/skills/self-media-compliance-review \
  /Users/june2/code/github/self-media-compliance-review/skills/
```

- [x] **Step 3: Add project docs and validation script**

Create README, source documentation, `.gitignore`, `LICENSE`, and `scripts/validate.sh`.

- [x] **Step 4: Run validation**

Run:

```bash
cd /Users/june2/code/github/self-media-compliance-review
chmod +x scripts/validate.sh
./scripts/validate.sh
```

Expected: `Validation passed.`

- [x] **Step 5: Initialize Git**

Run:

```bash
cd /Users/june2/code/github/self-media-compliance-review
git init
git status --short
```

Expected: new repository initialized with project files staged or unstaged for initial commit.
