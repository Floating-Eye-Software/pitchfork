# Pitchfork Symbolic Frequencies

## Purpose

Symbolic frequencies are the shared vocabulary that lets Pancakes and
Pitchfork interpret ordinary life, symbolic play, and economic accounting as
different views of the same underlying events.

This document is the canonical foundation for symbolic frequency concepts. It
defines frequencies, frequency vectors, provenance, and the relationship
between real activity, symbolic interpretation, and commerce. It does not
define crafting operations; those belong in `pitchfork-symbolic-crafting.md`.

## Canonical Definition

A symbolic frequency is a recurring pattern of meaning that can be interpreted
across multiple systems.

Frequencies are not RPG statistics, item tags, arbitrary enchantments, or
metadata labels. They represent durable patterns such as movement, recovery,
learning, stewardship, exchange, governance, wetland, silver, spring, or
cooperation. A frequency may be visible as a real-world activity, a symbolic
resource, a quality-of-life signal, or an economic concept depending on the
reader.

The same event can therefore be projected into three worlds:

* The real world: walking, studying, cooking, menstruation, budgeting,
  caregiving, repair, trade, and stewardship.
* The symbolic world: essences, materials, rituals, mentors, attunements,
  spells, and RPG resources.
* The commerce world: events, inventories, commodities, contracts, services,
  ledgers, and settlement records.

No projection replaces the others. A walk remains a walk. It may also carry a
movement frequency, produce Ember Moss in an RPG projection, contribute to a
wellness history, or settle as an activity event.

## Frequency Vectors

Objects and events are not defined by a single frequency. They carry vectors of
orthogonal frequencies.

Orthogonal means that each dimension remains independently meaningful. A walk
through a wetland in spring during a community cleanup may carry movement,
wetland, spring, stewardship, cooperation, and place frequencies at the same
time. None of those meanings needs to erase the others.

This keeps the model extensible. A future capability can add a pollinator,
accessibility, transit, or food-security frequency without changing the
fundamental architecture. The new dimension can coexist with older dimensions
as long as it describes a coherent pattern of meaning.

## Frequency Families

Frequency families group related dimensions without limiting future growth.

Activity frequencies arise from what happened. Examples include movement,
learning, cooking, repair, caregiving, budgeting, teaching, and stewardship.

Place frequencies arise from where something happened or what places it is
related to. Examples include wetland, forest, watershed, aquifer, urban,
neighbourhood, park, escarpment, trail, and library.

Commodity frequencies arise from material and economic identity. Examples
include silver, wheat, coffee, wood, electricity, oil, salt, water, and repair
parts. Commodity frequencies do not make commodities morally absolute; they
describe symbolic and practical relationships.

Temporal frequencies arise from time. Examples include season, moon phase,
recurrence, cycle, anniversary, harvest, school term, and festival.

Social frequencies arise from relationships between people and institutions.
Examples include cooperation, exchange, hospitality, mutual aid, governance,
contract, mentorship, and common stewardship.

Color frequencies summarize broad symbolic traditions used by RPG and mentor
interpretations. Colors are useful lenses, not replacements for detailed
frequency vectors.

## Intrinsic And Acquired Frequencies

Intrinsic frequencies come from what a thing is. Silver carries silver
frequency. Wood carries wood frequency. A community garden carries garden and
place frequencies even before any particular node interacts with it.

Acquired frequencies come from history. Silver found during a creek cleanup
may acquire stewardship, wetland, and community frequencies. Bread baked for a
neighbour may acquire hospitality and caregiving frequencies. A repaired tool
may acquire repair, continuity, and household frequencies.

This is provenance. History matters because meaning accumulates through use,
place, relationship, and transformation.

## Place And Provenance

Place contributes context without becoming a scoring system. A Rouge Valley
object, an escarpment object, and an urban library object may carry different
place frequencies because their histories differ. Different does not mean
better.

The place model exists to support local meaning, stewardship, and awareness. It
must not turn regions into loot tables or optimize identity into gameplay
advantage. Indigenous territories, place names, and treaty contexts are
contextual knowledge and must not become game resources.

Symbolic terroir is the idea that meaning partly arises from where and how
something came into being. It should preserve provenance and relationship, not
rank places.

## Capabilities As Frequency Sources

Frequencies may originate from node capabilities.

A GIS capability can contribute watershed, aquifer, park, trail, and civic
boundary context. A barcode capability can contribute product, ingredient,
packaging, repairability, and commodity context. A pollinator stewardship
capability can contribute habitat, native plant, observation, and community
science context. A civic infrastructure capability can contribute water,
wastewater, transit, waste, and public alert context.

Capabilities do not create meaning from nowhere. They expose coherent domains
of life that can add dimensions to the frequency vector.

## Relationship To The RPG

Mentors, schools of magic, resources, rituals, and lore interpret frequencies.
They do not own them.

For example, silver may be interpreted by one mentor as purification, by
another as lunar rhythm, and by a commerce view as a commodity. The frequency
remains shared while each projection gives it a different teaching role.

The RPG should use frequencies to teach abstractions through story and play.
Architecture remains canonical outside the lore.

## Non-Goals

This document does not define crafting algorithms, recipe execution, database
schemas, balance rules, mentor lore, or UI presentation.

It also does not require every implementation to store every possible
frequency. Implementations may choose compact representations, derived
projections, or partial views as long as they preserve the conceptual boundary:
frequencies describe meaningful patterns, not arbitrary power levels.

## Examples

A walk produces a movement frequency. In an RPG projection it may appear as
Ember Moss. In the commerce world it may settle as a movement event. In a
quality-of-life view it may support activity and access indicators.

A walk through a wetland during a stewardship event carries movement, wetland,
place, stewardship, and cooperation frequencies. The wetland context should
come from public reference data or local node knowledge, while the private walk
history remains local to the node.

Silver gathered through stewardship may carry silver, purification, wetland,
and community frequencies. If later crafted into a symbolic item, those
frequencies should remain available unless a recipe explicitly transforms or
filters them.

Oil may carry energy and extraction frequencies. A symbolic projection may
represent imbalance, dependence, or industrial force, but the model should not
treat any commodity as morally simple. Context and provenance matter.

## What Later Documents Should Reference

Later documents should reference this article when they need canonical language
for frequencies, frequency vectors, intrinsic meaning, acquired meaning,
provenance, symbolic terroir, and the Three Worlds projection model.

Application documents should define behaviour and examples. They should not
redefine what a symbolic frequency is.
