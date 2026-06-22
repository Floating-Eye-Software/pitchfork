# Pitchfork Contracts

## Status

Proposed Architecture

Draft

Companion to:

* Pitchfork System Overview
* Pitchfork Client API Spec
* Pancakes Node Infrastructure
* Service Exchange
* Mentor Ecosystem
* Future Covenant Specifications

---

# Purpose

This document defines the contract architecture for Pitchfork.

Pitchfork already provides:

* events,
* permissions,
* inventories,
* settlement,
* cooperative pools,
* symbolic projections,
* and future economic infrastructure.

Contracts provide the missing coordination layer.

They allow people, households, guilds, institutions, and nodes to express:

* commitments,
* expectations,
* responsibilities,
* permissions,
* limits,
* procedures,
* timelines,
* governance,
* and settlement rules.

The contract system should be expressive enough to model:

* participation rewards,
* rituals,
* service exchange,
* subscriptions,
* grants,
* household agreements,
* guild projects,
* cooperative pools,
* governance procedures,
* standing services,
* constitutions,
* and future covenant systems.

The goal is not to recreate legal systems or smart-contract platforms.

The goal is to provide a humane coordination substrate.

---

# Core Principle

A contract answers:

```text
Who
may or must do
what
under what conditions
during what time period
subject to what limits
resulting in what consequences
visible to whom
and governed by whom.
```

---

# Design Principles

## Contracts Coordinate

Contracts coordinate activity.

They are not primarily mechanisms for punishment.

---

## Contracts Are Human-Readable

Normal people should be able to understand:

* who is involved,
* what is expected,
* what happens,
* how decisions are made,
* and how the contract ends.

---

## Contracts Are Composable

Complex agreements should be constructed from reusable primitives.

Example:

```text
obligations
+
conditions
+
quotas
+
settlement
=
participation covenant
```

---

## Contracts Are Node-Governed

Pitchfork accounts.

Clients interpret.

Identity authorizes.

Nodes govern.

Contracts should preserve these boundaries.

---

## Contracts Prefer Restoration Over Punishment

Many contracts should default to:

```text
obligation unmet
→ no settlement
```

rather than:

```text
obligation unmet
→ punishment
```

The system should avoid turning ordinary life into behavioral wage labor.

---

# Contract Model

Minimum fields:

```text
Contract
- id
- type
- version
- title
- description
- state
- parties
- authority
- terms
- obligations
- conditions
- quotas
- procedures
- settlement
- enforcement
- timeline
- permissions
- visibility
- audit
- metadata
```

---

# Contract Types

Suggested types:

```text
participation
ritual
household
service_exchange
subscription
grant
guild_project
cooperative_pool
resource_access
governance
economic
covenant
service
constitution
custom
```

---

# State Machine

Contracts are processes.

Suggested states:

```text
draft
proposed
accepted
active
suspended
fulfilled
expired
terminated
void
```

---

# Parties

Parties participate in contracts.

```text
Party
- id
- type
- role
```

Party types:

```text
actor
household
guild
node
organization
service_pool
anonymous
```

Roles:

```text
promisor
beneficiary
participant
witness
steward
sponsor
arbitrator
observer
```

---

# Authority

Authority determines who may create, modify, or terminate contracts.

```text
Authority
- owner
- required_signatures
- modification_policy
- termination_policy
```

Examples:

```text
single owner
unanimous consent
majority vote
two-of-three stewards
```

---

# Terms

Terms are plain-language descriptions.

```text
Term
- id
- description
- category
```

Terms provide meaning.

They do not directly produce settlement.

---

# Obligations

Obligations describe expected actions.

```text
Obligation
- id
- actor
- action
- frequency
- required
- repeatable
```

Examples:

```text
walk
study
teach lesson
review proposal
repair equipment
provide care
```

---

# Conditions

Conditions determine when obligations apply.

```text
Condition
- trigger
- predicate
- scope
```

Examples:

```text
inventory below threshold
participant confirms completion
school term active
treasury balance above threshold
```

Conditions may reference:

* events,
* inventories,
* balances,
* time,
* environmental sources,
* other contracts.

---

# Quotas

Quotas constrain activity.

A quota is only one contract primitive.

```text
Quota
- resource
- limit
- window_type
- window_size
- refill_rate
- overflow_policy
```

Window types:

```text
fixed
rolling
token_bucket
leaky_bucket
lifetime
contract_term
```

Overflow policies:

```text
reject
ignore
allow_without_settlement
queue
partial_settlement
```

Examples:

```text
3 rewards per day
5 requests per week
100 messages per hour
```

---

# Procedures

Procedures define how collective decisions occur.

```text
Procedure
- type
- eligibility_rules
- participation_rules
- decision_rule
- timing
- tie_breaker
```

Examples:

```text
first_past_the_post
approval_voting
ranked_choice
consensus
majority_vote
supermajority_vote
random_selection
```

Contracts should declare procedures explicitly.

Procedural legitimacy depends on:

* transparency,
* advance declaration,
* consistent application,
* reviewability.

---

# Settlement

Settlement describes accounting consequences.

```text
Settlement
- trigger
- effects
- recipients
- timing
```

Possible effects:

```text
grant resource
transfer balance
unlock item
record completion
change reputation
modify world state
activate another contract
```

Timing:

```text
immediate
delayed
scheduled
manual approval
milestone completion
```

---

# Enforcement

Enforcement determines how unmet obligations are handled.

```text
Enforcement
- policy
- escalation
```

Policies:

```text
no_action
reminder
warning
cooldown
suspension
expiration
arbitration
custom
```

Many contracts should default to:

```text
no_action
```

---

# Timeline

Contracts exist within time.

```text
Timeline
- created_at
- starts_at
- activates_at
- expires_at
- review_at
- renews
- recurrence
- grace_period
```

---

# Permissions

Permissions determine who can perform contract operations.

```text
Permission
- actor
- capability
- scope
```

Capabilities:

```text
view
modify
accept
reject
settle
terminate
arbitrate
export
```

---

# Visibility

Contracts may contain sensitive information.

Suggested values:

```text
private
local_client
node_local
household
guild
trusted_participants
public_symbolic
economic_only
```

A contract may expose settlement while keeping underlying records private.

---

# Dispute Procedures

Contracts should support review and appeals.

```text
DisputeProcedure
- appeal_allowed
- appeal_window
- standing_rules
- review_body
- evidence_allowed
- remedy_options
- finality_rule
```

Possible remedies:

```text
uphold
recount
rerun
pause_settlement
amend_future_procedure
void_contract
escalate
```

The purpose is procedural legitimacy rather than punishment.

---

# Audit

Contracts should be auditable.

```text
Audit
- created_by
- accepted_by
- modified_by
- settlement_log
- event_refs
```

Audit logs support:

* accountability,
* debugging,
* migration,
* dispute resolution,
* export.

Audit records should minimize unnecessary sensitive information.

---

# Metadata

Metadata supports extension.

```text
priority
tags
notes
projection_intent
jurisdiction
client_hints
```

---

# Standing Service Contracts

A service contract is a long-lived contract representing an area of collective concern.

Examples:

* vitality,
* learning,
* relationships,
* stewardship,
* governance,
* ecology,
* justice,
* maintenance.

Service contracts function as safety cases.

```text
ServiceContract
- domain
- purpose
- stakeholders
- indicators
- risks
- interventions
- escalation
- governance
- budget
- visibility
- audit
```

---

# Service Safety Case Pattern

```text
Domain
→ indicators
→ risks
→ interventions
→ escalation
→ review
```

Examples:

```text
Care
→ caregiver burden
→ burnout risk
→ respite recommendations
```

```text
Governance
→ unresolved disputes
→ legitimacy risk
→ procedural review
```

```text
Maintenance
→ neglected systems
→ continuity risk
→ repair coordination
```

---

# Mentors and Service Contracts

Mentors are not administrators.

Mentors are humane interpreters of service contracts.

The service contract governs.

The mentor explains.

```text
Service Contract
→ indicators
→ risks
→ interventions
→ mentor interpretation
```

Examples:

Compass:

```text
Governance Service
→ unresolved appeals increasing
→ Orion explains legitimacy concerns
```

Kin:

```text
Belonging Service
→ care burden concentrated
→ Zara encourages conversation and reciprocity
```

Hearthwright:

```text
Maintenance Service
→ neglected repairs accumulating
→ Rowan recommends shared stewardship
```

Mentors make complex systems understandable without exposing users to bureaucracy.

---

# Future Directions

The contract system should eventually support:

* nested contracts,
* dependent contracts,
* templates,
* constitutions,
* standing service contracts,
* guild charters,
* cooperative governance,
* grants and sponsorships,
* recurring subscriptions,
* escrow and sealed rituals,
* marketplace agreements,
* future blockchain settlement adapters,
* symbolic game-world covenants.

The long-term vision is:

```text
contracts
→ coordination
→ settlement
→ cooperation
→ flourishing communities
```

rather than:

```text
contracts
→ extraction
→ coercion
→ optimization pressure
```

Pitchfork contracts should help people coordinate meaningful activity while preserving dignity, consent, local governance, and humane flourishing.
