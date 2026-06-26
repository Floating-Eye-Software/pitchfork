# Outline: `docs/pitchfork-symbolic-crafting.md`

## Purpose

Define how symbolic objects are transformed while preserving meaningful continuity.

This document establishes the laws governing symbolic transformation throughout the Pitchfork ecosystem.

It does **not** define what frequencies are; that belongs in `pitchfork-symbolic-frequencies.md`.

Instead, it explains how symbolic meaning survives, changes, combines, or is intentionally altered as objects are crafted, refined, exchanged, and used.

---

# 1. Introduction

## Motivation

Traditional RPG crafting destroys history.

```
Iron Ore
↓

Iron Bar
↓

Sword
```

The game forgets where the ore came from.

Pitchfork intentionally does not.

Crafting is not merely manufacturing.

It is symbolic transformation.

---

## Design Goals

Crafting should:

* preserve meaningful history
* respect provenance
* avoid arbitrary rarity
* encourage stewardship
* remain mathematically composable
* remain extensible

---

# 2. Symbolic Conservation

Introduce the central principle.

> Symbolic meaning is conserved unless intentionally transformed.

Explain that conservation is analogous to conservation laws in physics.

Crafting changes form.

It does not automatically erase meaning.

---

## Conservation Is Conceptual

This is not an implementation requirement for every field.

It is a design principle.

Meaning should survive unless a recipe explicitly changes it.

---

# 3. Craft Lineage

Every symbolic object has ancestry.

Examples:

```
Walk

↓

Ember Moss

↓

Refined Ember Moss

↓

Traveler's Charm
```

The charm remembers its lineage.

Explain why lineage matters.

---

# 4. Transformation Operations

Introduce the primitive symbolic operations.

---

## Refinement

Concentrate existing meaning.

Examples:

Ember Moss

↓

Rouge Leaf

---

## Amplification

Increase one symbolic frequency.

Example:

Purification ritual

↓

Stronger purification resonance.

---

## Attenuation

Reduce one symbolic aspect.

Example:

Repeated industrial processing reduces ecological resonance.

---

## Mixing

Combine frequencies from multiple inputs.

Example:

Silver

*

Wetland

*

Community Cleanup

↓

Shared symbolic object.

---

## Filtering

Retain selected frequencies while discarding others.

Explain intentional forgetting.

---

## Conversion

Transform one symbolic interpretation into another while preserving continuity.

Example:

Commodity

↓

Magic

↓

Service

---

## Corruption

Meaning becomes distorted.

Explain:

corruption

≠

evil

Corruption represents imbalance, contamination, exploitation, fragmentation, etc.

---

## Purification

Restore balance.

Do not define purification as "good."

It restores intended relationships.

---

# 5. Symbolic Provenance

Discuss history.

Where something came from matters.

Examples:

* who created it
* where it was gathered
* when
* stewardship context
* household history

History contributes symbolic identity.

---

# 6. Symbolic Terroir

One of the major new ideas.

Borrow the concept of terroir.

Meaning comes partly from place.

Examples:

Silver from wetlands

Silver from cities

Forest herbs

Prairie herbs

Explain:

Different

≠

better.

Avoid optimization.

---

# 7. Regional Crafting

Describe regional identity.

Examples:

Rouge Valley

Duffins Creek

Wetlands

Escarpment

Crafting may preserve regional relationships.

Explain:

Regional identity emerges naturally.

It should not become loot grinding.

---

# 8. Activities As Ingredients

Activities themselves contribute symbolic frequencies.

Examples:

Walking

Teaching

Cooking

Repair

Caregiving

Stewardship

Objects inherit aspects of the activities that produced them.

---

# 9. Recipes As Symbolic Transformations

Explain what recipes actually do.

Recipes transform:

* matter
* symbolic meaning
* history

Not merely inventories.

Recipes define transformation rules.

---

# 10. Community Crafting

Multiple participants.

Examples:

Community cleanup.

Festival.

Household meal.

Explain shared symbolic ancestry.

Objects may inherit collaborative frequencies.

---

# 11. Node And Capability Contributions

Capabilities contribute additional symbolic dimensions.

Examples:

GIS

↓

Place frequencies

Barcode

↓

Commodity frequencies

Community

↓

Volunteer frequencies

Future capabilities integrate naturally.

---

# 12. Frequency Algebra

High-level overview.

Discuss symbolic vectors.

Operations:

* addition
* amplification
* attenuation
* filtering
* inheritance

Avoid implementation mathematics.

Conceptual only.

---

# 13. Examples

Worked examples.

---

## Example 1

Walking

↓

Ember Moss

↓

Traveler's Charm

History preserved.

---

## Example 2

Rouge wetlands

↓

Ember Moss

↓

Rouge Leaves

↓

Wetland Lantern

Place identity retained.

---

## Example 3

Silver earned through stewardship

↓

Silver Saber

Purification

Stewardship

Wetland

remain present.

---

## Example 4

Oil gathered through extractive processes

↓

Industrial Catalyst

Extraction frequency amplified.

Discuss without assigning moral absolutes.

---

## Example 5

Community Cleanup

↓

Recovered Materials

↓

Community Monument

The artifact remembers cooperation.

---

# 14. Relationship To The RPG

Explain that crafting is interpreted differently by mentors.

The same symbolic transformation may appear as:

* alchemy
* ritual
* blacksmithing
* weaving
* cooking

depending on mentor tradition.

Crafting laws remain universal.

---

# 15. Design Rules

Summarize.

Examples:

* Crafting preserves symbolic continuity.
* Provenance matters.
* Place matters.
* Activities matter.
* Community participation matters.
* Recipes define transformation rather than arbitrary conversion.
* Regional identity should emerge naturally.
* Crafting should reward relationships rather than optimization.
* Symbolic history should be retained whenever practical.

---

# 16. Relationship To Other Documents

Boundaries.

This document defines:

* transformation
* conservation
* refinement
* lineage
* provenance
* terroir

It references but does not redefine:

* symbolic frequencies
* recipes
* node capabilities
* place model
* reference services
* RPG lore

The goal is to make symbolic crafting a general transformation framework shared by the RPG, Pancakes, and future applications rather than a crafting system tied to any single game mechanic.
