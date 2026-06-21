# Pitchfork Core Foundation Design Rationale

## Status

Draft

Companion to:

* Pitchfork Core Foundation Requirements
* Pitchfork Core Foundation Risk Register
* Pitchfork Core Foundation Traceability Matrix
* Pitchfork System Overview

---

# Purpose

This document records the rationale behind major architectural decisions in Pitchfork Core Foundation.

Its purpose is to answer questions such as:

* Why was this decision made?
* What problem does it solve?
* What risks does it mitigate?
* What requirements does it produce?
* How should it be verified?

This document exists to preserve institutional memory.

Future contributors should not need to reverse-engineer the motivations behind core architectural constraints.

---

# Design Rationale Structure

Each rationale records:

```text
Decision
Motivation Type
Problem
Risks or Quality Concerns
Chosen Solution
Alternatives Considered
Consequences
Derived Requirements
Derived Verification Activities
```

---

# Motivation Categories

Architectural decisions generally arise from one or more of the following sources.

## Hazard Prevention

The decision reduces the likelihood or impact of undesirable outcomes.

Examples:

* duplicate settlement,
* non-deterministic processing,
* state corruption.

---

## Quality Attributes

The decision improves important system properties.

Examples:

* portability,
* maintainability,
* testability,
* extensibility.

---

## Intended Use

The decision follows directly from the product definition.

Examples:

* Python library,
* accounting engine,
* reusable package.

---

## Architectural Principles

The decision reflects foundational design values.

Examples:

```text
same inputs
→ same outputs
```

```text
events
→ state
→ projections
```

```text
explicit inputs
→ explicit outcomes
```

---

# Rationale 1 — Deterministic Processing

## Decision

The same validated event, rule version, and prior resource state shall always produce the same result.

## Motivation Type

* Hazard Prevention
* Architectural Principle

## Problem

Accounting systems become difficult to trust if outcomes vary.

## Risks

* replay inconsistency,
* irreproducible defects,
* audit failures,
* node disagreement,
* difficult debugging.

## Chosen Solution

Require deterministic processing.

```text
same event
+
same rule version
+
same prior state
=
same outcome
```

## Alternatives Considered

Allow environmental factors to influence settlement.

Rejected because settlement semantics would become unpredictable.

## Consequences

All settlement inputs must be explicit.

Hidden dependencies are prohibited.

## Derived Requirements

* deterministic engine requirements,
* explicit input requirements.

## Derived Verification

* deterministic replay tests,
* repeated execution tests.

---

# Rationale 2 — No Wall-Clock Reads

## Decision

Settlement processing shall not read wall-clock time.

## Motivation Type

* Hazard Prevention

## Problem

Time is hidden input.

The same event processed at different times may produce different results.

## Risks

* non-deterministic settlement,
* replay failures,
* audit inconsistencies.

## Chosen Solution

All time values affecting settlement must be explicit event inputs.

## Alternatives Considered

Allow direct access to current time.

Rejected because settlement outcomes would depend on execution environment.

## Consequences

Settlement behavior becomes reproducible.

## Derived Requirements

* no wall-clock reads during settlement.

## Derived Verification

* replay events at different times,
* verify identical results.

---

# Rationale 3 — No Settlement-Critical Identifier Generation

## Decision

Settlement processing shall not generate settlement-critical identifiers.

## Motivation Type

* Hazard Prevention
* Architectural Principle

## Problem

Generated identifiers introduce hidden state.

## Risks

* replay inconsistencies,
* difficult debugging,
* synchronization failures.

## Chosen Solution

Require identifiers to be explicit inputs.

## Alternatives Considered

Allow settlement to generate identifiers.

Rejected because replay may produce different identifiers.

## Consequences

Processing becomes reproducible.

## Derived Requirements

* caller-supplied identities,
* explicit idempotency keys.

## Derived Verification

* replay tests,
* duplicate-event tests.

---

# Rationale 4 — Immutable Events

## Decision

Events are immutable historical records.

## Motivation Type

* Hazard Prevention

## Problem

Mutable events make history difficult to trust.

## Risks

* audit failures,
* inconsistent accounting,
* replay corruption.

## Chosen Solution

Treat events as append-only historical records.

## Alternatives Considered

Mutable event records.

Rejected because accounting history becomes unreliable.

## Consequences

Historical replay becomes possible.

## Derived Requirements

* immutable event models,
* append-only event recording.

## Derived Verification

* replay tests,
* audit tests.

---

# Rationale 5 — Events Affect State; State Produces Projections

## Decision

Projections are derived from resource state rather than attached directly as event side effects.

## Motivation Type

* Hazard Prevention
* Architectural Principle

## Problem

Event side effects are difficult to reproduce and recover.

## Risks

* projection drift,
* replay inconsistencies,
* recovery complexity.

## Chosen Solution

Use:

```text
events
→ resource state
→ projections
```

## Alternatives Considered

Direct event-to-projection updates.

Rejected because projections become difficult to reconstruct.

## Consequences

Projections become views of current state.

Replay naturally recreates projections.

## Derived Requirements

* projection derivation requirements,
* state transition requirements.

## Derived Verification

* replay tests,
* projection reconstruction tests.

---

# Rationale 6 — Idempotent Processing

## Decision

Duplicate processing of the same event identity shall not duplicate settlement.

## Motivation Type

* Hazard Prevention

## Problem

Distributed systems retry operations.

Duplicate delivery is normal.

## Risks

```text
event
→ settle
→ retry
→ settle again
```

Result:

* duplicate balances,
* corrupted accounting,
* incorrect projections.

## Chosen Solution

Require idempotent processing.

```text
same event identity
→ same outcome
```

## Alternatives Considered

Assume event delivery occurs exactly once.

Rejected because distributed systems cannot reliably make this guarantee.

## Consequences

Duplicate delivery becomes safe.

## Derived Requirements

* idempotency requirements,
* duplicate-event detection.

## Derived Verification

* duplicate processing tests,
* concurrent retry tests.

---

# Rationale 7 — Atomic Unit of Work

## Decision

Event recording, settlement recording, state updates, and projection updates shall succeed or fail together.

## Motivation Type

* Hazard Prevention

## Problem

Partial updates create inconsistent state.

## Risks

```text
event stored
settlement stored
resource update failed
projection missing
```

Result:

* corruption,
* difficult recovery,
* inconsistent views.

## Chosen Solution

Require atomic unit-of-work semantics.

## Alternatives Considered

Independent writes.

Rejected because failures produce inconsistent state.

## Consequences

Failures remain recoverable.

## Derived Requirements

* atomic transaction requirements,
* rollback requirements.

## Derived Verification

* failure injection tests,
* rollback tests.

---

# Rationale 8 — Database Independence

## Decision

Pitchfork Core Foundation shall not depend on a particular database technology.

## Motivation Type

* Quality Attribute
* Intended Use

## Problem

Persistence technologies change.

Settlement semantics should not.

## Risks

* infrastructure coupling,
* migration difficulty,
* limited portability.

## Chosen Solution

Depend on repository interfaces rather than database implementations.

## Alternatives Considered

Embed database technology directly in the engine.

Rejected because it reduces portability and testability.

## Consequences

Pitchfork remains reusable across different node implementations.

## Derived Requirements

* repository protocols,
* persistence abstraction requirements.

## Derived Verification

* in-memory tests,
* multiple repository implementations.

---

# Rationale 9 — No Production Database Ownership

## Decision

Pitchfork Core Foundation shall not open databases or commit production transactions.

## Motivation Type

* Quality Attribute
* Intended Use

## Problem

The engine would become responsible for infrastructure concerns.

## Risks

* hidden dependencies,
* reduced reuse,
* complicated testing,
* unclear responsibilities.

## Chosen Solution

Separate responsibilities.

```text
Pitchfork
→ accounting semantics

Pancakes
→ persistence
→ deployment
→ transactions
```

## Alternatives Considered

Monolithic service implementation.

Rejected because infrastructure concerns would contaminate accounting logic.

## Consequences

Clear ownership boundaries.

## Derived Requirements

* no database access requirements,
* explicit unit-of-work requirements.

## Derived Verification

* import safety tests,
* in-memory repository tests.

---

# Rationale 10 — Python Library First

## Decision

The first controlled implementation is an installable Python package.

## Motivation Type

* Intended Use

## Problem

The project requires an accounting engine, not a server.

## Risks

Premature service development may:

* introduce unnecessary complexity,
* entangle deployment concerns,
* obscure accounting semantics.

## Chosen Solution

Build the deterministic engine first.

Future services may wrap the library.

## Alternatives Considered

Implement a REST service immediately.

Rejected because it mixes infrastructure concerns with core semantics.

## Consequences

The accounting engine remains independently testable and reusable.

## Derived Requirements

* installable package requirements,
* public Python API requirements.

## Derived Verification

* package installation tests,
* import tests,
* API tests.

---

# Architectural Axioms

The following principles should be treated as foundational assumptions of Pitchfork Core Foundation.

```text
same inputs
→ same outputs
```

```text
events
→ state
→ projections
```

```text
explicit inputs
→ explicit outcomes
```

```text
history is immutable
```

```text
accounting semantics
≠
infrastructure concerns
```

These axioms guide future design decisions.

Any proposed change should explain:

* which axiom it preserves,
* which risks it introduces,
* and why the benefits justify the change.

---

# Long-Term Goal

Pitchfork Core Foundation should behave more like mathematics than infrastructure.

Given:

```text
event
+
rule version
+
prior state
```

the engine computes:

```text
settlement
+
new state
+
projections
```

Nothing hidden should influence the result.

Not:

* clocks,
* databases,
* deployment choices,
* network conditions,
* generated identifiers,
* application frameworks.

The result is a foundation that is:

* deterministic,
* replayable,
* testable,
* portable,
* auditable,
* and trustworthy.
