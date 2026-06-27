# 0006 Symbolic Frequency And Crafting Foundation

## Status

Done

## Purpose

Establish Pitchfork's canonical symbolic frequency and symbolic crafting
foundation documents.

This plan covers the Pitchfork-owned foundation for symbolic meaning,
provenance, frequency vectors, symbolic conservation, craft lineage, and
symbolic transformation. It separates those concepts from Pancakes-owned place,
reference service, and node capability foundations.

## Scope

This plan owns:

* `docs/pitchfork-symbolic-frequencies.md`
* `docs/pitchfork-symbolic-crafting.md`

It does not own:

* Pancakes place modeling
* Pancakes reference services
* Pancakes node capability architecture
* RPG lore preservation
* RPG client mechanics
* Pitchfork settlement implementation

Those concerns are tracked in their own plans or repositories.

## Goals

Define symbolic frequencies as the shared semantic vocabulary connecting real
activity, symbolic projections, and commerce/accounting interpretation.

Define symbolic crafting as transformation with memory, where meaningful
history is conserved unless a recipe or operation intentionally transforms it.

Provide stable terminology for later Pitchfork application documents so they
reference these foundations instead of redefining them.

## Deliverables

`docs/pitchfork-symbolic-frequencies.md` should define:

* the Three Worlds projection model
* symbolic frequencies
* orthogonal frequency vectors
* frequency families
* intrinsic and acquired frequencies
* place and provenance boundaries
* capability-originated frequency context
* RPG interpretation boundaries

`docs/pitchfork-symbolic-crafting.md` should define:

* symbolic conservation
* craft lineage
* transformation operations
* symbolic terroir
* activities as ingredients
* recipe semantics
* community crafting
* capability contributions to crafting context

## Acceptance Criteria

The plan is ready for closure review when:

* both Pitchfork foundation documents exist in `docs/`;
* both documents are written as full articles rather than outlines;
* no Pancakes-owned foundation documents are duplicated into Pitchfork;
* application documents can reference the foundation docs without redefining
  symbolic frequencies or symbolic conservation;
* `make check-work` passes;
* `git diff --check` passes.

## Current Review State

The documents have been drafted and the dashboard row is in `review`.

Closure should wait for user review because the work defines canonical
terminology that later documentation will depend on.

## Cross-Repository Relationship

The related Pancakes foundation plan is tracked in the Pancakes repository as
`0009-symbolic-architecture-foundations`.

Pitchfork owns symbolic frequency and symbolic crafting foundations. Pancakes
owns place, reference services, and node capability foundations.
