# 0007 RPG Documentation Consolidation

## Workflow Status

Blocked

## Dependency

This plan depends on `0005-rpg-lore-preservation`. Consolidation and deletion
of legacy sources should occur only after the replacement documentation has
been reconciled and accepted.

## Purpose

This document records the remaining ideas from the original 2023–2026 RPG design documents before the legacy `docs/rpg` directory is retired.

The new documentation reorganizes the RPG around its current architectural purpose rather than the chronology of its development. Most concepts from the older documents have already been incorporated into the new framework.

This document identifies the remaining ideas worth preserving before the legacy files are deleted.

---

# Status

The following replacement documents now form the canonical RPG documentation.

```
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

These documents replace the previous brainstorming archive.

---

# Concepts Successfully Preserved

The following concepts from the legacy documents have been incorporated into the new documentation.

## Educational progression

Originally spread across:

* story.md
* lore.md
* phases.md
* design.md
* design2.md

Now consolidated into:

* 03-novices-journey.md

Including:

* Academy
* mentors
* novice discoveries
* Blanken
* contact with the Commerce World
* convergence
* stewardship
* Walden Three

---

## Symbolic magic

Originally spread across:

* magic-token.md
* pitchfork_magic_system.md
* pitchfork_magic_system_with_contracts.md

Now consolidated into:

* 04-magic-system.md

Including:

* color magic
* tokens
* resonance
* blank magic
* alchemy
* rituals
* Create / Fill / Empty

---

## Institutional magic

Originally spread across:

* contracts
* lore
* commerce
* convergence

Now consolidated into:

* 05-commerce-and-contracts.md

Including:

* contracts
* covenants
* guilds
* trust
* governance
* automated contracts
* institutional magic

---

## Setting

Originally spread across:

* lore.md
* story.md
* mentors.md

Now consolidated into:

* 06-world-and-setting.md

---

## Gameplay

Originally spread across:

* game.md
* rules.md
* interface.md

Now consolidated into:

* 07-gameplay.md

---

## Economic research

Originally spread across:

* design2.md
* pitchfork-rpg-design-notes.md

Now consolidated into:

* 08-economic-testbed.md

* 09-research-platform.md

---

## Architecture

Originally spread across:

* pitchfork-rpg-architecture.md
* pitchfork-rpg-design-notes.md

Now consolidated into:

* 01-rpg-overview.md
* 10-product-roadmap.md

---

# Remaining Concepts Worth Preserving

The following ideas have not yet been fully documented.

These should be incorporated into future documents before implementation begins.

---

# 1. Symbolic Materials (High Priority)

Original sources:

* pancakes-tokens.*
* pitchfork_magic_system.md

Originally commodities possessed symbolic magical identities.

Examples included:

* silver
* wheat
* coffee
* cotton
* gold
* oil

These should evolve into a richer symbolic materials system informed by the newer Symbolic Frequencies work rather than fixed one-to-one mappings.

Recommended future document:

```
12-symbolic-materials.md
```

Topics:

* commodities
* symbolic meanings
* magical reagents
* ecological materials
* real-world correspondence
* crafting ingredients

---

# 2. Symbolic Crafting (High Priority)

Original sources:

* design2.md
* pancakes-elements.*
* pitchfork-rpg-design-notes.md

Crafting has evolved far beyond item creation.

Within Pitchfork, crafting now includes creation of:

* artifacts
* rituals
* recipes
* contracts
* institutions
* services
* communities

Crafting should become the universal transformation mechanism of the world.

Recommended future document:

```
13-symbolic-crafting.md
```

Topics:

* recipes
* transformations
* magical manufacturing
* institutions as crafted objects
* civilization as cumulative crafting

---

# 3. Recipes As First-Class Objects

Original sources:

* pancakes-elements.*
* pitchfork-rpg-design-notes.md

Recipes are more than crafting instructions.

They are reusable knowledge.

Examples include:

* spells
* rituals
* manufacturing
* services
* educational processes
* governance processes

This should be expanded in the Symbolic Crafting document.

---

# 4. Inventory Model

Original sources:

* inventory.md

The inventory concept should evolve beyond a traditional RPG backpack.

Inventory should distinguish:

* resources
* tokens
* recipes
* contracts
* relics
* books
* research
* crafted goods

This will eventually align with the Pitchfork object model.

---

# 5. Character Development

Original sources:

* stats.md

The original D&D attributes should not be retained.

Instead, progression should emerge through participation in symbolic domains such as:

* craftsmanship
* research
* stewardship
* teaching
* exploration
* governance
* reputation
* mentorship

This remains an open design area.

---

# 6. Browser Client

Original sources:

* interface.md
* pitchfork-rpg-architecture.md

The browser interface vision remains valuable.

Important characteristics:

* lightweight
* persistent
* text-friendly
* MUD-inspired
* Kingdom of Loathing-inspired
* institution-heavy
* low bandwidth

Eventually this deserves its own client design document.

---

# 7. Resource Loop

Original sources:

* pancakes-tokens.*

The original documents consistently expressed a clear gameplay loop:

Gather

↓

Transform

↓

Craft

↓

Exchange

↓

Build

↓

Steward

The newer documentation explains philosophy well but should eventually restore this concrete gameplay loop visually.

---

# 8. Achievement Artifacts

Original sources:

* game.md

Achievement tokens should be reinterpreted.

Rather than functioning as experience points, they become historical artifacts recording meaningful contributions to civilization.

Examples:

* discoveries
* expeditions
* restoration projects
* founding institutions
* first accomplishments

---

# 9. Blank Contracts

Original sources:

* design.md
* design2.md

Blank contracts remain one of the most original ideas from the early design.

They deserve greater emphasis.

They are to institutions what blank tokens are to magical resources:

general-purpose containers waiting to receive meaning.

This concept should become central to Contract Magic.

---

# 10. The Four Fundamental Objects

One architectural insight emerged during consolidation.

Nearly everything in the symbolic world derives from four primitive object types.

```
Resources

↓

Tokens

↓

Recipes

↓

Contracts
```

Examples:

Artifact

= Resources + Recipe

Spell

= Recipe

Institution

= Contracts

Service

= Recipe + Contract

Guild

= Network of Contracts

This abstraction should eventually become part of the core Pitchfork/RPG architecture documentation.

---

# Legacy Documents Safe To Delete

After this plan and the new documentation are committed, the following documents no longer contain unique conceptual material.

```
design.md
design2.md
game.md
interface.md
inventory.md
lore.md
magic-token.md
mentors.md
pancakes-elements.1.md
pancakes-elements.2.md
pancakes-tokens.md
pancakes-tokens.2.md
pancakes-tokens.3.md
pancakes-tokens.4.md
pancakes-tokens.5.md
pancakes-tokens.6.md
pancakes-tokens.7.md
phases.md
pitchfork_magic_system.md
pitchfork_magic_system_with_contracts.md
pitchfork-rpg-architecture.md
pitchfork-rpg-design-notes.md
rules.md
stats.md
story.md
```

Their useful ideas have either been incorporated into the new documentation or explicitly captured above as future work.

---

# Future Direction

The current documentation establishes the conceptual foundation of the Pitchfork RPG.

Future work should shift away from broad world-building and toward concrete architectural design, including:

* symbolic materials,
* symbolic crafting,
* browser client architecture,
* gameplay systems,
* object model,
* recipes,
* contracts,
* research workflows,
* and implementation on top of the Pitchfork platform.

The RPG has evolved from an exploratory fantasy concept into a coherent symbolic client for the Pitchfork ecosystem, an educational pathway into the Pancakes Commonwealth, and a long-term research platform for experimenting with institutions, governance, and civilization.
