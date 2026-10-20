---
name: read-from-docs
description: >
  Answer a question from the CodingBook notes (the Markdown files in this repo) first, then add detail
  from other sources (Microsoft Learn and official docs on the web) and give one cited answer. Use when the user says "check my notes", "what do my docs say
  about X", "look it up in the docs", "read from docs", or asks about a topic these notes cover (.NET/C#,
  Azure, SQL, Kubernetes/Helm, Docker, Git, Linux, React/Angular, TypeScript, Python, regex, cron, etc.),
  even if they don't mention the docs.
---

# Read from docs

Answer from the user's own notes first. Then add verified detail from other sources. The answer must
always show which parts came from the notes and which came from elsewhere.

## Step 1: Search the notes

The notes are Markdown files under the repo root (`E:\learning\CodingBook`), grouped by topic folder.
`file-list.txt` and `README.md` list every file. Skip `images/`, `diagrams/` and `.github/`.

1. Pick 2–5 search terms from the question: the main term, synonyms, abbreviations, and the folder's
   own spelling (folders are named `algorhythems` and `kubernates`).
2. Run `Grep` (case-insensitive, `glob: "**/*.md"`, `output_mode: "files_with_matches"`) to find
   candidate files. Also check whether a file *name* or folder matches the topic, e.g.
   `devops/kubernates/helm.md` for a Helm question.
3. `Read` the relevant sections, not just the matching line. Notes are short bullet lists, so the
   context sits under the nearest `##`/`###` heading.
4. Keep track of the file path and heading for every fact you take from the notes.

If nothing relevant turns up, tell the user the notes don't cover the topic and continue with Step 2.

## Step 2: Add detail from other sources

Use these to fill gaps, check what the notes say, and add examples. Pick the sources that fit the topic:

| Topic | Source |
|---|---|
| .NET, C#, Azure, SQL Server, PowerShell, AKS, Azure DevOps | `microsoft_docs_search`, then `microsoft_docs_fetch` for depth; `microsoft_code_sample_search` for code |
| Everything else (Kubernetes, Docker, React, Python, Git, …) | `WebSearch` (standard mode), then `WebFetch` on the official docs page |

These tools are deferred, so load the ones you need with a single `ToolSearch` call.
Never use Jira or Confluence (Atlassian tools) as a source.
Prefer official documentation over blogs. Use at most 3–4 lookups unless the question really needs more.

## Step 3: Write the answer

Use this structure:

```
## <Topic>

**From your notes** — `path/to/file.md` › <heading>
- <what the notes say, briefly>

**More detail**
- <added facts, examples or corrections> ([source title](url))

**Example** (if useful)
<code block>

**Gaps / corrections** (only if any)
- <where the notes are out of date, incomplete or wrong, and the source that says so>
```

Rules:
- Every fact gets a source: a note path or a link. Never present web content as coming from the notes.
- If an outside source contradicts the notes, say so plainly and name both sources.
- Keep the answer about as terse as the notes themselves.
- Don't edit any note unless the user asks for it. At the end, offer in one line to add the new
  detail to the relevant note (and then `python update-readme.py` if a file was added or renamed).
