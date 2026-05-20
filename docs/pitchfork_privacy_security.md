# Pitchfork Privacy and Security

## Purpose

This document defines the privacy and security direction for Pancakes, Pitchfork, Nexus, Redwitch, ambient symbolic clients, and Pancakes nodes.

The core privacy insight is:

```text
Encryption at rest is easy.
Secure processing is the hard part.
```

If a server needs to do useful work with data, that data often exists in decrypted form somewhere:

- In RAM.
- In an application process.
- In a browser.
- On a mobile device.
- In a local node.
- In an admin workflow.
- In an export.
- In a log.

The real question is not only:

```text
Can this data be encrypted?
```

The real question is:

```text
Who can decrypt it, when, where, for what purpose, and under what constraints?
```

Pancakes and Pitchfork should be designed around minimization, compartmentalization, explicit permission, local processing, auditability, and symbolic abstraction. They should not be designed around collecting everything and trusting encryption to make that safe.

## One-Sentence Summary

Sensitive life data should stay local whenever possible; shared systems should receive scoped, permissioned, symbolic, or aggregate projections rather than raw intimate records.

---

# Core Privacy Model

The strongest model for this ecosystem is:

```text
local intimate data
-> selective abstraction
-> permissioned symbolic projection
-> limited shared state
```

Not:

```text
all life data
-> one omniscient database
-> universal analytics
-> broad reuse
```

This is both safer and more aligned with the symbolic design direction.

## Privacy Goals

The system should make it possible to:

- Keep raw sensitive records local.
- Share derived symbolic state without exposing intimate facts.
- Use Pitchfork accounting without turning it into a life-surveillance ledger.
- Let each node choose its own identity and enforcement policies.
- Support cooperative pools and covenants without exposing unrelated personal data.
- Run useful clients even when some data never leaves a device.
- Limit breach impact through compartmentalization.
- Audit access to sensitive records.
- Export and delete personal records where feasible.
- Avoid hidden AI processing, analytics leakage, or secondary data use.

## Non-Goals

The system should not promise:

- Perfect safety.
- Magical encryption that preserves all server functionality.
- That hosted servers can process raw data without risk.
- That anonymization always prevents re-identification.
- That aggregate data is harmless.
- That admin access is safe without policy, logging, and technical limits.
- That blockchain storage is appropriate for sensitive personal data.

The realistic goal is:

```text
make compromise harder,
make breaches smaller,
make abuse more visible,
make sensitive processing rarer,
and make unsafe designs structurally difficult.
```

---

# Threat Model

Pancakes and Pitchfork handle unusually intimate data.

Threats include:

- External attackers stealing databases, backups, logs, or object storage.
- Network attackers observing traffic.
- Malicious or careless node administrators.
- Overbroad employee or steward access.
- Household, guild, or institutional coercion.
- Accidental sharing through bad permissions.
- Sensitive data leaking into logs, analytics, error reports, or AI tools.
- Re-identification from aggregate data.
- Future buyers, sponsors, insurers, employers, or advertisers misusing data.
- Loss of devices, keys, or backups.
- Legal or institutional pressure to disclose records.
- Blockchain immutability preserving data that should have remained deletable.

The design should assume mistakes happen.

Security should not depend on one perfect control.

---

# Data Classification

Every record should have a data classification.

## Data Classes

| Class | Examples | Default Handling |
| --- | --- | --- |
| Public | Published announcements, public project docs | Shareable |
| Node-shared | Guild notices, covenant boards, shared schedules | Visible under node policy |
| Household or group | Chores, shared rituals, group inventories | Scoped to approved members |
| Personal | Ritual history, private tasks, personal inventory | Private by default |
| Sensitive | Journals, mood, sleep notes, cycle data, symptoms, location traces, household conflict | Local-first, minimized, explicit permission |
| Regulated or high-risk | Clinical trial records, medical data, child/dependent data, pregnancy-related data, financial aid eligibility | Separate mode, stricter controls |
| Economic | Cooperative pools, payments, treasuries, grants, escrow, wallet-linked state | Strong audit, separation from intimate data |
| Cryptographic secrets | GPG private keys, recovery keys, signing keys, wallet keys | Never stored casually by application servers |

## Sensitive Categories

Sensitive data includes:

- Menstrual cycles.
- Fertility awareness.
- Sexual health.
- Pregnancy-related data.
- Symptoms.
- Mood.
- Mental health.
- Sleep quality.
- Raw journals.
- Trauma-adjacent reflections.
- Household conflict.
- Caregiving patterns.
- Location history.
- Children or dependent records.
- Financial vulnerability.
- Identity documents or verified identity claims.

Sensitive categories should not be used for public scoring, leaderboards, guild pressure, market rewards, or speculative value.

---

# Privacy Layers

Privacy is layered.

No single layer is enough.

## 1. Encryption At Rest

Encryption at rest protects:

- Databases.
- Disks.
- Backups.
- Object storage.
- Device storage.

It helps if hardware, snapshots, or backup media are stolen.

But it does not stop an authorized application server from reading data while running.

Encryption at rest is a baseline, not a complete privacy model.

## 2. Encryption In Transit

Encryption in transit protects traffic between:

- Browser and server.
- App and node.
- Node and node.
- Node and hosted service.

HTTPS/TLS should be mandatory for hosted services and node-to-node communication.

But after the server receives data, the server can usually read it unless the data is end-to-end encrypted or otherwise protected.

## 3. Application-Layer Permissions

Application permissions are the core of practical privacy.

Examples:

```text
User A should not see User B's cycle data.
Guild members should not see private journal entries.
Admins should not casually inspect emotional logs.
Nexus projections should not expose raw Redwitch state.
AI tools should not see private records without explicit scope.
```

Most real failures happen here:

- Bad defaults.
- Overbroad access.
- Broken authorization checks.
- Sensitive data in logs.
- Analytics leakage.
- Accidental sharing.
- Employee or steward overreach.
- Export mistakes.

Permissions need tests, audits, simple defaults, and visible user controls.

## 4. Capability Separation

Capability separation means different parts of the system are allowed to do different things.

Example:

| Component | Allowed To Know |
| --- | --- |
| Redwitch local client | Detailed cycle records |
| Pitchfork ledger | Abstract symbolic event or settlement result |
| Minecraft-like client | Red moon projection is active |
| Nexus | Dream district resonance changed |
| Guild systems | Nothing unless explicitly shared |
| Public projections | Only generalized or aggregate signals |

This separation is more important than any single encryption feature.

## 5. Auditability

Sensitive access should leave a trail.

Audit logs should record:

- Who accessed data.
- What class of data was accessed.
- When access happened.
- Which client or service requested it.
- Which permission grant allowed it.
- Whether data was exported, shared, or processed by AI.
- Whether admin override was used.

Audit logs should avoid storing the sensitive content itself.

## 6. Operational Discipline

Privacy depends on operations:

- Least privilege.
- Admin access controls.
- Key rotation.
- Backup protection.
- Incident response.
- Dependency updates.
- Security review.
- Access review.
- Breach notification.
- Data retention limits.

Operational failure can defeat good architecture.

---

# Local-First Sensitive Data

The default for sensitive raw data should be local-first.

Examples of data that should usually remain local:

- Raw journal text.
- Cycle details.
- Symptom details.
- Emotional reflections.
- Sleep notes.
- Trauma-adjacent material.
- Detailed location traces.
- Private household conflict notes.

Local-first can mean:

- Stored only on the device.
- Stored only on a self-hosted node.
- Stored encrypted with keys controlled by the user or node.
- Synced only through explicit selective sync.
- Never sent to hosted Pancakes by default.

## Derived Symbolic Events

Servers and shared clients should usually receive derived symbolic events.

Example:

```text
Local Redwitch state:
late-cycle phase with symptoms

Shared symbolic projection:
dream_moon_resonance +2
red_moon_projection enabled
```

The shared system should not need to know:

- Exact cycle phase.
- Fertility status.
- Symptoms.
- Sexual activity.
- Pregnancy-related details.
- Medical notes.

## Projection Rule

Before sharing data outside its origin client, ask:

```text
Can this be represented as a symbolic projection instead of a raw fact?
Can this projection be local-only?
Can this projection be visible only to trusted participants?
Can this projection be generalized or aggregated?
Can this feature work without sharing the data at all?
```

If the answer is yes, prefer the safer representation.

---

# Event Boundaries

Different layers should know different things.

## Example: Redwitch To Ambient Client

| Layer | Knows |
| --- | --- |
| Redwitch local client | Detailed cycle data |
| Pitchfork ledger | Abstract symbolic event |
| Ambient client | Red moon projection active |
| Nexus | Dream district resonance changed, if permitted |
| Guild systems | Nothing |
| Public systems | Nothing |

## Example: Household Ritual

| Layer | Knows |
| --- | --- |
| Pancakes household client | A specific household ritual was completed |
| Pitchfork | Order Salt generated under household scope |
| Nexus | Sanctuary district stability increased |
| Guild systems | Only if household contributed to a guild covenant |
| Public systems | Nothing |

## Example: Movement

Movement can be low-risk or high-risk depending on detail.

| Data | Risk |
| --- | --- |
| "Movement ritual completed" | Lower |
| Step count | Medium |
| Route trace | High |
| Home/work inference | High |
| Real-time location | Very high |

The system should prefer coarse movement events over precise location traces.

---

# End-To-End Encryption

End-to-end encryption means the server cannot read the protected content because only user-controlled devices have the keys.

This is appropriate for:

- Private journals.
- Sensitive messages.
- Health-adjacent notes.
- Cycle details.
- Private household records.
- Personal exports.

But E2EE limits server functionality.

If the server cannot read content, it cannot easily:

- Search it.
- Summarize it.
- Analyze it.
- Moderate it.
- Generate recommendations from it.
- Build aggregate projections from it.

That is a feature for sensitive data, not a bug.

## E2EE Design Principle

Use E2EE where the server has no legitimate need to inspect content.

Use derived symbolic events where shared systems need limited state.

Do not weaken E2EE just to make analytics, AI, or engagement features easier.

---

# Identity And Access

Identity is node-governed.

Pancakes Identity should provide a shared abstraction for:

- Local accounts.
- GPG identities.
- Ontario Digital ID Program integration.
- Pseudonymous continuity.
- Verified claims.
- Membership.
- Consent grants.
- Permission scopes.
- Covenant signing.
- Export authority.
- Role-based access.

Each node decides which identity methods it accepts.

Pitchfork consumes verified identity claims and permission grants, but should not impose one global identity provider.

## Identity Assurance

Different contexts need different assurance levels.

| Context | Likely Identity Need |
| --- | --- |
| Personal node | Local account or device identity |
| Household node | Local accounts, invitations, possibly GPG |
| Guild node | GPG, pseudonymous continuity, invite trust |
| Cooperative pool | Stronger member verification |
| Institutional node | Role-based access and higher assurance |
| Regulated research | Separate verified consent and eligibility workflow |

High-assurance identity should be used only when it provides real value. Forcing real-world identity everywhere would harm privacy and pseudonymous communities.

---

# Admin Access

Admins, stewards, and custodians are powerful.

The architecture should avoid casual admin access to sensitive records.

## Admin Controls

Admin access should be:

- Role-based.
- Least-privilege.
- Logged.
- Reviewable.
- Limited by data class.
- Separated from ordinary user access.
- Justified for sensitive overrides.

For hosted Pancakes, employee or operator access to sensitive user data should be exceptional, logged, and policy-bound.

For self-hosted nodes, the UI should make local administrator power clear to members.

## Break-Glass Access

Some institutional contexts may require emergency access.

Break-glass access should:

- Be disabled by default where not needed.
- Require a reason.
- Notify the affected user where appropriate.
- Be logged prominently.
- Be reviewed by stewards or compliance roles.
- Avoid exposing unrelated data.

---

# Logging, Analytics, And AI

Sensitive data often leaks through secondary systems.

## Logs

Do not log:

- Journal text.
- Cycle details.
- Symptoms.
- Mood entries.
- Location traces.
- Private messages.
- Secrets.
- Raw identity documents.
- Access tokens.
- Full request payloads for sensitive endpoints.

Logs should contain identifiers and metadata only where needed for debugging, audit, and security.

## Analytics

Analytics should be:

- Opt-in or strongly minimized.
- Aggregated.
- Free of sensitive payloads.
- Node-configurable.
- Disabled for sensitive clients by default.

Avoid third-party analytics in sensitive surfaces.

## AI Processing

AI must have a visible boundary.

Do not build:

- Silent ingestion of private life data.
- Universal life summarization.
- Hidden model training on private logs.
- AI judgments of productivity, care, health, relationship quality, or worth.
- Household surveillance framed as convenience.

Build instead:

- Explicit AI tools.
- Narrow scopes.
- Temporary context.
- Local processing where possible.
- Clear records of what was processed.
- Clear deletion.
- No training without explicit consent.

For example:

```text
OK:
Summarize this selected journal entry on my device.

Not OK:
Continuously read all journals and infer emotional trends for the server.
```

---

# Aggregate Data And Research

Aggregate data can still harm people.

Risks include:

- Re-identification.
- Small-group exposure.
- Buyer misuse.
- Household or guild pressure.
- Sensitive health or fertility inference.
- Communities becoming dependent on data sales.
- Participation becoming a new extraction pipeline.

Aggregate data products should require:

- Clear purpose.
- Named recipient or buyer.
- Included fields.
- Excluded fields.
- Minimum group-size threshold.
- Re-identification risk review.
- Member opt-in.
- Expiration date.
- Revenue distribution terms if money is involved.
- Audit trail.

## Hard Lines

Do not support:

- Secret data sales.
- Retroactive consent.
- Broad consent hidden in terms of service.
- Raw personal-log resale.
- Health-data resale to advertisers.
- Insurance, employment, credit, or policing uses.
- Sponsor access to private household data.
- Guild leaders coercing members into research.
- Selling data from children or dependents without special protections.

## Clinical Trial Mode

Clinical trials are not ordinary Pancakes activity.

If a node ever supports clinical trials or health-product validation, that should be a specialized regulated mode with:

- Independent ethics review where required.
- Informed consent.
- Clear sponsor identity.
- Protocol registration where required.
- Eligibility criteria.
- Adverse-event reporting.
- Separation from ordinary game rewards.
- No coercion through guild status, household pressure, or economic dependency.
- Extra protections for vulnerable groups.
- No hidden secondary use of health data.

Pancakes should not present clinical trial participation as a game quest.

---

# Event Streams And Projection Buses

Design notes propose IRC-like structures as append-only event streams, social ledgers, or projection buses.

This is a useful idea if treated carefully.

Possible channels:

```text
#guild.stonebound
#world.leyroad
#ledger.archive
#rituals.personal
```

These channels may be useful for:

- Append-only event flow.
- Projection input.
- Social history.
- Debugging world state.
- Covenant activity.
- Guild-visible events.

But an event stream must not replace:

- Databases.
- Permission checks.
- Projection rules.
- Data classification.
- Retention policy.
- Deletion/export workflows.

## Channel Privacy Rules

Each event stream or channel should have:

- Owner.
- Scope.
- Data classification.
- Read permissions.
- Write permissions.
- Retention period.
- Export policy.
- Redaction policy.
- Whether sensitive data is forbidden.
- Whether events are raw, derived, or projected.

Private channels should not casually feed public projections.

Public channels should never contain raw sensitive events.

---

# Backups, Export, And Deletion

Backups and exports are common privacy failure points.

## Backups

Backups should be:

- Encrypted.
- Access-controlled.
- Documented.
- Test-restored.
- Retained for limited periods.
- Separated by node where possible.
- Clear about whether deleted data remains temporarily recoverable.

## Exports

Exports should be:

- User-initiated.
- Human-readable where possible.
- Machine-readable where useful.
- Scoped by data class.
- Encrypted for sensitive data.
- Signed where identity continuity matters.

GPG can be useful for signed exports and encrypted archives.

## Deletion

Deletion should distinguish:

- Delete from active database.
- Delete from projections.
- Delete from indexes.
- Delete from backups after retention period.
- Preserve minimal audit record where legally or operationally necessary.
- Preserve economic settlement records where deletion would break covenant accounting.

Sensitive raw records should be easier to delete than public, economic, or legally significant records.

Blockchain-backed state should never contain sensitive personal data because deletion may be impossible.

---

# Compliance Direction

This document is architecture guidance, not legal advice.

Still, the system should be designed to support privacy obligations such as:

- Consent.
- Transparency.
- Data minimization.
- Purpose limitation.
- Access rights.
- Correction rights.
- Deletion rights.
- Portability.
- Security safeguards.
- Breach notification.
- Auditability.

Medical, clinical, child-related, financial, employment, insurance, or regulated research uses require separate legal and compliance review before implementation.

---

# Implementation Phases

## Phase 1: Local And Simple

Build:

- Local Pitchfork accounting module.
- Local users.
- Basic permissions.
- Data classification field.
- Sensitive data stays in originating client.
- Symbolic derived events.
- No third-party analytics.
- No AI ingestion.
- Export/import.

## Phase 2: Node Privacy

Add:

- Node policy.
- Role-based access.
- GPG identity support.
- Encrypted backups.
- Audit logs for sensitive access.
- Permission-scoped projections.
- Admin visibility controls.
- Channel/event-stream scopes if used.

## Phase 3: Multi-Client Privacy

Add:

- Explicit client permission grants.
- Cross-client projection registry.
- Redwitch-to-ambient symbolic projection boundaries.
- Nexus projection rules.
- Sensitive-client test cases.
- Retention policy by data class.

## Phase 4: High-Assurance And Regulated Modes

Add only when needed:

- Ontario Digital ID Program integration.
- Cooperative pool compliance workflows.
- Research or clinical-trial mode.
- Stronger consent records.
- Independent review workflows.
- Aggregate data product governance.

---

# Design Checklist

Before adding a feature, answer:

- What raw data does this collect?
- Can the feature work with less data?
- Can raw data stay local?
- Can shared state be symbolic or aggregate?
- Who can see the data?
- Who can export it?
- Who can delete it?
- Does admin access expose it?
- Does it enter logs, analytics, AI tools, or backups?
- What happens if this data leaks?
- Could a household, guild, employer, insurer, or sponsor misuse it?
- Does this create pressure to disclose sensitive state?
- Does it need a separate regulated mode?
- Is the permission understandable to a normal person?

If these questions cannot be answered clearly, the feature is not ready.

---

# Working Assumption

The safest early architecture is:

```text
local-first sensitive records
-> minimal Pitchfork event
-> capped symbolic accounting
-> permissioned projection
-> client-specific display
```

The system should succeed by doing less with raw data, not by collecting everything and hoping access controls are enough.

Privacy is not an afterthought for Pancakes and Pitchfork. It is one of the main architectural boundaries that lets the rest of the system exist.
