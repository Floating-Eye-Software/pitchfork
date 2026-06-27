# 0002 Pitchfork RPG Client Specification Update

## Status

Ready

## Purpose

Define the canonical, node-aware architecture of the Pitchfork RPG as a
symbolic client of the Pancakes and Pitchfork ecosystem.

This plan owns the technical boundary that the reader-oriented RPG documents
in plan `0005-rpg-lore-preservation` will explain. It does not own the RPG
directory's narrative, pedagogy, worldbuilding, or editorial organization.

## Architectural Position

The RPG is one client and projection of the wider ecosystem:

```text
life activity
→ Pancakes client and node
→ Pitchfork event and settlement
→ projection
→ RPG interpretation
```

Pitchfork owns shared domain contracts, settlement semantics, resource-state
transitions, projection derivation, and database-independent persistence
interfaces. Pancakes owns applications, physical databases, identity,
permissions, governance, and product behavior.

The RPG must not become the source of truth for life activity, identity,
settlement, or physical persistence.

## Scope

This plan will:

* audit the current RPG architecture and design sources;
* identify preserved concepts and obsolete assumptions;
* specify the RPG's relationship to Pancakes, Pitchfork, and nodes;
* define event, settlement, resource, inventory, and projection boundaries;
* define the architectural roles of sanctuaries, attunements, mentors,
  archetypes, gathering, crafting, rituals, Nexus, and ambient worlds;
* define privacy and sensitive-domain boundaries, including any Red Witch
  integration;
* define the staged path from solo play to household, guild, institutional,
  and broader multiplayer play;
* provide stable references for the gameplay, economic-testbed, research, and
  roadmap documents tracked by plan `0005`.

## Source Material

At minimum, review:

* the existing files under `docs/rpg/`;
* `docs/pitchfork-symbolic-frequencies.md`;
* `docs/pitchfork-symbolic-crafting.md`;
* current Pitchfork API and architecture documents;
* relevant Pancakes architecture by reference, without copying Pancakes-owned
  contracts into this repository.

## Deliverables

* A canonical RPG client architecture document under `docs/rpg/`.
* A source disposition mapping that records which legacy RPG concepts are
  preserved, modernized, superseded, or left open.
* Explicit architecture references suitable for the documents in plan `0005`.

The final filename may be retained or changed during the `docs/rpg`
reorganization, but there must be exactly one clearly identified canonical RPG
architecture source.

## Work Sequence

1. Inventory and classify existing RPG source material.
2. Reconcile the architecture with current Pitchfork domain contracts and the
   symbolic frequency and crafting foundations.
3. Specify ecosystem, node, projection, privacy, and ownership boundaries.
4. Specify the architecture of RPG gameplay and social systems without
   prematurely deciding open game-design questions.
5. Cross-reference authoritative documents and publish the source disposition
   mapping.

## Acceptance Criteria

The plan is ready for closure review when:

* one document is clearly designated as the canonical RPG client architecture;
* direct habit-tracking ownership, app-centric assumptions, centralized
  assumptions, and pre-node identity assumptions are removed or explicitly
  marked historical;
* the event-to-settlement-to-projection flow is explicit;
* ownership boundaries among the RPG, Pitchfork, and Pancakes are explicit;
* node types, privacy boundaries, and the multiplayer progression are covered;
* preserved and superseded legacy sources are traceable through a disposition
  mapping;
* the architecture supports, but does not duplicate, the eleven documents
  defined by plan `0005`;
* repository links resolve;
* `make check-work` passes;
* `git diff --check` passes.

## Out of Scope

This plan does not:

* implement the game or Pancakes applications;
* define physical database schemas or migrations;
* make unresolved product decisions such as combat, PvP, blockchain use, or
  procedural generation;
* replace canonical Pitchfork foundation documents with RPG terminology;
* create a single canonical player story.

## Verification of Effectiveness

At closure review, confirm that a contributor can use the architecture document
to determine where RPG state comes from, which repository owns each boundary,
and which questions remain product decisions. Record residual ambiguities as
follow-up tasks rather than resolving them implicitly in editorial prose.
