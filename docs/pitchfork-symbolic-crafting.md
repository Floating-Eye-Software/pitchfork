# Pitchfork Symbolic Crafting

## Purpose

Symbolic crafting defines how meaningful objects, services, resources, and
records transform while preserving continuity.

This document is the canonical foundation for symbolic transformation. It
depends on `pitchfork-symbolic-frequencies.md`, which defines frequencies and
frequency vectors. This document explains how those frequencies are conserved,
combined, refined, filtered, and intentionally transformed.

## Canonical Definition

Symbolic crafting is transformation with memory.

A crafted object is not merely an output inventory item. It is a new form that
inherits relevant meaning from its inputs, recipe, makers, activities, places,
and history. Crafting changes form. It should not erase provenance unless the
recipe explicitly calls for forgetting, purification, anonymization, or other
intentional transformation.

The central rule is:

```text
Symbolic meaning is conserved unless intentionally transformed.
```

This is a design principle, not a requirement that every field be retained in
every database row. Implementations may summarize, derive, project, or archive
details. The conceptual model remains that meaningful history survives by
default.

## Craft Lineage

Every symbolic object has lineage. A walk may produce Ember Moss. Ember Moss
may be refined into Rouge Leaves. Rouge Leaves may become a Traveller's Charm.
The charm should remember enough lineage to preserve the relationship between
movement, place, activity, and craft.

Lineage matters because Pancakes and Pitchfork are not trying to produce
anonymous game materials. They are trying to preserve relationships between
life, meaning, stewardship, and exchange.

Lineage can include:

* input resources
* activities that produced those resources
* places and reference contexts
* participants and roles
* time and season
* stewardship or community context
* recipes and transformation operations
* household or node history

## Transformation Operations

Symbolic crafting uses a small set of conceptual operations. Implementations
may represent them differently, but later documents should preserve these
meanings.

Refinement concentrates existing meaning. A raw movement resource may become a
more focused travel resource. Refinement should make the dominant frequency
clearer without pretending the earlier history never existed.

Amplification strengthens one or more frequencies. A purification ritual might
amplify purification resonance in silver that already carried wetland and
stewardship context.

Attenuation reduces a frequency. Repeated industrial processing may attenuate
ecological context. A privacy-preserving recipe may attenuate identifying
household context before sharing a community artifact.

Mixing combines frequencies from multiple inputs. A community meal may combine
food, hospitality, neighbourhood, caregiving, and seasonal frequencies.

Filtering preserves selected frequencies and discards or hides others. This is
intentional forgetting. It must be treated as a meaningful transformation, not
as accidental data loss.

Conversion changes the interpretive form of meaning. A commodity may become a
symbolic resource, a symbolic resource may become a service, or a service may
be represented as a contract. Continuity remains even when the projection
changes.

Corruption is distortion, imbalance, contamination, extraction, exploitation,
fragmentation, or broken relationship. It is not a synonym for evil.

Purification restores intended relationship or balance. It is not a generic
"good" operation. It should be meaningful only in context.

## Symbolic Terroir

Symbolic terroir is the way place contributes to meaning.

A wetland silver object and an urban library silver object are not ranked
versions of the same thing. They are different histories. The wetland object
may carry water, stewardship, species, and restoration context. The library
object may carry learning, civic, exchange, and public knowledge context.

Regional identity should emerge from provenance. It should not become a
grinding mechanic or a ranking system for places.

## Activities As Ingredients

Activities can be ingredients because activities carry frequencies.

Walking, teaching, cooking, repairing, caregiving, gardening, budgeting, and
volunteering can contribute meaning to crafted outputs. The activity does not
need to become a physical item first. A recipe may consume an event projection,
a service record, a resource, or a symbolic material depending on the domain.

This is especially important for household and civic systems. A repaired tool,
a shared meal, a neighbourhood cleanup, and a pollinator survey all carry
activity histories that matter.

## Recipes

A recipe is a rule for symbolic transformation.

Recipes may define required inputs, optional context, transformation
operations, expected outputs, permissions, safety constraints, provenance
rules, and quality-of-life effects. A recipe should explain what meaning is
preserved, what is amplified, what is filtered, and what is newly created.

Recipes are not limited to cooking or RPG crafting. They can describe service
work, community participation, household routines, repair, rituals, education,
and civic practices.

## Community Crafting

Some crafted outputs have shared ancestry.

A community cleanup may produce recovered materials, stewardship records,
shared recognition, place relationships, and symbolic resources. A festival may
produce hospitality, cultural, food, music, seasonal, and neighbourhood
frequencies. A household meal may combine pantry, care, budget, nutrition, and
family history.

Shared lineage does not mean every participant receives the same private data.
Nodes should preserve local privacy while allowing shared artifacts to carry
community context.

## Capability Contributions

Capabilities contribute additional symbolic dimensions to crafting.

A GIS capability can add place frequencies. A barcode capability can add
commodity and packaging frequencies. An inventory capability can add household
goods context. A civic infrastructure capability can add water, transit, waste,
and public alert context. A pollinator stewardship capability can add species,
habitat, and community science context.

Capabilities should contribute context through shared events and reference
services. They should not bypass the crafting model by inventing private
meaning systems.

## Non-Goals

This document does not define storage schemas, settlement algorithms, UI flows,
drop rates, rarity tables, or game balance. It also does not require permanent
retention of personally sensitive details.

Privacy-preserving transformation is valid symbolic crafting. A recipe may
summarize, redact, anonymize, or localize provenance when sharing details would
violate household privacy or community trust.

## Examples

A walk becomes Ember Moss. Ember Moss becomes a Traveller's Charm. The charm
retains movement lineage and may also retain place, season, or stewardship
frequencies if those were part of the original activity.

Rouge wetland activity produces a movement resource with wetland and place
context. Refinement can turn it into Rouge Leaves. A Wetland Lantern crafted
from those leaves can retain regional identity without making Rouge Valley a
superior resource source.

Silver earned through stewardship can become a Silver Saber. Silver,
purification, stewardship, and wetland frequencies may remain present. If a
recipe filters location details for privacy, it should still preserve the fact
that stewardship shaped the item.

An industrial catalyst made from oil may amplify energy and extraction
frequencies. A later purification recipe might reduce imbalance or restore
relationships, depending on the story, service, or civic context.

A community cleanup can produce recovered materials and a community monument.
The artifact can remember cooperation, place, stewardship, and repair without
exposing private participant histories.

## What Later Documents Should Reference

Later documents should reference this article when they need canonical language
for symbolic conservation, craft lineage, symbolic terroir, transformation
operations, recipe semantics, community crafting, and capability contributions
to symbolic transformation.

Application documents should describe concrete behaviours. They should not
redefine symbolic conservation or the meaning of crafting.
