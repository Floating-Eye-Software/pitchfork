# RPG Client Architecture

## Purpose

This document is the canonical technical boundary for the Pitchfork RPG.

The RPG is one client and projection of the wider Pancakes and Pitchfork
ecosystem. It is not the source of truth for real-world activity, identity,
permissions, settlement, or physical persistence.

The governing flow is:

```text
life or game activity
→ Pancakes client and node
→ source event
→ Pitchfork validation and settlement
→ permissioned projection
→ RPG interpretation
```

The same settled event may support several authorized projections without
duplicating the underlying truth.

## Ownership Boundaries

Pitchfork owns:

* shared domain contracts,
* accounting and settlement semantics,
* resource-state transitions,
* projection derivation,
* and database-independent persistence interfaces.

Pancakes owns:

* applications and nodes,
* identity and profiles,
* authentication and permissions,
* physical databases and migrations,
* governance,
* and Pancakes product behavior.

The RPG owns:

* symbolic interpretation,
* game rules and progression,
* world presentation,
* quests, encounters, and client-local interaction,
* and RPG-specific projections.

Deployment belongs to `site-ops`; organization-wide coordination belongs to
`fley-org`; controlled research, privacy, health, safety, and regulatory review
belong to `fley-qms`.

## Event And Settlement Boundary

A source event is a client's claim that something occurred. Pitchfork applies
the relevant contract, validates the claim, and produces accepted or rejected
settlement outcomes. Projections derive views from accepted history.

```text
source claim
→ validate authority, contract, and limits
→ settle resource and obligation transitions
→ append durable outcome
→ derive authorized projections
```

The RPG must not grant shared resources merely because a screen displayed an
animation or a client reported local success. Shared effects require a
Pitchfork settlement outcome.

Projection state is rebuildable. It is not a second source of truth.

## Client Categories

### Discrete Clients

Browser RPG, crafting, sanctuary, and covenant clients produce bounded actions
such as completing a ritual, crafting an item, restoring a room, or accepting a
contract. They are the simplest initial integration.

### Real-Time Clients

Graphical worlds and live group experiences may maintain high-frequency local
state. Frames, positions, and transient interactions remain local. Only
meaningful summaries cross the settlement boundary.

```text
real-time session
→ local movement and interaction
→ session summary
→ Pitchfork settlement
→ durable shared effect
```

Real-time state is ephemeral; shared accounting is settled.

### Reflective And Sensitive Clients

Journal, health, household, and other reflective clients may handle private or
sensitive information. Their raw records do not belong in RPG projections.
They may produce a minimal symbolic claim only with explicit authority and
purpose limitation.

Sensitive participation must never be required for ordinary RPG access.

## Privacy Rules

The architecture follows these constraints:

* minimize data before it crosses a client boundary;
* default sensitive claims and projections to private;
* separate evidence from the symbolic outcome it may authorize;
* do not expose raw health, cycle, journal, household, caregiving, or location
  records to guilds or the shared world;
* require explicit permission for cross-client interpretation;
* allow permission revocation without rewriting settled public history;
* avoid rewards that pressure players to disclose sensitive information.

A shared projection should usually reveal only the game outcome. For example,
other players may see that a sanctuary received care without seeing the private
activity that supported it.

## Nodes And Multiplayer

Pancakes nodes provide the application, identity, permission, and persistence
boundary. A personal node may support solo play and private projections. A
household node may support explicitly shared resources and spaces. Guild and
institutional nodes may coordinate contracts, treasuries, research, and
governance under their own authority.

Multiplayer should expand in stages:

1. solo play and private projections;
2. explicit household sharing;
3. guild cooperation and contracts;
4. institutional and community projects;
5. federated participation between authorized nodes.

No stage requires a globally centralized world or unrestricted identity
sharing.

## One World, Many Clients

Text, web, mobile, ambient, graphical, and agent-assisted clients may interpret
the same platform. Clients can differ radically in presentation and local
simulation while sharing settled resources, contracts, and history.

The domain model must therefore describe actions and outcomes, not Flask
routes, UI widgets, database tables, socket protocols, Minecraft blocks, or
Doom maps. Those are possible adapters and renderers, not the platform.

## Failure And Reconciliation

Clients must tolerate:

* rejected and duplicate claims,
* delayed settlement,
* disconnected nodes,
* stale projections,
* permission changes,
* and projection rebuilds.

Client-local feedback may be immediate, but it must distinguish pending effects
from settled shared effects. Reconciliation uses stable event identity and
idempotent settlement rather than trusting the latest client state.

## Initial Proof

The smallest useful architectural proof has:

* one Pancakes identity and node boundary,
* one source activity,
* one Pitchfork contract and settlement path,
* one private source projection,
* and one RPG projection.

It succeeds when the same accepted event can be interpreted differently by two
authorized clients without copying private source data or creating conflicting
economic truth.
