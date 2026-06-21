# Pitchfork Core Foundation Risk Register

## Status

Draft

Companion to:

* Pitchfork Core Foundation Requirements
* Pitchfork Core Foundation Design Rationale
* Pitchfork Core Foundation Traceability Matrix
* Pitchfork Core Foundation Design Control Plan

---

# Purpose

This register records risks and opportunities associated with the design, implementation, verification, and maintenance of Pitchfork Core Foundation.

The register supports:

* risk-based thinking,
* architectural decision making,
* requirement derivation,
* verification planning,
* change assessment,
* institutional memory.

This register uses qualitative ISO 9001-style risk assessment.

For each risk:

* Severity is assessed as Low / Medium / High.
* Likelihood is assessed as Low / Medium / High.
* Responses are documented.
* Residual risk is assessed after mitigation.

Residual risk does not imply acceptance.

Residual risks should continue to be monitored and re-evaluated throughout the project.

---

# Risk Categories

## Architectural

Risks arising from core design decisions.

## Implementation

Risks arising from coding or integration activities.

## Verification

Risks arising from inadequate testing or review.

## Project

Risks affecting schedule, scope, or maintainability.

## Opportunity

Potential improvements or strategic advantages.

---

# Risk Register

| ID       | Category      | Risk                                                            | Potential Impact                                                               | Severity | Likelihood | Initial Level | Response                                                                           | Residual Severity | Residual Likelihood | Residual Level | Status |
| -------- | ------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------- | ---------- | ------------- | ---------------------------------------------------------------------------------- | ----------------- | ------------------- | -------------- | ------ |
| PF-R-001 | Architectural | Settlement processing becomes non-deterministic.                | Inconsistent accounting, replay failures, audit failures, difficult debugging. | High     | Medium     | High          | Prohibit hidden inputs and require deterministic processing.                       | High              | Low                 | Medium         | Open   |
| PF-R-002 | Architectural | Settlement reads wall-clock time.                               | Same event may produce different outcomes depending on execution time.         | High     | Medium     | High          | Require time to be explicit input. Prohibit wall-clock reads.                      | High              | Low                 | Medium         | Open   |
| PF-R-003 | Architectural | Settlement generates hidden identifiers.                        | Replay inconsistency and synchronization failures.                             | Medium   | Medium     | Medium        | Require explicit identifiers and idempotency keys.                                 | Medium            | Low                 | Low            | Open   |
| PF-R-004 | Architectural | Events are mutable.                                             | Accounting history becomes unreliable and difficult to audit.                  | High     | Low        | Medium        | Treat events as immutable historical records.                                      | Medium            | Low                 | Low            | Open   |
| PF-R-005 | Architectural | Projections become event side effects.                          | Projection drift, recovery difficulty, replay inconsistencies.                 | High     | Medium     | High          | Derive projections exclusively from resource state.                                | Medium            | Low                 | Low            | Open   |
| PF-R-006 | Architectural | Duplicate event delivery duplicates settlement.                 | Corrupted balances and resource state.                                         | High     | High       | High          | Require idempotent event processing.                                               | High              | Low                 | Medium         | Open   |
| PF-R-007 | Architectural | Partial updates occur during processing.                        | Corrupted accounting state and difficult recovery.                             | High     | Medium     | High          | Require atomic unit-of-work semantics and rollback capability.                     | Medium            | Low                 | Low            | Open   |
| PF-R-008 | Architectural | Accounting semantics become coupled to database implementation. | Reduced portability and maintainability.                                       | Medium   | Medium     | Medium        | Use repository interfaces and persistence abstraction.                             | Low               | Low                 | Low            | Open   |
| PF-R-009 | Architectural | Core engine acquires infrastructure responsibilities.           | Reduced reuse, hidden dependencies, difficult testing.                         | Medium   | Medium     | Medium        | Separate Pitchfork accounting concerns from Pancakes infrastructure concerns.      | Low               | Low                 | Low            | Open   |
| PF-R-010 | Verification  | Deterministic assumptions are not adequately tested.            | Undetected defects in production.                                              | High     | Medium     | High          | Create replay and invariant tests.                                                 | Medium            | Low                 | Low            | Open   |
| PF-R-011 | Verification  | Duplicate processing scenarios are not adequately tested.       | Accounting corruption under retry conditions.                                  | High     | Medium     | High          | Add duplicate-event and retry testing.                                             | Medium            | Low                 | Low            | Open   |
| PF-R-012 | Verification  | Failure and rollback scenarios are not tested.                  | Corruption defects remain undetected.                                          | High     | Medium     | High          | Add failure injection and rollback tests.                                          | Medium            | Low                 | Low            | Open   |
| PF-R-013 | Project       | Architectural rationale is lost over time.                      | Future contributors accidentally violate assumptions.                          | Medium   | High       | High          | Maintain rationale and traceability documentation.                                 | Low               | Medium              | Low            | Open   |
| PF-R-014 | Project       | Scope expands into service or deployment concerns prematurely.  | Increased complexity and delayed delivery.                                     | Medium   | Medium     | Medium        | Keep the first controlled implementation limited to an installable Python library. | Low               | Low                 | Low            | Open   |

---

# Opportunities

| ID       | Opportunity                           | Potential Benefit                                        | Feasibility | Status |
| -------- | ------------------------------------- | -------------------------------------------------------- | ----------- | ------ |
| PF-O-001 | Deterministic replay capability       | Simplified debugging, migration, and auditing.           | High        | Open   |
| PF-O-002 | Database-independent architecture     | Reuse across personal, hosted, and test nodes.           | High        | Open   |
| PF-O-003 | In-memory verification infrastructure | Fast and deterministic testing.                          | High        | Open   |
| PF-O-004 | Explicit repository contracts         | Easier integration with future persistence technologies. | High        | Open   |

---

# Architectural Risk Mapping

Several architectural constraints exist primarily as risk mitigations.

| Decision                  | Primary Risk Mitigated |
| ------------------------- | ---------------------- |
| Deterministic processing  | PF-R-001               |
| No wall-clock reads       | PF-R-002               |
| Explicit identifiers      | PF-R-003               |
| Immutable events          | PF-R-004               |
| State-derived projections | PF-R-005               |
| Idempotent processing     | PF-R-006               |
| Atomic unit of work       | PF-R-007               |
| Repository interfaces     | PF-R-008               |
| Ownership boundaries      | PF-R-009               |

---

# Review Guidance

The register should be reviewed:

* during requirements review,
* during architecture review,
* after major design changes,
* before release,
* whenever a significant defect or incident occurs.

New requirements, architectural decisions, and verification activities should be evaluated for additional risks and opportunities.

Residual risks should be explicitly accepted, monitored, or further mitigated as the project evolves.
