# Outline: `docs/pitchfork-symbolic-frequencies.md`

## Purpose

Define symbolic frequencies as the semantic bridge connecting the real world, the symbolic RPG world, and the commerce/accounting world.

This document introduces the conceptual model underlying resources, commodities, colors, places, activities, and symbolic meaning. It does **not** define crafting algorithms; those belong in `pitchfork-symbolic-crafting.md`.

---

# 1. Introduction

## Motivation

Explain the design problem.

Ordinary life produces events.

Pitchfork projects those events into symbolic worlds without disconnecting them from reality.

Frequencies provide the common language shared by:

* Pancakes
* Pitchfork
* the RPG
* commerce
* node quality-of-life systems

### Design Goals

* unify multiple interpretations of the same event
* preserve symbolic meaning
* avoid arbitrary game mechanics
* allow future expansion without redesign
* support regional and cultural variation

---

# 2. The Three Worlds

Introduce the existing Three-World model.

## The Real World

Examples:

* walking
* studying
* gardening
* cleaning
* menstruation
* caregiving
* cooking

---

## The Symbolic World

The RPG interpretation.

Examples:

* Ember Moss
* Moonwater
* Order Salt
* Covenant Runes

---

## The Commerce World

Accounting and economic interpretation.

Examples:

* events
* commodities
* inventories
* contracts
* services
* ledgers

---

## Projection Principle

One real event may be viewed simultaneously through all three worlds.

No world is more "real" than another.

---

# 3. What Is A Frequency?

Definition.

A frequency is a recurring pattern of reality that can be interpreted across multiple symbolic systems.

Explain why frequencies are not:

* RPG stats
* metadata
* item tags
* arbitrary enchantments

Instead they represent recurring human, ecological, economic, and physical patterns.

---

# 4. Orthogonal Frequency Vectors

Core concept.

Objects are not defined by one property.

They carry many independent symbolic frequencies.

Illustrate vectors.

Example:

Walking through Rouge Park in spring while collecting silver.

Produces frequencies for:

* movement
* stewardship
* wetland
* spring
* silver
* purification

Explain orthogonality.

Each dimension remains independently meaningful.

---

# 5. Categories Of Frequencies

Introduce the major families.

## Activity Frequencies

Examples:

* movement
* learning
* stewardship
* cooking
* caregiving

---

## Place Frequencies

Examples:

* wetland
* forest
* river
* urban
* escarpment

Mention:

GIS contributes place frequencies.

---

## Commodity Frequencies

Examples:

* silver
* coffee
* wheat
* oil
* electricity

Commodity frequencies arise from symbolic interpretation of real commodities.

---

## Color Frequencies

Relationship to mentor colors.

Explain that colors summarize broad patterns rather than replacing other frequencies.

---

## Temporal Frequencies

Examples:

* season
* moon
* recurrence
* cycles

---

## Social Frequencies

Examples:

* cooperation
* exchange
* governance
* hospitality

---

## Future Frequency Families

Architecture intentionally supports unforeseen categories.

Reference Sneeds philosophy.

---

# 6. Intrinsic And Acquired Frequencies

One of the key ideas.

## Intrinsic

Properties inherent to the thing.

Examples:

* silver
* wood
* salt
* coffee

---

## Acquired

Properties gained through history.

Examples:

* walked in Rouge
* harvested in spring
* used in community cleanup
* crafted during a festival

Explain provenance.

History matters.

---

# 7. Place And Provenance

Discuss why place matters.

Examples:

* Rouge Valley
* wetlands
* watersheds
* aquifers

Explain symbolic terroir.

Mention:

Place contributes symbolic meaning.

Place does not imply superiority.

Avoid treating regions as loot tables.

---

# 8. Frequencies And Node Capabilities

Explain that frequencies may originate from capabilities.

Examples:

GIS capability contributes:

* watershed
* biome
* park

Barcode capability contributes:

* commodity
* packaging

Community capability contributes:

* stewardship
* volunteering

Future capabilities may introduce additional frequency families.

---

# 9. Frequencies And Mentors

Relationship to the RPG.

Mentors interpret frequencies.

They do not own frequencies.

Example:

Silver Frequency

↓

Red Witch

↓

Moonwater

↓

Cycle Magic

Different mentors may interpret overlapping frequencies differently.

---

# 10. Frequency Conservation (Overview)

Brief conceptual introduction only.

State the principle:

Symbolic meaning should survive transformation.

Do not define algorithms.

Refer readers to:

`pitchfork-symbolic-crafting.md`

---

# 11. Worked Examples

Include several end-to-end examples.

Example:

Walking

↓

Movement

↓

Red

↓

Ember Moss

↓

Movement Event

---

Walking through Rouge wetlands

↓

Movement

Wetland

Stewardship

↓

Ember Moss carrying regional frequencies

---

Silver gathered through stewardship

↓

Silver

Purification

Wetland

↓

Silver Saber

(History preserved.)

---

Oil

↓

Energy

Extraction

↓

Corrupted Ember

Explain corruption without treating commodities as morally absolute.

---

# 12. Design Rules

Summarize.

Examples:

* Frequencies describe patterns, not power levels.
* Frequencies are orthogonal.
* Frequencies are extensible.
* Frequencies may originate from node capabilities.
* Frequencies preserve symbolic continuity.
* Frequencies should arise from meaningful real-world relationships.
* New frequencies should require new knowledge rather than new architecture.

---

# 13. Relationship To Other Documents

Explain document boundaries.

This document defines:

* frequencies
* vectors
* provenance
* symbolic meaning

Other documents define:

* symbolic crafting
* recipes
* node capabilities
* place model
* reference services
* RPG mechanics

This document should become the canonical conceptual reference for symbolic frequencies throughout the Pancakes and Pitchfork ecosystem.
