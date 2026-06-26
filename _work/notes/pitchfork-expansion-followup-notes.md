# `_work/pitchfork-expansion-followup-notes.md`

# Pitchfork Expansion Follow-up Notes

These notes capture architectural observations from the symbolic expansion planning work that did not warrant separate implementation plans but should influence future documentation and design decisions.

Most of these items are expected to become subsections of the new foundational documents rather than standalone documents.

---

# 1. Symbolic Continuity

The symbolic crafting documents introduce symbolic conservation, but there is a broader principle that should remain visible throughout the ecosystem.

**Symbolic continuity** is the idea that symbolic meaning should evolve continuously rather than being discarded whenever objects, services, or knowledge change form.

This principle extends beyond crafting.

Examples include:

* crafting preserves lineage
* inventories preserve provenance
* regional identity survives refinement
* node history contributes meaning
* services build upon previous relationships
* RPG discoveries accumulate rather than replacing earlier understanding

Symbolic continuity should become one of the recurring design principles of Pitchfork.

---

# 2. Node Metabolism

During planning the concept of **node metabolism** emerged.

This is **not** resource accounting.

Instead it models the civic and ecological systems that sustain a node.

Examples include:

* drinking water source
* wastewater destination
* electrical grid
* waste collection
* recycling
* transit systems
* conservation authority
* food systems

The purpose is understanding relationships rather than measuring consumption.

Examples:

* determining whether a boil-water advisory affects a node
* identifying local stewardship opportunities
* understanding watershed relationships
* improving quality-of-life indicators

Primary home:

* `pancakes-place-model.md`

Secondary references:

* `pancakes-reference-services.md`
* `pancakes-node-capabilities.md`

---

# 3. Facts Versus Interpretations

The architecture should preserve a clean separation between public facts and local interpretation.

Reference services answer questions such as:

* What watershed is this?
* What product has this barcode?
* Which utility serves this address?

Capabilities answer questions such as:

* What does this mean for this household?
* Which symbolic frequencies are relevant?
* Which quality-of-life indicators are affected?
* Which community opportunities should be surfaced?

This separation should remain explicit throughout the documentation.

---

# 4. Capabilities Represent Domains Of Life

Capabilities should not be described merely as software modules or plugins.

Instead, a capability represents a coherent domain of life.

Examples include:

* GIS
* GPX
* Inventory
* Pantry
* Community Quests
* Pollinator Stewardship
* Civic Infrastructure

Each capability contributes:

* data
* events
* user interfaces
* reports
* QoL indicators
* recipes
* symbolic interpretation
* reference-service integrations

This distinction should be emphasized in the node capability documentation.

---

# 5. The RPG As Curriculum

The RPG is more than preserved lore.

It is also an educational sequence.

Each chapter teaches one conceptual abstraction.

For example:

* colored magic
* tokens
* token/value separation
* contracts
* commodities
* Ether
* executable agreements
* restored balance

Future chapters should continue this pattern.

New concepts should emerge because the previous worldview becomes insufficient rather than because the mechanics changed.

---

# 6. Symbolic Terroir

The discussion of place suggested a useful organizing concept borrowed from agriculture.

Meaning arises partly from where and how something came into existence.

Examples include:

* wetland silver
* urban silver
* Rouge Valley Ember Moss
* community-crafted objects

Regional identity should emerge naturally from provenance.

It should never become a loot optimization system.

This concept belongs primarily in symbolic crafting.

---

# 7. Layered Architecture

The planning process clarified the conceptual layering of the ecosystem.

```text
Reference Services

↓

Node Core

↓

Capabilities

↓

Events

↓

Place Model

↓

Symbolic Frequencies

↓

Symbolic Crafting

↓

Applications
```

Future documentation should preserve this separation of concerns.

---

# 8. Preserve Architectural Vocabulary

The new foundational documents establish shared terminology.

Application documents should reference these concepts rather than redefining them.

Canonical concepts now include:

* symbolic frequencies
* symbolic crafting
* symbolic continuity
* place model
* homeland
* stewardship
* reference services
* node capabilities
* provenance
* symbolic terroir
* node metabolism

Keeping these concepts centralized should reduce duplication and improve long-term consistency across the documentation.

---

# 9. Potential Future Work

These ideas emerged during planning but are intentionally deferred.

Possible future design documents include:

* Pancakes Design Principles
* Civic Infrastructure Registry
* Open Species Database
* Household Knowledge Graph
* Community Stewardship Model
* Symbolic Ecology

These should only be developed if they become independently significant rather than being extracted prematurely from the current foundational documents.

---

# Closing Observation

The symbolic expansion planning clarified a major architectural shift.

Originally, Pitchfork centered on symbolic magic and commodities.

The current architecture is broader.

It begins with shared public knowledge, extends nodes through modular capabilities, grounds those capabilities in place, derives symbolic meaning through frequencies, preserves that meaning through symbolic crafting, and finally presents different interpretations through applications such as the RPG, Lone Honk, Wellness Notebook, and future clients.

The result is a layered architecture in which symbolic systems emerge from ordinary life rather than replacing it.
