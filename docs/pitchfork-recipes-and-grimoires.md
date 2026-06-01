# Pitchfork Recipes and Grimoires

## A Unified Transformation Model for Lifecraft, Covenants, and Symbolic Worlds

**Status:** Draft
**Character:** Foundational Architecture Specification

---

# Purpose

This document defines the Recipe and Grimoire model used throughout the Pitchfork ecosystem.

Pitchfork is often described as:

* an accounting system,
* a covenant system,
* a symbolic economy,
* a world projection engine,
* or a roleplaying framework.

Each description is partially correct.

At a deeper level, Pitchfork is a system for representing and settling transformations.

Human life is composed of transformations:

* meals become nourishment,
* effort becomes competence,
* care becomes continuity,
* commitments become trust,
* rituals become meaning,
* stewardship becomes flourishing,
* agreements become institutions.

Pitchfork provides a shared structure for representing these transformations without reducing them to productivity metrics or economic transactions.

The primary abstraction used to model transformation is the **Recipe**.

---

# Core Concept

A recipe is a reusable description of transformation.

In ordinary life:

```text
ingredients
+ process
=
meal
```

In Pitchfork:

```text
inputs
+ participants
+ process
+ settlement
=
transformation
```

Recipes describe how one state of the world may become another.

The transformation may be:

* material,
* personal,
* social,
* symbolic,
* economic,
* ecological,
* institutional,
* or magical.

---

# Why Recipes?

Most systems organize activity around tasks.

```text
Task
→ Completion
→ Reward
```

Pitchfork instead emphasizes transformation.

```text
Recipe
→ Transformation
→ Settlement
→ Outcome
```

This distinction matters.

Many meaningful human activities cannot be reduced to tasks:

* raising children,
* maintaining a household,
* building trust,
* recovering from illness,
* caring for elders,
* cultivating friendships,
* strengthening communities.

Recipes provide a broader and more humane model.

---

# Why Recipes Instead of Contracts?

Contracts are a special case.

Contracts focus on:

```text
obligation
→ enforcement
→ settlement
```

Recipes focus on:

```text
ingredients
→ process
→ transformation
```

Many important transformations are not contractual.

Examples:

* learning,
* caregiving,
* homemaking,
* rest,
* reflection,
* stewardship.

Contracts become one type of recipe-derived structure rather than the foundation of the system.

---

# Recipe Structure

A recipe defines a transformation.

Conceptually:

```yaml
recipe:
  id:
  name:

  purpose:

  participants:

  inputs:

  process:

  settlement:

  outputs:

  privacy_boundary:

  metadata:
```

Not all fields are required.

Different recipe types emphasize different elements.

---

# Recipe Components

## Purpose

Purpose explains why the recipe exists.

Examples:

```text
Maintain household continuity.
```

```text
Improve sleep quality.
```

```text
Redistribute invisible labor.
```

```text
Strengthen community trust.
```

Purpose is central because Pitchfork tracks meaningful transformation rather than isolated activity.

---

## Participants

Participants identify who is involved.

Examples:

* individual,
* household,
* guild,
* cooperative,
* institution,
* mentor circle.

Participation may be explicit or role-based.

---

## Inputs

Inputs are resources, conditions, or prerequisites.

Examples:

* materials,
* time,
* attention,
* knowledge,
* previous accomplishments,
* participation,
* permissions.

Inputs may be physical, symbolic, or social.

---

## Process

The process describes how transformation occurs.

Examples:

```text
Review pantry.
Plan meals.
Create shopping list.
```

```text
Gather participants.
Conduct review.
Redistribute responsibilities.
```

The process may be structured, narrative, or ritualized.

---

## Settlement

Settlement determines when the transformation is considered complete.

Examples:

```text
Seven days of meals planned.
```

```text
Household workload inventory completed.
```

```text
Bridge repaired.
```

```text
Proposal adopted.
```

Settlement is one of the most important concepts in Pitchfork.

Recipes define transformation.

Settlement confirms transformation.

---

## Outputs

Outputs describe what emerges.

Examples:

* crafted items,
* trust,
* continuity,
* reputation,
* access,
* resources,
* permissions,
* world-state changes.

Outputs may be tangible or intangible.

---

## Privacy Boundary

Recipes should declare intended visibility.

Examples:

* private,
* household,
* guild,
* trusted participants,
* public symbolic,
* settlement only.

This aligns recipes with the broader Pitchfork privacy model.

---

# Recipe Types

The same recipe structure supports many forms of transformation.

---

# Lifecraft Recipes

Lifecraft recipes describe ordinary human flourishing.

Examples:

* meal planning,
* sleep preparation,
* study practice,
* movement routines,
* budgeting,
* reflection.

These are the most common Pancakes-facing recipes.

---

# Household Recipes

Household recipes support continuity and stewardship.

Examples:

* meal planning,
* laundry continuity,
* household review,
* cleaning cycles,
* family meetings,
* hospitality preparation.

A household recipe focuses on outcomes rather than chores.

Example:

```text
Recipe:
Clothing Continuity

Settlement:
All household members have sufficient clean clothing.
```

The focus is continuity, not labor extraction.

---

# Ritual Recipes

Ritual recipes transform action into meaning.

Examples:

* seasonal review,
* gratitude practice,
* sanctuary restoration,
* personal reflection,
* mentor-guided exercises.

Rituals emphasize intention, rhythm, and symbolism.

---

# Covenant Recipes

A covenant recipe describes a transformation that depends upon shared commitment.

Examples:

* household agreements,
* cooperative participation,
* governance processes,
* mutual aid commitments.

The recipe defines the transformation.

The covenant defines who agrees to participate.

---

# Governance Recipes

Governance recipes transform participation into decisions.

Examples:

* elections,
* proposal reviews,
* budget approvals,
* steward appointments.

These recipes support institutional continuity.

---

# Service Recipes

Service recipes transform effort into value exchange.

Examples:

* childcare exchange,
* community support,
* volunteer work,
* cooperative labor.

These recipes provide the conceptual bridge between service exchange and symbolic accounting.

---

# Crafting Recipes

Crafting recipes transform materials into objects.

Examples:

* tools,
* charms,
* artifacts,
* sanctuary upgrades,
* symbolic resources.

These are most visible within RPG clients but use the same underlying structure.

---

# Spells

A spell is a recipe expressed through magical language.

Examples:

* blessings,
* wards,
* sanctuary rituals,
* threshold protections.

The distinction between a recipe and a spell is interpretive rather than structural.

A spell remains a transformation.

---

# Covenants

A covenant is a social agreement attached to a recipe.

Recipes define:

```text
what transformation means
```

Covenants define:

```text
who agrees
```

Relationship:

```text
Recipe
→ defines transformation

Covenant
→ binds participants to that transformation
```

Example:

```yaml
covenant:
  recipe: household_load_review

  participants:
    - Alex
    - Jordan

  steward:
    Alex

  witness_rule:
    self_attestation

  settlement_rule:
    recipe_settled

  privacy_boundary:
    household
```

A covenant is therefore a social wrapper around a recipe.

---

# Magical Agreements

Within symbolic and RPG clients, covenants may be presented as magical agreements.

Examples:

```text
Threshold Covenant
Hearth Covenant
River Oath
Sanctuary Pact
```

The underlying structure remains identical.

The presentation changes.

This allows ordinary life agreements and magical roleplay to share the same architecture.

---

# Smart Contracts

Smart contracts are another specialization of covenants.

Relationship:

```text
Recipe
→ Transformation

Covenant
→ Social Agreement

Smart Contract
→ Enforceable Settlement Mechanism
```

Most recipes will never require smart contracts.

Most covenants will never require smart contracts.

However, future Pitchfork infrastructure may support:

* cooperative treasuries,
* shared ownership,
* service exchange,
* community currencies,
* crypto-compatible settlement systems.

In these cases:

```text
Recipe
→ Covenant
→ Smart Contract
```

provides a natural progression.

---

# Grimoires

A grimoire is a collection of recipes.

Recipes describe transformations.

Grimoires organize knowledge.

Examples:

* personal grimoires,
* household grimoires,
* mentor grimoires,
* guild grimoires,
* institutional grimoires.

---

# Personal Grimoires

Personal grimoires contain transformations cultivated by an individual.

Examples:

* morning routines,
* study practices,
* reflection rituals,
* health systems.

---

# Household Grimoires

Household grimoires preserve practical household wisdom.

Examples:

* meal planning,
* family meetings,
* household audits,
* continuity reviews.

Household grimoires make invisible knowledge visible and transferable.

---

# Mentor Grimoires

Mentors teach through grimoires.

Mentors do not primarily assign tasks.

Mentors curate transformations.

Examples:

### Hearth Mentor

* Meal Planning
* Hospitality Preparation
* Shared Cooking
* Pantry Stewardship

### Stone Mentor

* Household Audit
* Laundry Continuity
* Sanctuary Maintenance
* Continuity Planning

### River Mentor

* Family Meetings
* Conflict Repair
* Relationship Check-Ins

Mentors become stewards of wisdom rather than productivity managers.

---

# Recipe Graphs

Recipes may depend on other recipes.

Examples:

```text
Meal Planning
    ↓
Shared Cooking
    ↓
Hospitality Gathering
```

or:

```text
Household Review
    ↓
Responsibility Redistribution
    ↓
Continuity Covenant
```

Recipe graphs support:

* progression,
* achievements,
* quests,
* governance pathways,
* learning journeys.

Without requiring separate systems.

---

# Relationship to Pancakes

Pancakes is the human-facing lifecraft layer.

Pitchfork is the transformation, covenant, and settlement layer.

Relationship:

```text
Pancakes
→ Recipes

Pitchfork
→ Covenants
→ Settlement
→ Accounting
```

A user interacts with recipes.

Pitchfork records and settles transformations.

---

# Relationship to Projections

The same settled transformation may appear differently across clients.

Example:

```text
Recipe:
Household Review
```

Pancakes:

```text
Household review completed.
```

Pitchfork:

```text
Covenant settled.
```

RPG:

```text
Threshold Wax +1
```

Ambient World:

```text
Sanctuary stability increases.
```

Different interpretations.

Shared underlying transformation.

---

# Design Principles

## Transformation Over Optimization

Support meaningful transformation rather than productivity maximization.

## Stewardship Over Extraction

Recognize maintenance, care, and continuity.

## Meaning Over Metrics

Use accounting to support interpretation, not replace it.

## Consent Over Surveillance

Participation should be transparent and bounded.

## Wisdom Over Automation

Recipes should augment human judgment.

## Many Worlds, One Transformation Layer

Different clients may interpret the same recipe differently.

The transformation remains consistent.

---

# Conclusion

Recipes are the foundational transformation primitive of the Pitchfork ecosystem.

Crafting, rituals, covenants, spells, service exchange, governance processes, quests, achievements, and future smart-contract-backed systems can all be understood as specializations of the same underlying structure.

Grimoires organize these transformations into reusable bodies of knowledge.

Together, recipes and grimoires provide a shared foundation for lifecraft, stewardship, cooperation, symbolic worlds, and future economic systems.

Pitchfork is not fundamentally a game, an economy, or a task manager.

It is a transformation system.

Recipes describe transformation.

Covenants coordinate transformation.

Settlement records transformation.

Grimoires preserve transformation.
