# Pitchfork Data Sovereignty

## Purpose

This document defines the data sovereignty direction for Pancakes, Pitchfork, Redwitch, Nexus, ambient clients, and Pancakes nodes.

It translates the project's privacy and non-exploitation principles into governance requirements: who controls data, how consent works, where data can live, what secondary use is forbidden, and how communities retain authority over shared records.

## Core Principle

Pancakes and Pitchfork must reject the idea that human life data is ownerless platform material.

Data belongs inside a relationship:

```text
person or community
-> node governance
-> explicit purpose
-> permissioned use
-> accountable processing
-> export, revocation, and deletion rights
```

The system should be useful because it respects these boundaries, not because it quietly collects more data than people understand.

## What Data Sovereignty Means Here

Data sovereignty has several overlapping meanings in this project:

- Personal sovereignty: a person can understand, control, export, and revoke use of their own records.
- Node sovereignty: a household, guild, cooperative, institution, or community can govern its own node policy.
- Community sovereignty: some data is collective and must be governed by the community it concerns, not only by an outside operator.
- Jurisdictional sovereignty: hosted infrastructure, vendors, backups, and AI providers may create legal exposure depending on where data is stored and who can access it.
- Cultural sovereignty: data about culture, land, tradition, ceremony, identity, or community knowledge requires protocols beyond ordinary product consent.

For ordinary Pancakes use, this means local ownership, readable permissions, and exit rights.

For Redwitch and other sensitive clients, this means local-first raw records, explicit consent, symbolic projection, and strong deletion rights.

For community or Indigenous data, this means community-led governance, free and informed consent, and respect for applicable protocols such as OCAP, CARE, or a community's own rules.

## Design Requirements

### 1. No Digital Terra Nullius

Do not treat data as ownerless because it is visible, technically accessible, or useful.

This applies to:

- User-entered records.
- Household records.
- Guild records.
- Community records.
- Public or semi-public posts.
- Imported files.
- Exports.
- Logs.
- Derived records.
- Aggregates.

Use requires a purpose, a permission boundary, and a governance answer.

### 2. Continuity Of Consent

Consent should be specific, understandable, revocable, and renewed when purpose changes.

Avoid:

- "Accept all" consent for unrelated purposes.
- Broad consent hidden in terms of service.
- Retroactive consent.
- Consent that cannot be withdrawn.
- Consent that is required for unrelated essential functionality.

A permission grant should identify:

- Data class.
- Client or service.
- Purpose.
- Allowed event types.
- Allowed projection types.
- Whether AI processing is involved.
- Whether data leaves the node.
- Expiration or review date where appropriate.
- Revocation behavior.

### 3. Local And Community-Controlled Storage

Sensitive raw data should stay local whenever possible.

Local can mean:

- Device-local storage.
- A personal node.
- A household node.
- A self-hosted guild node.
- A community-controlled institutional node.
- Encrypted storage with keys controlled by the user or node.

Hosted Pancakes can exist, but hosted storage must be a choice with visible boundaries, not the only valid architecture.

### 4. No Scraping Or Silent Collection

The system must not silently collect data that the user did not intentionally enter, authorize, import, connect, or generate through an understood workflow.

Do not scrape node data into:

- AI training.
- Engagement analytics.
- Advertising systems.
- Behavioral prediction.
- Search indexes.
- Research datasets.
- Vendor tools.
- Debug logs.

Any secondary processing must be explicit, scoped, logged where appropriate, and revocable for future use.

### 5. Transparency Of Access

Sensitive access should leave a record that can answer:

- Who accessed the data?
- Which client or service accessed it?
- What class of data was accessed?
- For what purpose?
- Which permission grant allowed it?
- When did it happen?
- Was AI processing involved?
- Was data exported, synced, or shared?

Audit records should avoid storing sensitive payloads.

### 6. Anti-Coercive UX

Essential use should not require broad data sharing.

Avoid designs where people must trade privacy for basic access, household participation, guild status, care coordination, or game progression.

Risky patterns include:

- Guild rewards that pressure disclosure of sensitive state.
- Household dashboards that expose private care or health patterns.
- AI features that become mandatory for core flows.
- Hosted sync that is required when local use would work.
- Research or product validation framed as normal gameplay.

## Raw, Derived, Symbolic, Aggregate

The system should distinguish data forms clearly.

| Form | Meaning | Default Posture |
| --- | --- | --- |
| Raw record | Original client data, such as journal text, cycle details, or location traces | Keep local and private |
| Derived event | Minimal accounting event, such as movement logged or rest ritual complete | Permissioned and scoped |
| Symbolic projection | Ambiguous client interpretation, such as red moon or dream resonance | Preferred for cross-client sharing |
| Aggregate product | Group-level output created for research, validation, planning, or sale | Requires governance, opt-in, thresholds, and audit |
| Economic settlement | Record needed for covenant, pool, credit, or payment consistency | Minimized, audited, separated from intimate data |

Do not preserve raw sensitive records merely because a derived event or projection used them.

## Redwitch And Sensitive Domains

Redwitch, mood, sleep, fertility, symptoms, caregiving, trauma-adjacent reflection, child or dependent records, and health-adjacent rituals need stronger rules.

Defaults:

- Private by default.
- Local-first raw records.
- Symbolic projection only for shared clients.
- Explicit permission grants.
- Opt-in sharing.
- No public leaderboards.
- No guild pressure.
- No hidden AI processing.
- No secondary research or resale without separate governance.

Example:

```text
Redwitch local record:
cycle detail, symptom note, private reflection

Allowed shared projection:
red_moon_projection enabled for a private ambient world

Not allowed:
raw cycle phase exposed to Nexus, guild systems, analytics, or AI by default
```

## Community And Indigenous Data

Some data is governed collectively.

This may include:

- Indigenous data.
- Cultural knowledge.
- Land-based records.
- Community health or wellness data.
- Household or caregiving data involving multiple people.
- Guild or cooperative records.
- Institutional records about a served population.

Community data governance should define:

- Authority to collect.
- Authority to share.
- Authority to revoke future use.
- Steward and custodian roles.
- Benefit-sharing rules.
- Forbidden uses.
- Export and migration rights.
- Dissolution rules.
- External protocols or legal requirements.

If Indigenous data or community-specific cultural data is involved, the project must not reduce governance to an individual checkbox. Relevant frameworks such as OCAP and CARE can guide review, but the applicable community's own governance process is the source of authority.

## AI And Data Sovereignty

AI features must remain bounded.

Allowed direction:

- User-initiated tools.
- Narrow context.
- Temporary processing.
- Local or node-controlled processing where possible.
- No training without explicit consent.
- Visible records of what was processed.
- Clear deletion behavior.

Forbidden direction:

- Silent ingestion.
- Ambient life summarization.
- Training on private logs by default.
- AI judgments of health, productivity, worth, relationship quality, or care.
- Vendor processing without clear jurisdiction, retention, and secondary-use terms.

Sovereign or local AI infrastructure can reduce some risks, but it does not replace consent, minimization, audit, or community governance.

## Vendor And Hosting Requirements

Any external vendor that can access project data should be evaluated for:

- Data residency.
- Legal jurisdiction.
- Subprocessors.
- Retention.
- Training use.
- Logging.
- Breach notification.
- Export support.
- Deletion support.
- Contractual limits on secondary use.

Data stored in a country is not automatically sovereign if the provider, subprocessors, keys, logs, or legal control sit elsewhere.

## Deletion, Export, And Retention

Users and communities need exit rights.

The system should support:

- User-owned exports.
- Node-level exports.
- Encrypted sensitive exports.
- Signed exports where identity continuity matters.
- Import/migration between nodes.
- Deletion from active records.
- Projection cleanup.
- Backup expiry.
- Minimal audit retention only where justified.

Deletion should distinguish raw records from derived accounting residues.

Raw sensitive records should be deletable wherever feasible. Minimized audit or settlement records may remain only when needed for security, legal compliance, or covenant/economic consistency.

## Risk Register Inputs

The following risks should be represented in privacy, security, and product review:

| Risk | Description | Controls |
| --- | --- | --- |
| Data treated as ownerless | User or community data is reused without authority | Explicit permissions, no scraping, purpose limitation |
| Bundled consent | People must accept broad use to access basic features | Granular consent, anti-coercive UX, revocation |
| Hidden secondary use | Data enters AI, analytics, research, or vendor systems unexpectedly | Processing records, vendor review, no hidden training |
| Community governance failure | Collective data is handled as individual product data | Node governance, steward roles, community protocols |
| Hosted centralization | Convenience hosting becomes mandatory platform capture | Self-hosting, virtual nodes, export/import |
| Retention overreach | Sensitive records remain after purpose ends | Retention policy, raw-record deletion, backup expiry |
| Aggregate harm | Aggregates reveal or pressure small groups | Thresholds, opt-in, risk review, data product governance |

## Working Rule

Before collecting, syncing, projecting, analyzing, training on, exporting, selling, or sharing data, answer:

- Whose data is this?
- Is it individual, shared, community, or institutional?
- What purpose justifies this use?
- What permission grant allows it?
- Can the feature work with less data?
- Can raw data stay local?
- Can shared state be symbolic instead?
- Who can revoke future use?
- Who can export it?
- Who can delete it?
- What harm follows if it leaks?
- Does community governance apply?

If the answers are unclear, the feature is not ready.
