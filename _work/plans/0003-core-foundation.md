# 0003 Pitchfork Core Foundation

## Status

Ready

## Purpose

Replace the current SQLite player/token prototype with an installable,
database-independent Python package that owns the accounting semantics required
by Pancakes nodes and their clients.

This plan is a prerequisite for Pancakes plan `0006-node-ambience-event-plan`.
It does not build or operate a node.

## Ownership Boundary

Pitchfork owns:

* immutable domain models and validation,
* deterministic settlement rules,
* resource-state transition semantics,
* projection derivation semantics,
* idempotency requirements,
* repository interfaces used by the engine,
* package-level tests and compatibility contracts.

Pitchfork does not own:

* database connections or transactions,
* SQLAlchemy models or Alembic migrations,
* Flask routes or node configuration,
* identity, sessions, permission grants, or deployment.

Pancakes supplies persistence implementations and transaction boundaries. This
keeps the accounting engine usable with both PostgreSQL hosted nodes and SQLite
personal or test nodes.

## Required Domain Model

Define typed, serializable models for:

* client events,
* settlement entries and settlement results,
* resource keys, balances, and state changes,
* projection requests and derived projections,
* rule identifiers and rule versions,
* idempotency keys and processing outcomes.

Models must make tenant or node scope, actor scope, client namespace, event
identity, timestamps, and schema version explicit where applicable. Numeric
accounting values must use a deterministic representation; binary floating
point is not permitted for settled quantities.

## Engine Contract

Implement a deterministic application service with an explicit unit-of-work
boundary:

```text
validated event
→ select versioned settlement rule
→ calculate settlement entries
→ apply resource-state transitions
→ derive projections from resulting state
→ return an immutable processing result
```

The same inputs, rule versions, and prior resource state must produce the same
result. The engine must not read wall-clock time, generate identifiers, open a
database, or commit a transaction implicitly.

Events affect resource state. Projections are derived from resource state and
must not be attached directly as event side effects.

## Persistence Interfaces

Define repository protocols for the minimum state required by the engine:

* event existence and recording,
* settlement recording,
* resource-state reads and writes,
* projection reads and writes,
* rule-version lookup where rules are not compiled into the package.

Define a unit-of-work protocol that lets the Pancakes node make event storage,
settlement, resource updates, and projection updates one atomic transaction.
Interfaces must describe concurrency and duplicate-event expectations without
assuming SQLAlchemy or a particular database.

Provide in-memory implementations for engine tests. Database-backed
implementations belong to Pancakes.

## Initial Rules

Implement only the bounded rules required to prove the first integration:

* accept a namespaced `lone_honk.client_ping` event,
* settle its documented migration resource change,
* derive the `red_moon` projection from resulting resource state,
* return the existing result when the same event identity is processed again.

Rule registration must support later Lone Honk and Resonance event types without
hard-coding client routing into the engine.

## Packaging

Create a standard `src`-layout Python package with:

* `pyproject.toml`,
* an importable `pitchfork` package,
* declared supported Python versions,
* development and test dependencies,
* a documented public API,
* migration notes for the legacy prototype.

The existing `src/pitchfork.py` prototype must not remain the package entry
point. Preserve it as legacy code until its useful behavior is covered or an
explicit removal decision is recorded.

## Implementation Phases

### Phase 1 — Package and Contracts

Create the package structure, domain models, validation, public API, repository
protocols, and in-memory adapters.

### Phase 2 — Deterministic Engine

Implement versioned rule registration, settlement calculation, resource-state
transitions, projection derivation, and idempotent processing.

### Phase 3 — Verification and Integration Contract

Add unit and contract tests, document transaction and concurrency expectations,
and publish the callable interface Pancakes will consume.

## Verification

Automated tests must cover:

* model validation and serialization,
* deterministic replay,
* duplicate-event idempotency,
* settlement balance and cap invariants,
* atomic unit-of-work behavior using the in-memory adapter,
* projections derived from state rather than directly from events,
* unknown event and rule-version rejection,
* isolation between node, actor, and client scopes,
* package build and installation in a clean environment.

Property-based tests should cover settlement invariants where practical.

## Acceptance Criteria

This plan is complete when:

* Pitchfork installs and imports as a Python package;
* the public domain and repository interfaces are documented and stable enough
  for Pancakes to implement;
* the engine processes the initial Lone Honk event deterministically;
* duplicate processing cannot produce duplicate settlement;
* all engine tests use in-memory repositories and no production code opens a
  database directly;
* package, unit, and contract tests pass;
* Pancakes can consume the package without importing legacy prototype modules.

## Dependencies

None.

## Follow-on Work

After this plan and the Pancakes Node Foundation are complete, Pancakes plan
`0006-node-ambience-event-plan` may implement cross-product event and projection
integration for Lone Honk and Resonance.
