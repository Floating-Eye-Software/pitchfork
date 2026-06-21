# Pitchfork Core Foundation Requirements

## Status

Draft Design Input

## Controlled Item

Pitchfork Core Foundation

## Product Definition

Pitchfork Core Foundation is an installable Python library that provides deterministic accounting semantics for Pancakes nodes and Pancakes/Pitchfork clients.

It is not, in this phase:

* a standalone server,
* a REST API,
* a database schema,
* a Flask application,
* a node implementation,
* an identity system,
* a permission-management system,
* or a deployment target.

A future Pitchfork service or REST API may wrap this library, but that is a separate controlled item.

---

# Purpose

The purpose of Pitchfork Core Foundation is to process validated client events into deterministic accounting outcomes.

The core processing flow is:

```text
validated event
→ settlement rule
→ settlement entries
→ resource-state transition
→ derived projection
→ immutable processing result
```

---

# Scope

## In Scope

Pitchfork Core Foundation shall provide:

* typed domain models,
* event validation semantics,
* deterministic settlement processing,
* resource-state transition semantics,
* projection derivation semantics,
* idempotency handling,
* repository protocols,
* unit-of-work protocol,
* in-memory test repositories,
* package-level tests,
* documented public Python API.

## Out of Scope

Pitchfork Core Foundation shall not provide:

* production database connections,
* SQLAlchemy models,
* Alembic migrations,
* Flask routes,
* REST endpoints,
* authentication,
* user sessions,
* permission grant issuance,
* node administration,
* deployment configuration.

---

# System Boundary

Pancakes supplies:

* identity,
* permissions,
* persistence implementation,
* database transactions,
* deployment,
* node configuration,
* API routes,
* user interface.

Pitchfork supplies:

* accounting models,
* deterministic rules,
* settlement logic,
* resource transition logic,
* projection derivation logic,
* repository contracts.

---

# Functional Requirements

## PF-CF-FR-001 — Installable Python Package

Pitchfork Core Foundation shall be packaged as an installable Python package.

## PF-CF-FR-002 — Public Python API

Pitchfork Core Foundation shall expose a documented public Python API for processing validated events.

## PF-CF-FR-003 — Typed Domain Models

Pitchfork Core Foundation shall define typed, serializable models for:

* client events,
* settlement entries,
* settlement results,
* resource keys,
* resource balances,
* resource state changes,
* projection requests,
* derived projections,
* rule identifiers,
* rule versions,
* idempotency keys,
* processing outcomes.

## PF-CF-FR-004 — Explicit Scope Fields

Domain models shall make the following explicit where applicable:

* node scope,
* actor scope,
* client namespace,
* event identity,
* timestamp,
* schema version.

## PF-CF-FR-005 — Deterministic Numeric Representation

Settled accounting quantities shall use deterministic numeric representation.

Binary floating point shall not be used for settled quantities.

## PF-CF-FR-006 — Event Processing

Pitchfork Core Foundation shall process a validated event by:

1. selecting a versioned settlement rule,
2. calculating settlement entries,
3. applying resource-state transitions,
4. deriving projections from resulting resource state,
5. returning an immutable processing result.

## PF-CF-FR-007 — Rule Versioning

Settlement rules shall be identified by rule id and rule version.

## PF-CF-FR-008 — Idempotent Processing

Processing the same event identity more than once shall not produce duplicate settlement.

The engine shall return the existing processing outcome or equivalent idempotent result.

## PF-CF-FR-009 — Resource-State Transitions

Events shall affect resource state through explicit settlement entries and state changes.

## PF-CF-FR-010 — Projection Derivation

Projections shall be derived from resource state.

Projections shall not be attached directly as event side effects.

## PF-CF-FR-011 — Repository Protocols

Pitchfork Core Foundation shall define repository protocols for:

* event existence checks,
* event recording,
* settlement recording,
* resource-state reads,
* resource-state writes,
* projection reads,
* projection writes,
* rule-version lookup where applicable.

## PF-CF-FR-012 — Unit of Work Protocol

Pitchfork Core Foundation shall define a unit-of-work protocol that allows a Pancakes node to commit or roll back event storage, settlement records, resource updates, and projection updates as one atomic transaction.

## PF-CF-FR-013 — In-Memory Implementations

Pitchfork Core Foundation shall provide in-memory repository and unit-of-work implementations for tests.

## PF-CF-FR-014 — Initial Lone Honk Rule

Pitchfork Core Foundation shall process the namespaced event type:

```text
lone_honk.client_ping
```

## PF-CF-FR-015 — Initial Migration Resource Change

Pitchfork Core Foundation shall settle the documented migration resource change for the initial Lone Honk event.

## PF-CF-FR-016 — Red Moon Projection

Pitchfork Core Foundation shall derive the `red_moon` projection from resulting resource state.

## PF-CF-FR-017 — Unknown Event Rejection

Pitchfork Core Foundation shall reject unknown event types or unsupported rule versions with explicit errors.

---

# Non-Functional Requirements

## PF-CF-NFR-001 — Determinism

Given the same validated event, rule version, and prior resource state, Pitchfork Core Foundation shall produce the same processing result.

## PF-CF-NFR-002 — No Wall-Clock Reads

Pitchfork Core Foundation shall not read wall-clock time during settlement processing.

All time values affecting settlement shall be explicit inputs.

## PF-CF-NFR-003 — No Identifier Generation During Processing

Pitchfork Core Foundation shall not generate settlement-critical identifiers during processing.

Event identities and idempotency keys shall be supplied by the caller.

## PF-CF-NFR-004 — No Production Database Access

Pitchfork Core Foundation production code shall not open database connections.

## PF-CF-NFR-005 — No Implicit Transaction Commit

Pitchfork Core Foundation shall not implicitly commit production transactions.

Transaction control belongs to the Pancakes node unit-of-work implementation.

## PF-CF-NFR-006 — Database Independence

Pitchfork Core Foundation shall not depend on PostgreSQL, SQLite, SQLAlchemy, Alembic, or any specific persistence technology.

## PF-CF-NFR-007 — Testability

Pitchfork Core Foundation shall be testable using in-memory repositories without requiring a production database.

## PF-CF-NFR-008 — Package Import Safety

Importing the `pitchfork` package shall not open network connections, open databases, mutate persistent state, or require node configuration.

---

# Interface Requirements

## PF-CF-IR-001 — Event Processing Interface

Pitchfork Core Foundation shall expose a callable event-processing interface equivalent to:

```python
result = pitchfork.process_event(event, unit_of_work)
```

The exact function name may differ, but the interface shall accept an event and an explicit unit-of-work boundary.

## PF-CF-IR-002 — Immutable Result

The processing result shall be immutable after creation.

## PF-CF-IR-003 — Error Interface

Validation, unknown event, unsupported rule version, duplicate conflict, and repository consistency errors shall be represented by documented exception or result types.

---

# Atomicity Requirements

## PF-CF-AR-001 — Atomic Processing Boundary

Event recording, settlement recording, resource-state updates, and projection updates shall succeed or fail as a single atomic operation when used with a compliant unit-of-work implementation.

## PF-CF-AR-002 — Rollback on Failure

If processing fails before completion, no partial settlement result shall be committed by the unit-of-work implementation.

## PF-CF-AR-003 — Duplicate Event Protection

A compliant persistence implementation shall prevent duplicate settlement for the same event identity under concurrent processing.

## PF-CF-AR-004 — Concurrency Contract

Pitchfork Core Foundation shall document the concurrency expectations required of database-backed Pancakes implementations.

---

# Design Constraints

## PF-CF-DC-001 — Python Library First

The first controlled implementation shall be a Python library.

A REST API is a future wrapper, not part of this controlled item.

## PF-CF-DC-002 — Node Owns REST

If a REST API is later implemented, it shall belong to a Pancakes node or Pitchfork service wrapper, not to the core foundation library.

## PF-CF-DC-003 — Pancakes Owns Production Persistence

Production database-backed repositories shall be implemented by Pancakes or a node service layer.

## PF-CF-DC-004 — No Legacy Entry Point

The legacy `src/pitchfork.py` prototype shall not remain the package entry point.

---

# Verification Requirements

Automated tests shall verify:

* package installation,
* package import,
* model validation,
* serialization and deserialization,
* deterministic replay,
* duplicate-event idempotency,
* settlement invariants,
* resource-state transition correctness,
* projection derivation from state,
* unknown event rejection,
* unsupported rule-version rejection,
* node isolation,
* actor isolation,
* client namespace isolation,
* atomic unit-of-work behavior using in-memory adapters,
* no production database access from core library code.

Property-based tests should verify settlement invariants where practical.

---

# Acceptance Criteria

Pitchfork Core Foundation is acceptable when:

* it installs as a Python package;
* it imports as `pitchfork`;
* it exposes documented public Python interfaces;
* it processes `lone_honk.client_ping`;
* it settles the required migration resource change;
* it derives the `red_moon` projection from state;
* duplicate event processing cannot duplicate settlement;
* in-memory tests pass;
* package build tests pass;
* no production code opens a database connection;
* no production code commits a transaction implicitly;
* Pancakes can implement database-backed repositories without importing legacy prototype modules.

---

# Open Questions

1. What exact deterministic numeric type should be used for settled quantities?
2. What is the canonical shape of `lone_honk.client_ping`?
3. What is the exact migration resource name and unit?
4. What resource-state threshold derives `red_moon`?
5. Should the public API be named `process_event`, `record_event`, or something else?
6. Should idempotent duplicate processing return the original result object or a new result marked as duplicate?
7. Which package versions of Python are supported?
8. What concurrency guarantees must Pancakes database implementations provide?
