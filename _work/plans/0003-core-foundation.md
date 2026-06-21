# 0003 Pitchfork Core Foundation

## Status

Ready. Dependency `0004-local-testing-framework` is complete.

## Purpose

Replace the current SQLite player/token prototype with an installable,
database-independent Python package that owns the accounting semantics required
by Pancakes nodes and their clients.

This plan is a prerequisite for Pancakes plan `0006-node-ambience-event-plan`.
It does not build or operate a node.

## Design Inputs And Precedence

This execution plan implements the Core Foundation design described by:

* `docs/design/planning/pitchfork-core-foundation-dcp.md`;
* `docs/design/planning/pitchfork-core-foundation-pqp.md`;
* `docs/design/requirements/pitchfork-core-foundation-requirements.md`;
* `docs/design/requirements/pitchfork-core-foundation-design-rationale.md`;
* `docs/design/risks/pitchfork-core-foundation-risk-register.md`;
* `docs/pitchfork-testing.md`.

These documents are currently drafts. Before implementation establishes a
public contract, the applicable requirements, architecture, risks, and review
criteria must be reconciled and their review status recorded. Requirement IDs
in the Core Foundation requirements document are the detailed design inputs;
this plan summarizes their executable scope rather than duplicating them.

If a draft design document conflicts with repository authority boundaries,
approved organization policy, or an applicable controlled QMS procedure, route
the conflict to the owning repository and record the resolution before treating
the document as baselined.

## Ownership Boundary

Pitchfork owns:

* immutable event, result, and accounting domain models and validation,
* deterministic settlement rules,
* resource-state transition semantics,
* projection derivation semantics,
* idempotency requirements,
* documented domain error types,
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

Models must make node scope, actor scope, client namespace, event
identity, timestamps, and schema version explicit where applicable. Numeric
accounting values must use a deterministic representation; binary floating
point is not permitted for settled quantities.

Events are immutable, append-only historical records. Processing results are
immutable after creation. Validation, unknown event, unsupported rule version,
duplicate conflict, and repository consistency failures must use documented
exception or result types.

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

The public API must accept the validated event and an explicit unit-of-work
boundary. Importing the package must not open a database or network connection,
mutate persistent state, or require Pancakes node configuration.

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

The protocol must expose commit and rollback semantics sufficient to ensure
that a processing failure cannot leave a partial event, settlement, resource,
or projection update. The persistence contract must require concurrent
duplicate-event protection; Pitchfork documents that requirement while
Pancakes implements it for physical databases.

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

Before implementing this rule, resolve and record the open design inputs for:

* the deterministic numeric type;
* the canonical `lone_honk.client_ping` event schema;
* the migration resource name, unit, and state change;
* the resource-state rule that derives `red_moon`;
* the public processing API name and result shape;
* duplicate-result semantics;
* supported Python versions;
* the concurrency guarantees required from Pancakes repositories.

These decisions belong in reviewed requirements or architecture artifacts, not
only in source code or tests.

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

Plan 0004 established minimum project metadata for the test adapter. This plan
must complete production packaging without weakening the declared test extra or
the stable commands in `docs/pitchfork-testing.md`.

## Implementation Phases

### Phase 1 — Requirements And Risk Review

Reconcile the draft requirements, rationale, risk register, DCP, and PQP.
Resolve the initial-rule and public-interface questions required for
implementation, define review criteria, and establish the initial
requirements-to-design-to-verification traceability matrix.

Record requirements and risk review outcomes. Repository design documentation
does not become a controlled QMS record merely by being committed; any formal
approval or controlled-use claim must follow the applicable `fley-qms`
procedure.

### Phase 2 — Architecture And Public Contracts

Publish the package architecture, immutable domain model, documented error
model, public event-processing API, repository and unit-of-work protocols,
rule-registration design, concurrency expectations, and import-safety boundary.
Record the architecture review and update traceability and risks.

### Phase 3 — Package And Domain Implementation

Create the package structure, domain models, validation, public API, repository
protocols, and in-memory adapters.

### Phase 4 — Deterministic Engine

Implement versioned rule registration, settlement calculation, resource-state
transitions, projection derivation, and idempotent processing.

### Phase 5 — Verification And Integration Contract

Add unit, contract, property, integration, package, failure-injection, and
rollback tests through the Plan 0004 adapter. Complete requirement and risk
traceability, retain a verification summary, and confirm the callable interface
and persistence contract Pancakes will consume.

### Phase 6 — Validation And Release Readiness

Exercise the intended-use scenario for deterministic processing of the initial
Lone Honk event, assess Pancakes integration readiness, review known
limitations and residual risks, and record validation and release-readiness
outcomes. A package release is not required to close implementation work unless
the reviewed release criteria explicitly require it.

## Verification

Automated tests must cover:

* package build, clean installation, import, and import safety;
* model validation and serialization,
* event and processing-result immutability,
* deterministic replay,
* duplicate-event idempotency,
* settlement balance and cap invariants,
* resource-state transition correctness,
* atomic unit-of-work behavior using the in-memory adapter,
* injected failures and rollback with no partial state retained,
* projections derived from state rather than directly from events,
* projection reconstruction from resource state,
* unknown event and rule-version rejection,
* documented validation, duplicate-conflict, and repository-consistency errors,
* isolation between node, actor, and client scopes,
* absence of database, network, node-configuration, and persistent-state side
  effects in package import and core processing.

Property-based tests should cover settlement invariants where practical.
Tests must use the stable commands in `docs/pitchfork-testing.md`; `make test`
is the authoritative aggregate engineering gate. Verification evidence must map
to requirement IDs and risk mitigations. Routine results remain engineering
feedback unless an applicable approved QMS process identifies and retains them
as controlled evidence.

## Acceptance Criteria

This plan is complete when:

* draft design inputs required by the implementation have recorded review
  outcomes and no unresolved question prevents a deterministic initial rule;
* architecture, public API, repository, unit-of-work, rule-registration, error,
  and concurrency contracts are documented and traced to requirements;
* Pitchfork installs and imports as a Python package;
* the public domain and repository interfaces are documented and stable enough
  for Pancakes to implement;
* the engine processes the initial Lone Honk event deterministically;
* duplicate processing cannot produce duplicate settlement;
* failed processing rolls back without partial in-memory state and the
  concurrent duplicate-protection obligation is explicit for Pancakes;
* projections can be reconstructed from resource state;
* package import and core processing are free of database, network,
  node-configuration, and persistent-state side effects;
* all engine tests use in-memory repositories and no production code opens or
  commits a database transaction;
* the complete `make test` gate, package checks, and clean-environment
  installation pass;
* requirements and material risks trace to reviewed design and verification
  evidence;
* the intended-use validation and Pancakes integration-readiness assessment are
  recorded;
* known limitations and residual risks are recorded for closure review;
* Pancakes can consume the package without importing legacy prototype modules.

## Dependencies

* `0004-local-testing-framework`

Dedicated QMS V&V procedures are not a dependency for ordinary local
engineering tests. If test results are later designated as controlled design
verification evidence, the applicable approved QMS plan or procedure will
define the additional execution and record controls.

The draft design-control documents describe proposed reviews and release
criteria. Their controlled status, named roles, approvals, and records are
governed by the applicable `fley-qms` process when one is adopted; Pitchfork's
repository workflow and ordinary engineering tests must not imply approval on
their own.

## Follow-on Work

After this plan and the Pancakes Node Foundation are complete, Pancakes plan
`0006-node-ambience-event-plan` may implement cross-product event and projection
integration for Lone Honk and Resonance.
