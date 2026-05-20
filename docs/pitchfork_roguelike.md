# Pitchfork Roguelike: The Nexus

## Purpose

This document defines the design direction for the Nexus roguelike client inside the broader Pitchfork/Pancakes ecosystem.

The Nexus roguelike is not a standalone game disconnected from the rest of the platform. It is a shared symbolic settlement-space where accounting, rituals, inventories, contracts, vendors, guilds, factions, crafting, projections, and social systems become spatial and explorable.

The Nexus should feel like:

* A roguelike town.
* A MUD crossroads.
* A magical market.
* A procedural social settlement.
* A ledger made physical.
* A symbolic operating system for the Pancakes ecosystem.

The Nexus is where systems meet.

It is not primarily:

* a combat MMO,
* a giant overworld,
* or a realtime action game.

It is a persistent social infrastructure layer rendered as a roguelike settlement.

The strongest inspirations are:

* NetHack Minetown.
* ADOM settlements.
* MUD hubs and guild halls.
* Caves of Qud villages.
* Kingdom of Loathing's low-friction interaction model.
* Traditional roguelike inventories and vendors.
* Social simulation games.
* Shared settlement spaces in MMOs.

## One-Sentence Summary

The Nexus is a persistent roguelike settlement layered on top of the Pitchfork accounting system where players explore markets, guild halls, contracts, sanctuaries, vendors, rituals, and faction systems generated from real-life and game-originated platform events.

---

# Core Design Philosophy

The Nexus is not "the game world."

The Nexus is:

* the convergence point,
* the social crossroads,
* the accounting-visible layer,
* and the symbolic settlement-space of the ecosystem.

Other clients generate events.

The Nexus spatializes and interprets those events.

Example:

```text
Player logs a walk in Pancakes
↓
Movement event enters ledger
↓
RPG projection grants Ember Moss
↓
Nexus herb vendor inventory updates
↓
Another player sees ember scarcity rise
↓
Ley Road faction offers movement covenant
```

This is the core architectural fantasy:
the world reacts to participation.

The player does not simply complete isolated tasks.
Their actions alter inventories, factions, prices, opportunities, rumors, rituals, and settlement conditions.

---

# Position Within the Ecosystem

## Pancakes

Pancakes is the human-facing life layer.

It contains:

* journals,
* rituals,
* schedules,
* self-reflection,
* household systems,
* wellness systems,
* relationship systems,
* and other non-game interfaces.

## Pitchfork

Pitchfork is the accounting and ledger substrate.

It manages:

* inventories,
* permissions,
* events,
* contracts,
* resources,
* balances,
* caps,
* covenants,
* and settlement logic.

## Nexus Roguelike

The Nexus is:

* a projection layer,
* a settlement simulation,
* a symbolic economy,
* and a social-exploration client.

It translates:

* ledgers into archives,
* inventories into vendors,
* contracts into covenants,
* and events into visible world-state.

---

# Thematic Identity

The Nexus should feel:

* mysterious,
* inhabited,
* procedural,
* ancient,
* practical,
* magical,
* economic,
* social,
* and slightly decayed.

The tone is not:

* heroic epic fantasy,
* grimdark warfare,
* or optimization-heavy strategy.

It is:

* exploratory,
* systems-rich,
* ritualistic,
* weirdly cozy,
* and infrastructural.

The player should feel:

> "This place exists because many lives and systems flow through it."

---

# The Nexus as a Settlement

The Nexus should begin as a dense roguelike town-space rather than a giant overworld.

The strongest early experience is:

* wandering,
* discovering,
* trading,
* overhearing,
* negotiating,
* restoring,
* crafting,
* and learning systems.

The world should feel closer to:

* Minetown,
* Bazaar districts,
* MUD guild hubs,
* and procedural settlements

than to:

* open-world survival games,
* raid MMOs,
* or Diablo-style dungeon crawlers.

---

# Spatial Structure

The Nexus is composed of districts.

Each district corresponds to:

* a domain,
* an economic layer,
* a faction,
* or a symbolic function.

Districts may shift over time as the ecosystem evolves.

## Core Districts

### The Bazaar

The economic heart of the Nexus.

Contains:

* vendors,
* traders,
* commodity shrines,
* wandering merchants,
* recipe exchanges,
* bulletin boards,
* and market rumors.

The Bazaar reflects:

* inventories,
* scarcity,
* crafting demand,
* and player activity.

If many players generate Ember Moss:

* prices fall,
* recipes change,
* and herbalists adapt.

If Dream Resin becomes scarce:

* dream rituals become expensive,
* and factions react.

---

### The Contract Hall

The center of covenants and agreements.

Contains:

* covenant boards,
* witness chambers,
* escrow vaults,
* faction requests,
* public works,
* and sealed rituals.

Players may:

* accept contracts,
* issue contracts,
* inspect settlements,
* view reputation,
* or negotiate terms.

The Hall is where:

* smart-contract ideas,
* escrow,
* settlement,
* and accountability

become spatial gameplay.

---

### The Ledger Archive

A massive procedural library and record-hall.

Contains:

* event history,
* covenant records,
* faction treaties,
* world-state summaries,
* player histories,
* and strange forgotten entries.

The Archive acts as:

* audit layer,
* lore engine,
* and historical memory.

The Ledger Archive should feel:

* infinite,
* bureaucratic,
* magical,
* and partially broken.

Some records may:

* contradict,
* decay,
* fork,
* or become corrupted.

---

### The Mentor Wings

A district of schools, halls, gardens, and ritual chambers.

Mentors:

* teach systems,
* unlock recipes,
* interpret events,
* and offer guidance.

Mentors are not just quest-givers.
They are:

* domain interpreters,
* economists,
* ritual theorists,
* historians,
* and witnesses.

---

### Sanctuary District

A partially residential area.

Contains:

* player sanctuaries,
* workshops,
* gardens,
* storage,
* and attunement spaces.

Sanctuaries are:

* projections of identity,
* ritual spaces,
* and long-term progression anchors.

They should feel:

* personal,
* evolving,
* and persistent.

---

### The Veil Market

A strange semi-illegal district.

Contains:

* unstable vendors,
* black-market contracts,
* rare commodities,
* experimental rituals,
* and dangerous conversions.

This area introduces:

* arbitrage,
* instability,
* exploits,
* corruption,
* and economic ethics.

---

### The Ley Gates

Transition points between clients and systems.

Examples:

* walking client,
* journaling client,
* Minecraft-like client,
* Doom client,
* browser RPG,
* cooperative ritual spaces.

The Gates are literalized APIs.

Different clients are interpreted as:

* realms,
* provinces,
* dreamspaces,
* or attunement domains.

---

# Gameplay Structure

The Nexus should initially be:

* turn-based,
* grid-based,
* lightweight,
* and low-friction.

The ideal interaction loop:

```text
wander
→ inspect
→ converse
→ trade
→ craft
→ accept covenant
→ discover rumor
→ alter inventory
→ affect world-state
→ return later to see changes
```

This is closer to:

* classic roguelikes,
* MUD social spaces,
* and simulation hubs

than action combat games.

---

# Core Gameplay Systems

## Wandering

Movement should matter.

Players discover:

* rumors,
* hidden rooms,
* wandering vendors,
* procedural encounters,
* faction emissaries,
* and temporal anomalies.

The town should feel:

* alive,
* partially procedural,
* and socially reactive.

---

## Vendors

Vendors are central.

The player fantasy is:

* wandering through weird shops,
* discovering impossible goods,
* and learning systems through trade.

Vendor inventories should react to:

* ecosystem activity,
* player behavior,
* scarcity,
* faction influence,
* and seasonal events.

Examples:

* a herbalist sells Ember Moss after movement surges,
* a dream vendor appears during high rest participation,
* a ledger broker appears after covenant activity spikes.

Vendors are projections of platform behavior.

---

## Contracts and Covenants

Contracts become physical social objects.

Players can:

* browse,
* negotiate,
* settle,
* witness,
* and archive agreements.

Examples:

* restore a sanctuary district,
* gather movement resources,
* contribute study materials,
* fund a guild ritual,
* stabilize a corrupted archive wing.

Contracts can be:

* personal,
* cooperative,
* factional,
* seasonal,
* or procedural.

---

## Exploration

The Nexus is not static.

Possible dynamic systems:

* shifting rooms,
* temporary markets,
* hidden archives,
* unstable gates,
* rotating factions,
* seasonal districts,
* procedural ruins,
* and event-generated structures.

The Nexus should feel:

* layered,
* old,
* and constantly adapting.

---

## Crafting

Crafting transforms:

* materials,
* essences,
* contracts,
* and relics

into:

* wards,
* ritual tools,
* sanctuary upgrades,
* social artifacts,
* and economic instruments.

Crafting should feel:

* symbolic,
* infrastructural,
* and material.

---

# Multi-Client Integration

The Nexus is where multi-client interaction becomes visible.

## Example Client Types

### Pancakes Core

Produces:

* rituals,
* journaling events,
* schedules,
* reflections,
* and household systems.

Nexus interpretation:

* resources,
* district stability,
* sanctuary upgrades,
* social resonance.

---

### Pitchfork RPG

Produces:

* crafting,
* combat,
* exploration,
* inventory,
* and covenant events.

Nexus interpretation:

* faction reputation,
* vendor stock,
* relic circulation,
* and guild opportunities.

---

### Realtime Clients

Examples:

* Minecraft-like worlds,
* Doom-like clients,
* shared ritual spaces,
* walking maps.

These produce:

* session summaries,
* achievements,
* environmental interactions,
* and social presence.

The Nexus reflects:

* migration,
* seasonal surges,
* and infrastructural changes.

---

### Journal Clients

Examples:

* Redwitch,
* reflection clients,
* dream logs,
* mood systems.

These should affect the Nexus carefully and permissionedly.

Examples:

* dream districts become more active,
* moon rituals appear,
* certain vendors arrive,
* reflective factions gain influence.

Sensitive data should never become public by default.

---

# Architectural Model

The Nexus should be projection-driven.

## Core Structure

```text
Clients
↓
Platform events
↓
Pitchfork accounting layer
↓
Ledger/event stream
↓
Nexus projections
↓
Settlement state
```

The Nexus should never own the source of truth.

It visualizes and spatializes:

* accounting state,
* inventories,
* faction pressure,
* covenant activity,
* and symbolic economies.

---

# Event Projection Examples

## Movement Example

```text
Player logs a walk in Pancakes
↓
Movement event enters ledger
↓
RPG projection grants Ember Moss
↓
Nexus herb vendor inventory updates
↓
Another player sees ember scarcity rise
↓
Ley Road faction offers movement covenant
```

---

## Study Example

```text
Study session completed
↓
Ledger records intellectual activity
↓
Rune Fragments generated
↓
Scholar district archives expand
↓
New codex pages appear
↓
Mentor offers advanced research covenant
```

---

## Household Example

```text
Household ritual completed
↓
Order Salt generated
↓
Sanctuary district stability improves
↓
Repair vendors lower prices
↓
Stonebound faction influence rises
```

---

# Realtime vs Turn-Based Clients

The Nexus itself should remain mostly:

* turn-based,
* asynchronous,
* and settlement-oriented.

Realtime clients should:

* generate events,
* not dominate the platform architecture.

Important principle:

```text
Realtime simulation is local.
Settlement and accounting are global.
```

Realtime clients should emit:

* summaries,
* session settlements,
* and bounded economic effects.

Not:

* every frame,
* movement packet,
* or combat tick.

---

# Social Structure

The Nexus should support:

* passive coexistence,
* asynchronous presence,
* and light social interaction.

Not mandatory realtime coordination.

Possible systems:

* bulletin boards,
* covenant boards,
* guild halls,
* asynchronous gifting,
* public works,
* shared rituals,
* reputation trails,
* and cooperative restoration projects.

---

# Factions

Factions should represent:

* philosophies,
* domains,
* and economic tendencies.

Examples:

## Ley Road Fellowship

Movement, wandering, exploration, vitality.

## Stonebound

Maintenance, order, stewardship, stability.

## Dream Choir

Rest, dreams, reflection, emotional resonance.

## Clockwork Synod

Planning, coordination, scheduling, governance.

## Ledgerbound

Contracts, archives, accounting, settlement.

## Verdant Tide

Food, care, nourishment, growth.

Factions should react dynamically to:

* participation patterns,
* resource scarcity,
* covenant completion,
* and world-state shifts.

---

# Procedural Systems

The Nexus should heavily use procedural systems.

Examples:

* procedural vendors,
* rumors,
* contracts,
* district events,
* archive records,
* relic descriptions,
* and wandering NPCs.

This allows:

* massive depth,
* replayability,
* and emergent storytelling

without requiring huge handcrafted worlds.

---

# Interface Style

The ideal early implementation is:

* ASCII,
* tiles,
* browser grid,
* or lightweight terminal rendering.

The Nexus should feel:

* readable,
* dense,
* and systemic.

Example:

```text
#################
#....V......L...#
#..###..........#
#..#.@....M.....#
#......C........#
#################
```

Legend:

* @ = player
* V = vendor
* L = ledger archive
* M = mentor
* C = covenant hall

This is enough to create:

* atmosphere,
* exploration,
* and systems-rich interaction.

---

# Economy Philosophy

The Nexus economy should prioritize:

* symbolic value,
* crafting,
* social meaning,
* and participation

over:

* grinding,
* extraction,
* or optimization.

Important principles:

* caps,
* soulbound progression,
* privacy,
* non-extractive systems,
* and cooperative structures.

The economy should feel:

* inhabited,
* ritualistic,
* and civic.

Not like a spreadsheet casino.

---

# MVP Recommendation

The first playable Nexus should include:

1. Small grid-based settlement.
2. One vendor district.
3. One mentor hall.
4. One covenant board.
5. Simple inventory.
6. Ledger event feed.
7. Procedural rumors.
8. Sanctuary room.
9. Ember Moss resource loop.
10. One faction system.
11. Event-driven vendor inventory updates.

The MVP should prove:

```text
platform event
→ accounting layer
→ world projection
→ social/economic consequence
```

If that loop feels alive,
the Nexus works.

---

# Long-Term Vision

The Nexus eventually becomes:

* a shared symbolic civilization,
* a settlement-space for many clients,
* a cooperative infrastructure layer,
* and a social-economic projection of lived activity.

The player is not simply leveling a character.

They are:

* contributing to a world,
* shaping symbolic economies,
* altering settlement conditions,
* supporting factions,
* restoring districts,
* and participating in a civilization built from ordinary life.

The Nexus is where:

* rituals become infrastructure,
* inventories become economies,
* contracts become governance,
* and private life becomes visible symbolic participation without becoming exploitative surveillance.

That is the core fantasy of the Nexus.
