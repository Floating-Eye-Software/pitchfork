# 0005 RPG Documentation Reorganization And Lore Preservation

## Status

Todo

## Purpose

Reorganize `docs/rpg/` by architectural responsibility while preserving and
modernizing the RPG's narrative, mechanics, pedagogy, economic experiments,
research model, and product direction.

This plan operationalizes `_work/pitchfork-rpg-plan.md`. The proposal is source
material; this plan and the workflow dashboards are the authoritative execution
record.

## Dependencies

* `0002-pitchfork-rpg-client-spec-update` must establish the canonical RPG
  client boundary and source disposition mapping.
* `0006-symbolic-frequency-and-crafting-foundation` must complete review so the
  RPG documents can reference stable symbolic terminology.

Drafting and source analysis may begin before those plans close, but dependent
documents must not be finalized against unsettled canonical terminology.

## Design Principle

The directory will be organized by document responsibility rather than legacy
brainstorming categories such as story, inventory, stats, or rules.

The Pitchfork RPG is simultaneously a game, a pedagogical experience, an
economic sandbox, a research platform, and a client for the Pancakes ecosystem.

There will be no canonical `story.md`. The novice's journey is a curriculum,
the world is persistent, and each player creates a story within it.

## Target Structure

```text
docs/rpg/
README.md
01-rpg-overview.md
02-design-goals.md
03-novices-journey.md
04-magic-system.md
05-commerce-and-contracts.md
06-world-and-setting.md
07-gameplay.md
08-economic-testbed.md
09-research-platform.md
10-product-roadmap.md
11-open-questions.md
```

The canonical architecture document from plan `0002` may remain alongside this
reader-oriented set when it serves a distinct technical purpose. `README.md`
must identify it as authoritative for technical boundaries.

## Document Responsibilities

### README.md

Orient readers, identify the recommended reading order, distinguish canonical
from archived material, and explain the RPG's relationship to Pitchfork and
Pancakes.

### 01-rpg-overview.md

Define the RPG as a browser RPG, symbolic economy, pedagogical experience,
Pancakes client, economic sandbox, research platform, eventual MMO, and
potential foundation for future clients.

### 02-design-goals.md

Explain the design intent: symbolic thinking, stewardship, safe institutional
experimentation, contributor development, recognition of invisible and
household labor, and commonwealth mechanics.

### 03-novices-journey.md

Define the Academy curriculum and conceptual progression. Each stage should
introduce one primary abstraction. Preserve the intellectual sequence:

```text
Colored Tokens
→ Blanken
→ Gray Tokens and Released Value
→ Contracts
→ Commodities
→ Ether and Convergence
→ Executable Agreements
→ Governance and Restored Balance
```

The journey should connect magical discovery to stewardship, institutions, the
Commerce Realm, and Walden Three without becoming the player's canonical story.

### 04-magic-system.md

Define magical mechanics: mentors, colors, attunements, resonance, frequencies,
tokens, rarity, Blanken, create/fill/empty operations, alchemy, spellcraft, and
rituals. Reference canonical symbolic-frequency and crafting documents rather
than redefining them.

### 05-commerce-and-contracts.md

Define institutional magic: contracts, covenants, guilds, escrow, reputation,
governance, institutions, ledgers, markets, and treasuries. Clearly separate
game interpretation from canonical settlement and accounting semantics.

### 06-world-and-setting.md

Describe the Academy, mentors, magical civilization, Commerce Realm, geography,
factions, Walden Three, locations, atmosphere, and history.

### 07-gameplay.md

Describe browser interaction, gathering, crafting, sanctuaries, exploration,
quests, progression, inventory, recipes, multiplayer, and clients. Keep
philosophy and canonical architecture in their responsible documents.

### 08-economic-testbed.md

Explain how the RPG can safely test symbolic currencies, institutions,
governance, incentives, contracts, recipes, and resource flows before applying
lessons outside the game. State initial real-money and safety boundaries
explicitly.

### 09-research-platform.md

Explain how players and collaborators propose, test, evaluate, and govern new
schools, rituals, recipes, institutions, and other experiments. Cover
playtesting, academic collaboration, evidence, and open experimentation.

### 10-product-roadmap.md

Provide an implementation-focused progression from an initial browser
experience through cooperative play, economic systems, MMO capabilities,
carefully governed real-economy possibilities, and future clients. Separate
committed scope from hypotheses.

### 11-open-questions.md

Record unresolved decisions, their constraints, and the evidence needed to
decide them. Seed it with color and commodity semantics, AI mentors,
multiplayer governance, reputation, PvP, combat, procedural worlds,
blockchain, and economic settlement.

## Migration Rules

1. Inventory every existing file under `docs/rpg/` and map its useful material
   to a target document, canonical architecture source, archive, or explicit
   supersession.
2. Reorganize before performing broad rewrites so provenance remains visible.
3. Preserve distinctive mechanics, terminology, mentor traditions, discovery
   order, and emotional progression unless a documented conflict requires a
   change.
4. Modernize technology assumptions and evolve the historical blockchain
   conclusion toward privacy-respecting, community-governed civic
   infrastructure.
5. Do not make architecture depend on lore or make lore redefine architecture.
6. Do not silently discard contradictory or undecided concepts; record them in
   `11-open-questions.md`.
7. Preserve useful Git history where practical and ensure superseded entry
   points direct readers to the new structure.

## Work Sequence

1. Build a complete source inventory and migration matrix.
2. Establish the target directory, README, terminology, cross-reference, and
   archival conventions.
3. Draft the overview, goals, and novice's journey.
4. Draft the magic, commerce, world, and gameplay documents.
5. Draft the economic testbed, research platform, roadmap, and open questions.
6. Reconcile all documents with plans `0002` and `0006`.
7. Remove or archive superseded reader-facing files only after their useful
   content is accounted for.
8. Perform editorial, link, workflow, and acceptance review.

## Acceptance Criteria

The plan is ready for closure review when:

* all twelve target reader-oriented files exist as substantive documents;
* `03-novices-journey.md` provides a coherent one-abstraction-at-a-time
  curriculum and preserves the discovery sequence;
* every preexisting `docs/rpg` file has a recorded migration disposition;
* no canonical `story.md` remains in the active reader path;
* architecture, narrative, mechanics, pedagogy, economics, research, roadmap,
  and open questions have clear non-overlapping homes;
* the documents correctly route Pitchfork-, Pancakes-, site-ops-, fley-org-,
  and fley-qms-owned concerns;
* economic experimentation is presented as a safe testbed and does not imply
  unreviewed real-money deployment;
* unresolved decisions remain visibly open rather than becoming accidental
  commitments;
* terminology and links are consistent with plans `0002` and `0006`;
* repository links resolve;
* `make check-work` passes;
* `git diff --check` passes.

## Out of Scope

This plan does not implement game services, databases, identity, deployment,
live economic settlement, controlled research procedures, or regulatory
review. Work in those areas must be routed to the authoritative repository.

## Verification of Effectiveness

At closure review, ask readers unfamiliar with the project to identify:

* what the RPG is and why it exists;
* how a novice learns its symbolic language;
* which material is game design versus canonical architecture;
* how economic and research experiments are constrained;
* where unresolved decisions are recorded.

Record navigation failures, responsibility ambiguity, lost legacy concepts,
and unsafe economic implications as residual work before closure.
