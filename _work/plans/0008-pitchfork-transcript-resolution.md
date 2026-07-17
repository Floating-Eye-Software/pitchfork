# 0008 Pitchfork Transcript Resolution

## Status

Doing.

## Purpose

Resolve Pitchfork transcript and note evidence into repository-owned ledger,
settlement, projection, and persistence work during emergency recovery.

The first recovery question is:

> What needs cryptographic proof for Pitchfork ledgers?

This plan keeps Pitchfork-specific transcript evidence and follow-up work in
Pitchfork rather than routing it through `fley-org` as durable project memory.

## Authority Boundary

Pitchfork owns:

* shared domain contracts;
* accounting and settlement semantics;
* resource-state transitions;
* projection derivation;
* database-independent persistence interfaces;
* ledger integrity and cryptographic proof requirements for Pitchfork-owned
  records.

Pancakes owns node applications, physical databases, migrations, identity,
permissions, governance, and product behavior.

`fley-org` owns emergency recovery coordination and cross-repository routing.

`fley-qms` owns controlled privacy, health, safety, compliance, regulatory, or
governance review if transcript resolution creates controlled obligations.

## Scope

In scope:

* inventorying Pitchfork transcript and note files that contain durable domain
  concepts;
* identifying ledger, settlement, projection, and persistence requirements
  implied by transcript evidence;
* deciding which Pitchfork records require cryptographic proof, auditability,
  immutability, or tamper evidence;
* routing physical storage, node operations, or governance work to the owning
  repository;
* preserving enough provenance to locate originating notes and references.

Out of scope:

* storing Pitchfork transcript evidence in `fley-org`;
* treating transcripts or reference PDFs as authoritative requirements;
* implementing cryptographic mechanisms directly from transcript text without
  repository review;
* deciding Pancakes database schema or node operations inside Pitchfork;
* bypassing controlled review for privacy, health, safety, compliance, or
  regulatory claims.

## Source Evidence Rule

Transcript and reference files under `_work/notes/` are provenance and recovery
evidence.

They are not authoritative.

Authoritative Pitchfork work must be accepted into durable repository surfaces,
including:

* `_work/plans/*.md`;
* `_work/todo.csv`;
* requirements documents;
* architecture documents;
* source files;
* tests;
* routed governance records.

When a durable work item depends on a retained note or reference, reference the
`_work/notes/` path from the work item and record the reason the evidence is
being retained.

## Work Plan

### 1. Resolve Ledger Cryptographic Proof Evidence

Review and route:

```text
_work/notes/6a407873-9410-83ea-bab5-1448637a801b.html
```

Use this reference while reviewing the transcript:

```text
_work/notes/merkle-tree.pdf
```

Determine what Pitchfork ledgers need cryptographic proof.

At minimum, decide whether proof requirements apply to:

* event identity and append-only event history;
* settlement entries and settlement results;
* resource-state transitions;
* projection derivation inputs and outputs;
* rule versions and processing results;
* idempotency and duplicate-event outcomes;
* cross-node or exported ledger snapshots;
* audit trails needed by Pancakes or future node implementations.

For each candidate proof surface, record one of:

* accepted as a Pitchfork requirement;
* converted into one or more Pitchfork todos;
* routed to Pancakes for physical storage or node behavior;
* routed to `fley-qms` for controlled governance review;
* retained only as provenance;
* intentionally discarded.

### 2. Define The Proof Boundary

Create or update a Pitchfork-owned requirements or architecture document that
states which ledger facts require cryptographic proof and why.

The document should distinguish:

* integrity;
* auditability;
* tamper evidence;
* reproducibility;
* non-repudiation;
* privacy and disclosure constraints;
* local-node storage guarantees versus portable exported proofs.

### 3. Route Mechanisms To Owning Surfaces

Pitchfork should own domain-level proof requirements, deterministic proof
inputs, ledger semantics, and verification contracts.

Pancakes should own physical database storage, node transaction boundaries,
identity, permissions, and deployment-specific proof retention.

Controlled governance review should enter `fley-qms` only when a claim,
process, or obligation requires that authority.

### 4. Convert Accepted Concepts Into Executable Work

For accepted concepts, create or update Pitchfork todos, requirements,
architecture documents, implementation plans, source files, or tests.

Avoid leaving follow-up work inside transcripts or notes.

## Acceptance Criteria

* the initial transcript has explicit disposition;
* `merkle-tree.pdf` has been reviewed as a reference for proof design;
* ledger proof surfaces have been classified;
* accepted proof requirements are captured in Pitchfork-owned durable
  artifacts;
* follow-up work has been converted into Pitchfork todos, plans, documents, or
  routed work items;
* transcript and reference files are treated as provenance only;
* Pancakes-owned physical storage work is routed to Pancakes when needed;
* controlled governance work is routed to `fley-qms` when needed.

## Verification Of Effectiveness

Use this section near closure.

Objectives achieved:

* TBD

Evidence:

* TBD

Residual risks:

* TBD

Follow-on actions:

* TBD

Lessons learned:

* TBD
