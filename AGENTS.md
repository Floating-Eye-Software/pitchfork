# Pitchfork Codex Instructions

This repository uses `_work/` for local workflow management.

Before code or content changes, Codex should check:

- `_work/README.md`
- `_work/repo-workflow.md`
- `_work/todo.csv`
- `_work/plans/plans.csv`
- the relevant `_work/plans/*.md` file when one applies

Pitchfork owns shared domain contracts, accounting and settlement semantics,
resource-state transitions, projection derivation, and database-independent
persistence interfaces.

Route broader concerns to their authoritative repositories:

- `../pancakes` for node applications, physical databases, migrations,
  identity, permissions, governance, and Pancakes product behavior
- `../site-ops` for deployment, hosting, DNS, TLS, and live-site operations
- `../fley-org` for organization-level coordination and repository governance
- `../fley-qms` for controlled SOP, WI, CAPA, Change Control, and controlled
  privacy, health, safety, compliance, or regulatory review

Do not expose credentials, private user data, raw private records, or secrets
in committed files.

When the user says `wrap up`, `finish the session`, or equivalent, Codex should
perform the workflow maintenance described in `_work/repo-workflow.md`.

Do not commit unless the user explicitly asks.
