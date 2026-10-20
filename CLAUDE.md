# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal knowledge base of Markdown study notes (no application code, build, lint, or tests). Notes are grouped by topic folder: `algorhythems` (sic), `backend/DotNet`, `cloud/azure`, `dataStructures`, `database`, `devops` (docker, git, kubernates (sic), linux), `frontend`, `languages`, `misc`, `scripting`, `security`, `workflow-tools`. Images referenced by notes live in `images/`; draw.io sources in `diagrams/`. Folder names keep their original spelling — don't "fix" them, since README links and note cross-references depend on them.

## README.md is generated — do not edit it by hand

`README.md` is just a folder/file tree produced by `update-readme.py`, which walks the repo and rewrites the file from scratch (ignoring `.git`, `diagrams`, `images`, `.github`). The GitHub Action `.github/workflows/create-readme.yml` runs it on every push to `main` and auto-commits `*.md` changes ("auto-update readme file"). To regenerate locally:

```
python update-readme.py
```

Run it from the repo root (it uses relative `./` paths). Adding, renaming, or deleting a note only needs the script to be re-run (or the CI to do it); no manual index maintenance.

## Note conventions

- Notes are terse bullet-style Markdown with `##`/`###` headings, fenced code blocks tagged by language, and images referenced from `images/`.
- Put new notes in the matching topic folder (create a new folder only for a genuinely new topic) and match the style of neighbouring files.
