# Pitchfork System Overview

## Purpose

This document gives an architectural overview of the Pancakes/Pitchfork system.

It is not a product pitch, gameplay specification, economic policy, or lore document. It is the system map: the major layers, their responsibilities, how data moves between them, where identity and permission boundaries live, and how different clients can share one coherent substrate without collapsing into one monolithic app.

The core system goal is:

```text
ordinary life
-> consented records
-> symbolic accounting
-> humane interfaces
-> cooperative and ecological world-state
```

The system should recognize care, rhythm, rest, study, household work, movement, reflection, creativity, service, and covenantal participation without turning human life into extractable behavioral labor.

Pitchfork and Pancakes should support:

- Human dignity.
- Local ownership.
- Consent-based participation.
- Symbolic interpretation.
- Cooperative value.
- Strong privacy boundaries.
- Optional fantasy and game layers.
- Future economic and crypto rails without forcing them into the early product.

## One-Sentence Summary

Pancakes is the human-facing life system, Pitchfork is the accounting and covenant substrate, and clients such as the RPG, Nexus, Redwitch, ambient worlds, and cooperative tools interpret permissioned events through different humane, symbolic, and practical interfaces.

---

# Core Architecture

The system is best understood as a layered architecture.

```text
People, households, guilds, communities
↓
Pancakes clients and domain apps
↓
Pancakes Identity and node policy
↓
Pitchfork accounting substrate
↓
Ledgers, inventories, covenants, permissions, projections
↓
Client-specific experiences
```

No single client should own the entire system.

Pancakes is the human layer.
Pitchfork is the accounting layer.
Clients are interfaces.
Nodes are deployment and governance boundaries.
Identity is a shared abstraction governed by node policy.

## Layer Responsibilities

| Layer | Primary Responsibility |
| --- | --- |
| Pancakes | Human-facing life, rituals, journals, schedules, care, household systems, service exchange, and privacy surfaces |
| Pancakes Identity | Accounts, keys, identity claims, membership, consent, permissions, and node-level identity enforcement |
| Pitchfork | Events, ledgers, inventories, resources, contracts, covenants, caps, balances, permissions, settlement logic, and future crypto-facing state |
| Clients | Domain-specific interfaces over Pancakes and Pitchfork state |
| Nexus | Shared roguelike settlement and projection layer for platform state |
| Ambient clients | Symbolic environmental projections of permissioned life state |
| Nodes | Local or hosted governance, storage, policy, backups, exports, and data stewardship |

---

# Pancakes

Pancakes is the broad human-facing life system.

It owns the ordinary-life product surface:

- Ritual logging.
- Journaling.
- Reflection.
- Schedules.
- Rest.
- Movement.
- Food and nourishment.
- Study.
- Household work.
- Caregiving.
- Relationship maintenance.
- Local service exchange.
- Household and community coordination.
- Privacy and consent controls.

Pancakes should be understandable without fantasy, crypto, markets, or game mechanics.

A user should be able to use Pancakes as a humane life app even if they never enter the RPG client, Nexus, Minecraft-like symbolic world, Redwitch, or any blockchain-connected environment.

## Pancakes Design Principle

Pancakes should not say:

```text
Optimize your behavior for maximum yield.
```

It should say:

```text
Your life contains forms of care, rhythm, and contribution worth recognizing.
```

Pancakes is the layer where users understand what is being recorded, what is private, what is shared, and what a given action means in ordinary human terms.

---

# Pitchfork

Pitchfork is the accounting substrate.

It provides durable primitives for:

- Events.
- Ledgers.
- Inventories.
- Materials.
- Essences.
- Crafted items.
- Contracts.
- Covenants.
- Permissions.
- Balances.
- Caps.
- Settlement.
- Cooperative pools.
- Reputation or trust where appropriate.
- Future crypto rails.

Pitchfork should not know every detail of every client. It should know enough to account for meaningful events, enforce limits, preserve history, resolve permissions, and expose stable primitives.

## Pitchfork Design Principle

Pitchfork should sit below experience.

The same underlying event may appear differently across clients:

| Layer | Interpretation |
| --- | --- |
| Pancakes | "You logged a walk." |
| Pitchfork RPG | "Your walk gathered Ember Moss from the ley road." |
| Nexus | "Ley Road vendor stock increased." |
| Ambient client | "Paths have begun appearing through the grass." |
| Ledger | A permissioned movement event was recorded and settled under caps |

The accounting should remain coherent even when client interpretations differ.

## What Pitchfork Should Avoid

Pitchfork must not become:

- A universal surveillance database.
- A productivity scoring engine.
- A direct "behavior to money" system.
- A health-data speculation layer.
- A mechanism for guilds or groups to pressure intimate disclosure.
- A crypto abstraction that leaks wallet logic into every client.

Pitchfork should store what is needed for explicit user-facing value, auditability, covenant settlement, inventory consistency, and future portability.

---

# Pancakes Identity

Pancakes Identity is the shared identity abstraction for the ecosystem.

It should handle:

- Accounts.
- Keys.
- Local identities.
- Pseudonymous identities.
- Verified claims.
- Membership.
- Consent grants.
- Permission scopes.
- Export authority.
- Covenant signing.
- Node access.
- Role-based access where needed.

Identity should be pluggable and node-governed.

Pitchfork should consume identity claims and permission decisions, but it should not dictate one global identity authority.

## Node-Governed Identity

Each Pancakes node decides how it wants to enforce identity.

Built-in identity enforcement methods should include:

- GPG-based identity.
- Ontario Digital ID Program integration.

Additional methods may be added later, but these two establish the initial range:

| Method | Best Fit |
| --- | --- |
| Local account | Personal nodes, early development, low-risk household use |
| GPG identity | Self-hosted nodes, technical users, pseudonymous continuity, signed exports, covenant witnessing |
| Ontario Digital ID Program | Higher-assurance identity, institutional nodes, cooperative pools, grants, legal workflows, or real-world eligibility checks |

## Identity Boundary Principle

Pitchfork should record actions against identities, but identity enforcement belongs to the node.

```text
Node identity method
-> verified account/key/claim
-> permission grant
-> Pitchfork event or covenant
-> ledger record
```

This keeps the system flexible enough for:

- Personal use.
- Households.
- Guilds.
- Cooperatives.
- Clinics.
- Schools.
- Mutual-aid groups.
- Pseudonymous game communities.
- High-trust institutional contexts.

---

# Pancakes Nodes

A Pancakes node is a deployment and governance boundary.

It may be:

- Personal.
- Household.
- Guild-based.
- Cooperative.
- Institutional.
- Hosted.
- Self-hosted.

Nodes allow groups to retain control over:

- Personal logs.
- Household records.
- Ritual history.
- Inventories.
- Covenants.
- Cooperative pools.
- Membership.
- Permissions.
- Local policy.
- Backups.
- Exports.
- Whether data leaves the node.

## Node Types

| Node Type | Purpose |
| --- | --- |
| Personal node | Local-first personal archive and ritual history |
| Household node | Shared care, chores, household rituals, and private family or chosen-family records |
| Guild node | Shared rituals, guild vaults, cooperative restoration, covenants, and optional federation |
| Institutional node | Role-based access, audit trails, policy enforcement, and strict privacy controls |
| Hosted node | Convenient public entry point for users who cannot or do not want to self-host |

## Hosted Domains

The likely hosted shape is:

| Domain | Role |
| --- | --- |
| `pancakes.ca` | Stable public app, non-crypto by default, human-facing Pancakes experience |
| `pancakes.love` | Experimental environment for cooperative, RPG, blockchain-connected, or relational prototypes |

Hosted Pancakes should be useful, but not mandatory.

The long-term architecture should allow hosted Pancakes to become one node among many, not the unavoidable center of the network.

## Community Data Stewardship

Pancakes nodes should support community data stewardship.

A node may operate socially or legally as:

- A household server.
- A data cooperative.
- A civic data trust.
- A data commons.
- A community-run digital home.
- A local institutional system.

The default principle is:

```text
Raw personal logs stay private unless explicitly shared.
```

Derived state can sometimes be shared more safely, but even derived state can reveal patterns. Sharing should be intentional, scoped, and reversible where possible.

---

# Events And Data Flow

The core data flow is:

```text
real-world action
-> client record
-> permission check
-> Pitchfork event
-> accounting settlement
-> derived state
-> client-specific projection
```

Example:

```text
Player logs a walk in Pancakes
↓
Node identity and permission policy approves the event
↓
Pitchfork records a movement event
↓
Daily movement cap is applied
↓
Ember Moss is generated
↓
RPG inventory updates
↓
Nexus herb vendor inventory shifts
↓
Ambient world grows new paths
```

## Event Model

The early event model should support:

- Actor identity.
- Node identity.
- Client source.
- Event type.
- Timestamp.
- Permission scope.
- Sensitive-data classification.
- Self-attestation or verification method.
- Derived resources.
- Cap settlement.
- Audit trail.

The system should distinguish:

- Raw personal event.
- Sanitized derived event.
- Shareable symbolic projection.
- Economic settlement.
- Public or group-visible state.

## Raw Events vs Derived State

Raw events may include intimate context.

Derived state should reveal less.

Example:

| Raw or Sensitive State | Safer Derived Projection |
| --- | --- |
| Menstrual cycle phase | Red moon in a private or trusted symbolic world |
| Mood reflection | Dream district activity |
| Household chore | Order Salt contribution |
| Sleep difficulty | Storms near the sanctuary |
| Caregiving pattern | Hearthlight generated |

The system should prefer symbolic, ambiguous, and permissioned projections over explicit metrics.

---

# Client Taxonomy

The ecosystem may contain many clients.

Clients should not duplicate the accounting substrate. They should produce events, request permissions, display derived state, and provide domain-specific experiences.

| Client Type | Purpose |
| --- | --- |
| Human clients | Journals, rituals, schedules, dashboards, reflection, household tools |
| RPG clients | Gathering, crafting, mentors, sanctuaries, recipes, magical progression |
| Nexus roguelike | Shared settlement, vendors, factions, covenants, ledgers, guild halls |
| Ambient symbolic clients | Weather, ecology, symbolic worlds, companion systems, emotional landscapes |
| Realtime clients | Minecraft-like worlds, local simulations, shared spaces, session-based events |
| Journal or health-adjacent clients | Redwitch, dream logs, mood, cycle, reflection, symptom-aware systems |
| Cooperative clients | Guilds, shared rituals, service exchange, pools, mutual aid, household covenants |
| Administrative clients | Governance, ledgers, exports, permissions, role management, audits |

## Client Boundary Principle

Clients interpret.

Pitchfork accounts.

Nodes govern.

Identity authorizes.

Pancakes humanizes.

---

# Pitchfork RPG Client

The Pitchfork RPG client is a life-powered fantasy RPG interface over Pitchfork.

It turns ordinary real-world activity into magical gathering, crafting, sanctuary restoration, mentors, rituals, and symbolic progression.

It should begin as:

- Single-player.
- Browser-based.
- Text-heavy.
- Low-friction.
- Crafting-oriented.
- Sanctuary-centered.
- Non-crypto by default.

The first emotional loop is:

```text
I did something meaningful in real life.
The game interpreted it mythically.
I gathered a magical resource.
I used that resource to craft, restore, or unlock something.
My life felt connected to a world.
```

## RPG Role In The Architecture

The RPG client is not the whole platform.

It is one optional interface for people who want a magical, game-like interpretation of Pitchfork accounting.

Example mappings:

| Real-World Domain | RPG Resource |
| --- | --- |
| Movement | Ember Moss, Road Dust |
| Rest | Lucid Dew, Stillwater |
| Household | Order Salt, Steward's Wax |
| Study | Rune Fragments, Memory Ink |
| Care | Hearthlight |
| Reflection | Dream Resin |

The RPG client can teach deeper concepts like contracts, escrow, staking, reputation, and ledgers through fantasy-native systems such as covenants, sealed rituals, mana attunement, renown, and codices.

---

# The Nexus

The Nexus is the shared roguelike settlement and projection layer.

It is not the whole game world.
It is not a combat MMO.
It is not a giant realtime overworld.

The Nexus is where systems meet.

It spatializes:

- Ledgers.
- Inventories.
- Vendors.
- Contracts.
- Covenants.
- Guild halls.
- Factions.
- Archives.
- Sanctuaries.
- Markets.
- Rumors.
- Procedural social state.

## Nexus Architectural Role

The Nexus should be projection-driven.

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

It visualizes and spatializes accounting state, inventories, faction pressure, covenant activity, and symbolic economies.

## Nexus Example

```text
Many users log movement rituals
↓
Movement events settle in Pitchfork
↓
Ember Moss supply increases
↓
Ley Road faction influence rises
↓
Nexus herb vendors change prices
↓
Road districts grow busier
↓
Movement covenants become more common
```

## Nexus MVP

The first playable Nexus should prove:

```text
platform event
-> accounting layer
-> world projection
-> social/economic consequence
```

An early MVP can include:

- Small grid-based settlement.
- One vendor district.
- One mentor hall.
- One covenant board.
- Simple inventory.
- Ledger event feed.
- Procedural rumors.
- Sanctuary room.
- Ember Moss resource loop.
- One faction system.
- Event-driven vendor inventory updates.

---

# Ambient Symbolic Clients

Ambient symbolic clients are environments that respond symbolically to permissioned life state.

They are not dashboards.
They are not optimization systems.
They are not metric displays.

They are:

- Symbolic environments.
- Emotional landscapes.
- Ambient world projections.
- Ecological reflections of lived experience.

Their core flow is:

```text
private embodied state
-> permissioned symbolic projection
-> environmental response
```

Not:

```text
private embodied state
-> exposed metrics
-> social optimization pressure
```

## Ambient Projection Examples

| Human Pattern | Environmental Projection |
| --- | --- |
| Walking | Paths emerge |
| Rest | Storms calm |
| Study | Libraries expand |
| Caregiving | Sanctuaries strengthen |
| Reflection | Dream wells deepen |
| Burnout | Environmental decay |
| Joy | Wildlife gathers |
| Community | Festivals emerge |
| Recovery | Gardens regrow |
| Stress | Skies darken |
| Stability | Hearths glow steadily |

## Minecraft-Like Clients

Minecraft-like clients are well-suited to ambient projection because they already support:

- Weather.
- Moon phases.
- Creatures.
- Lighting.
- Particles.
- Ambient sound.
- Biomes.
- Procedural terrain.
- Structures.
- Passive entities.

These clients should not render private metrics.

They should transform permissioned state into symbolic ecology:

```text
Redwitch detects a sensitive cycle-related state
↓
User permits symbolic projection
↓
Pitchfork emits a bounded derived event
↓
Ambient client receives world modifier
↓
Moon appears crimson
↓
No explicit reproductive or medical status is exposed
```

The world should feel responsive without becoming diagnostic.

---

# Redwitch And Sensitive Clients

Redwitch is a possible specialized Pancakes client for menstrual cycles, fertility awareness, symptoms, mood, energy, body rhythms, and related reflection.

It has a higher privacy burden than ordinary RPG features.

Sensitive data includes:

- Menstrual cycles.
- Fertility.
- Sexual health.
- Pregnancy-related data.
- Symptoms.
- Mood.
- Mental health.
- Sleep.
- Trauma-adjacent reflection.
- Household or caregiving patterns.

Redwitch should participate in the broader ecosystem only through careful permissioning and symbolic abstraction.

It should never expose explicit reproductive status, health details, or intimate metrics to other players, guilds, public worlds, markets, or economic systems by default.

## Sensitive Client Principle

Sensitive clients may emit:

- Private personal records.
- Local-only projections.
- Trusted-participant projections.
- Aggregated or generalized resonance.
- Symbolic environmental modifiers.

They should not emit:

- Public explicit health state.
- Marketable intimate data.
- Guild-visible fertility or mood labels.
- High-value rewards for sensitive disclosures.
- Raw health data into shared ledgers by default.

---

# Economics

Pitchfork's early economy should be:

- Symbolic.
- Internal.
- Capped.
- Non-speculative.
- Privacy-preserving.
- Resistant to farming.
- Built around crafting and contribution rather than raw behavior extraction.

The system should not begin as a real-money earning app.

## Economic Layers

| Layer | Meaning |
| --- | --- |
| Raw materials | Capped symbolic resources generated by rituals |
| Essences | Refined resources used in crafting, covenants, and later economic systems |
| Crafted items | Meaningful outputs created through recipes and choices |
| Soulbound achievements | Non-tradable identity, recovery, sanctuary, or trust milestones |
| Covenants | Structured commitments, escrow-like agreements, and settlement logic |
| Cooperative pools | Shared treasuries or resource stores for mutual support |

## Economic Boundary Principle

Pitchfork should avoid:

- Infinite per-action rewards.
- Direct conversion from steps or chores to money.
- Public leaderboards based on raw output.
- Rewards that pressure users to disclose sensitive health or household data.
- Tradable raw participation materials in early versions.
- Speculative markets before the symbolic economy is healthy.

The safest base is capped participation:

```text
basic participation
-> baseline reward access
-> reduced pressure
```

Not:

```text
more tracking
-> more yield
-> more pressure
-> more extraction
```

## Crypto Position

Crypto, if added, belongs behind Pitchfork.

Clients should not each invent wallet, token, marketplace, contract, or ledger logic.

Pitchfork should decide whether an accounting operation is:

- Internal.
- Symbolic.
- Database-backed.
- Node-local.
- Federated.
- Blockchain-backed.

Fantasy-native mappings can teach crypto concepts later:

| Technical Concept | In-World Concept |
| --- | --- |
| Wallet | Soul sigil |
| Private key | True name |
| Token | Essence, shard, sigil |
| Smart contract | Binding covenant |
| Escrow | Sealed ritual |
| Staking | Mana attunement |
| Validator | Rune keeper |
| Oracle | Omen, witness, scrying mirror |
| Ledger | Codex, Nexus record |
| DAO | Mage council, guild order |
| Treasury | Guild vault |

The early product should not expose crypto terminology to ordinary users.

---

# Permissions And Privacy

Privacy is not a feature added later.

Privacy is a system boundary.

The architecture should distinguish:

- Private personal data.
- Household-shared data.
- Guild-shared data.
- Node-local data.
- Public or published data.
- Economic or treasury data.
- Sensitive health or cycle data.
- Wallet or crypto-facing data.

## Permission Scopes

A useful early permission model should include:

| Scope | Meaning |
| --- | --- |
| Private | Visible only to the person |
| Local client | Used only inside the originating client |
| Node-local | Available inside the node under policy |
| Household | Shared with household participants |
| Guild | Shared with guild or cooperative group |
| Trusted participants | Shared with specifically approved people |
| Public symbolic | Published only as symbolic or aggregated projection |
| Economic settlement | Used for covenant or pool settlement under explicit terms |

## Privacy Design Principle

The system should prefer:

```text
permissioned derived state
```

over:

```text
raw personal disclosure
```

Example:

```text
Private state: User is exhausted.
Derived symbolic state: Sanctuary storms have intensified.
Economic state: No tradable reward.
Public state: None unless explicitly allowed.
```

This preserves dignity, ambiguity, and safety.

---

# Contracts, Covenants, And Cooperative Systems

Contracts and covenants are central to Pitchfork's long-term role.

They can model:

- Plans.
- Promises.
- Household agreements.
- Guild work.
- Mutual aid.
- Escrow.
- Settlement.
- Witnessing.
- Reputation.
- Cooperative pools.
- Public works.
- Grants.
- Shared rituals.

In human-facing Pancakes, a covenant may look like:

```text
We agree to maintain the shared kitchen schedule this week.
```

In the RPG client, it may look like:

```text
Bind a hearth covenant to restore the Sanctuary threshold.
```

In the Nexus, it may appear as:

```text
A sealed ritual posted on the Contract Hall board.
```

In Pitchfork, it is:

```text
an agreement with participants, permissions, conditions, locked value, witnesses, settlement rules, and history
```

## Cooperative Pools

Cooperative pools are the most promising path toward real social value.

They can support:

- Mutual aid.
- Emergency funds.
- Escape grants.
- Childcare support.
- Household support.
- Education support.
- Community projects.
- Guild infrastructure.

Real economic value should emerge through cooperative structures and explicit governance, not through pay-per-behavior mechanics.

---

# Realtime Systems

Realtime clients may exist, but they should not dominate the platform architecture.

Examples:

- Minecraft-like symbolic worlds.
- Shared ritual spaces.
- Walking maps.
- Doom-like experimental clients.
- Local simulations.

Important principle:

```text
Realtime simulation is local.
Settlement and accounting are global.
```

Realtime clients should emit:

- Session summaries.
- Bounded achievements.
- Environmental interactions.
- Social presence events.
- Settlement requests.

They should not emit:

- Every frame.
- Every movement packet.
- Every combat tick.
- Unbounded economic rewards.
- Raw sensitive telemetry by default.

---

# Administrative And Governance Surfaces

The system needs administrative clients and governance surfaces, especially for nodes.

These should answer:

- Who owns the node?
- Who administers the server?
- Who can add or remove members?
- Who can see personal data?
- Who can see aggregate data?
- Who can approve covenants?
- Who can manage cooperative pools?
- Who can export data?
- Who can delete data?
- What happens if the group dissolves?
- How can a person leave with their own records?
- Which identity methods does the node accept?
- Which events may be shared outside the node?

For trust-like nodes, the system should distinguish:

- Members.
- Stewards.
- Custodians.
- Beneficiaries.

One person may hold multiple roles in a small node, but the concepts should remain separate.

---

# Technical Shape

The early technical architecture should stay simple.

The current working assumption is:

- Pitchfork starts as a Python accounting module.
- Pancakes clients can be Flask/Gunicorn web apps.
- Pitchfork RPG can import Pitchfork primitives directly.
- Redwitch can use Pancakes Identity and selected Pitchfork primitives.
- Nexus can begin as a browser or terminal-style grid client over local Pitchfork state.
- Nodes can initially be standalone deployments without federation.

This does not require premature microservices.

## Evolution Path

Pitchfork may later become:

- A service.
- A local daemon.
- A node-local API.
- A federated accounting layer.
- A blockchain bridge.

But early development should optimize for:

- Coherent user experience.
- Fast iteration.
- Clear data boundaries.
- Stable event and permission models.
- Small end-to-end loops.

---

# Minimum Coherent System

The first integration win should be small.

```text
One real-life event
-> one Pitchfork accounting record
-> one Pancakes human view
-> one RPG interpretation
-> one Nexus projection
-> one ambient projection
```

Example:

```text
User logs a walk
↓
Pancakes shows the human record
↓
Pitchfork records and caps the movement event
↓
RPG grants Ember Moss
↓
Nexus updates herb vendor stock
↓
Ambient client grows paths or changes wildlife behavior
```

This proves the architecture without requiring the whole platform.

## Early Build Sequence

A pragmatic sequence:

1. Stabilize Pitchfork as a Python accounting module.
2. Define a small event model for self-attested life activity.
3. Add identity and permission abstractions that can be governed by nodes.
4. Implement local account and GPG identity support first.
5. Keep Ontario Digital ID Program as a built-in high-assurance identity target.
6. Build one simple Pancakes human-facing flow.
7. Build one RPG interpretation of the same event.
8. Add persistence, caps, and inventory.
9. Add one simple Nexus projection.
10. Add one ambient symbolic projection.
11. Add node export/import and backup surfaces.
12. Only then decide whether Pitchfork needs to become a separate service.

---

# System Principles

## Human Layer First

Pancakes must remain useful and understandable without fantasy, crypto, markets, or speculative economics.

## Accounting Below Experience

Pitchfork should keep events, permissions, caps, inventories, covenants, and ledgers coherent across clients.

## Identity Is Node-Governed

Nodes choose how identity is enforced. Pitchfork consumes verified identity claims but does not impose one global identity authority.

## Privacy By Boundary

Raw personal logs are private by default. Sensitive data requires explicit permission and symbolic abstraction before it influences shared systems.

## Symbolic Before Financial

The first economy should be symbolic, capped, and non-speculative.

## Crafting Before Markets

Value should arise from meaning, recipes, contribution, taste, and use before exchange or speculation.

## Rest Is Valid Participation

The system should recognize rest, recovery, low-capacity participation, and care without punishing users for not maximizing output.

## Fantasy Is Optional

The RPG and Nexus layers can be rich and magical, but Pancakes should not require the fantasy frame.

## Realtime Is Bounded

Realtime clients may generate events, but accounting should settle bounded summaries rather than raw streams.

## Nodes Preserve Exit Rights

People and communities should be able to export, leave, self-host, back up, and govern their data.

## Crypto Is Behind Pitchfork

Blockchain integration, if added, should be mediated by Pitchfork and hidden from ordinary clients until needed.

---

# Open Architectural Questions

- Does Pancakes Identity become its own package, or does it begin inside the Pancakes codebase?
- What is the minimum event schema that can support Pancakes, RPG, Nexus, and ambient projections?
- How should node-local identity claims be represented so GPG and Ontario Digital ID Program methods can both fit?
- Which data belongs in Pitchfork versus Pancakes Core?
- Should Pitchfork own its own database early, or should the first clients share storage?
- What is the boundary between an event, a resource grant, a projection, and a settlement?
- How should sensitive Redwitch-derived projections be represented without leaking health data?
- What is the first covenant format?
- What is the first export format for a personal or household node?
- When does federation become necessary?
- What is the smallest useful administrative surface for node governance?
- Which client should prove the first multi-client loop: RPG plus Nexus, or Pancakes plus ambient projection?

---

# Working Assumption

For now, the system should be built as a simple local architecture:

```text
Pancakes web client
Pitchfork Python module
Pancakes Identity abstraction
local persistence
one RPG interpretation
one Nexus projection
one ambient projection
```

This keeps the system small enough to build while preserving the long-term architecture:

```text
many clients
many nodes
shared accounting primitives
node-governed identity
permissioned projections
cooperative infrastructure
optional crypto rails
```

The system succeeds when ordinary life can become meaningful, private, symbolic, and cooperative without becoming surveillance, extraction, or speculative labor.
