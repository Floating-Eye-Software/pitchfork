# Pitchfork Ecosystem

## Purpose

This document situates Pitchfork inside the broader Pancakes ecosystem.

Pitchfork and Pancakes are parallel efforts:

- **Pitchfork** is the accounting layer.
- **Pancakes** is the human layer.
- **Pitchfork RPG** is a magical client built on top of Pitchfork.
- **Redwitch** is a possible body-rhythm and period-tracking client.
- **Pancakes Identity** is a shared identity and permissions layer that should sit above individual clients.

The exact integration model can evolve. The important architectural idea is that Pitchfork should provide durable accounting primitives, while Pancakes and its clients provide humane interfaces for living with those primitives.

The broader power-to-the-people direction is described in [Non-Exploitative Infrastructure](non_exploitative_infrastructure.md): Pancakes should help replace extractive platform defaults with local, cooperative, consent-based tools.

## One-Sentence Summary

Pitchfork is the symbolic accounting substrate for Pancakes: it records tokens, materials, contracts, ledgers, permissions, and eventually crypto-facing state, while Pancakes turns ordinary life into a human-scale experience.

## Layer Model

### Pancakes

Pancakes is the broad human-facing life system.

It is the product family, domain, and user-facing container for ordinary life:

- Daily rhythms.
- Ritual logs.
- Personal history.
- Care, rest, movement, food, study, household work, and reflection.
- Human-readable dashboards and journals.
- Domain-specific clients.
- Privacy and consent surfaces.

The name Pancakes fits the project because pancakes are ordinary, embodied, domestic, social, and cross-cultural. Nearly every culture has some form of pancake. That makes the name a good symbol for a life app that wants to recognize common human practices without reducing them to productivity metrics.

Pancakes also carries the mutual-service exchange direction: household help, chores, local services, indirect credits, Pancakes Earth, and community coordination. That layer is described in [Pancakes Service Exchange](pancakes_service_exchange.md).

### Pitchfork

Pitchfork is the base accounting layer.

It should provide the shared model for:

- Tokens.
- Materials.
- Essences.
- Inventory.
- Contracts and covenants.
- Ledgers.
- Scores or balances where appropriate.
- Participation caps.
- Ownership and permissions.
- Future crypto rails.

Pitchfork should not need to know every detail of every client. It should know enough to account for meaningful events, enforce limits, preserve history, and expose stable primitives to clients.

### Pitchfork RPG Client

The Pitchfork RPG client is one interface into Pitchfork.

It is more tightly coupled to the magical mechanics than Pancakes Core:

- Real-world activity becomes magical gathering.
- Materials become recipes, relics, wards, potions, and sanctuary improvements.
- Contracts become covenants or sealed rituals.
- Ledgers become codices or nexus records.
- Tokens and essences become fantasy-native resources.

The RPG client can teach the accounting layer through play, but it should not force every Pancakes user to inhabit the fantasy interface.

### Redwitch

Redwitch is a possible specialized client for menstrual cycles, fertility awareness, symptoms, mood, energy, body rhythms, and related reflection.

It should be treated as a Pancakes client that may use Pitchfork primitives only where they are helpful. It should not be forced into game mechanics where a calmer health-oriented interface is better.

Redwitch also has a higher privacy and safety burden than the RPG client. Cycle data, sexual health data, pregnancy-related data, and symptom logs should be treated as sensitive by default.

## Current Technical Intuition

The early technical split can stay simple:

- Pitchfork base layer: Python package or service.
- Pancakes clients: Flask/Gunicorn web apps.
- Pitchfork RPG client: Flask/Gunicorn web app using Pitchfork primitives.
- Redwitch client: Flask/Gunicorn web app using Pancakes identity and selected Pitchfork primitives.

This does not require a premature microservice architecture.

Early versions can share a Python codebase or import a local Pitchfork package directly. If the boundaries become clearer, Pitchfork can later become a service with an API. If crypto becomes real, the blockchain integration can remain behind the Pitchfork layer rather than leaking into every client.

## Possible Deployment Shape

### pancakes.ca

The stable public app.

Likely role:

- Pancakes Core.
- Non-crypto by default.
- Human-facing dashboards.
- Ritual logging.
- Personal history.
- Gentle inventory and progress systems.
- Privacy-first account management.

### pancakes.love

The beta, variant, or experimental environment.

Possible roles:

- Experimental Pancakes clients.
- Pitchfork RPG previews.
- Blockchain-connected prototypes.
- Cooperative pools.
- Covenants.
- Guild or shared-economy experiments.

The `.love` domain can carry more experimental, relational, and cooperative systems without forcing those risks into the stable `.ca` product.

### Self-Hosted Pancakes Nodes

Pancakes should also support community-run nodes.

Possible operators:

- Individuals.
- Families.
- Households.
- Guilds.
- Circles.
- Cooperatives.
- Schools.
- Clinics.
- Mutual-aid groups.

These nodes let groups retain control over personal logs, ritual history, local policies, cooperative pools, and selected Pitchfork accounting state without depending on the hosted `pancakes.ca` or `pancakes.love` servers.

The governance model is described in [Pancakes Node Infrastructure](pancakes_node_infrastructure.md).

## Integration Principles

### Human Layer First

Pancakes should remain understandable without crypto, markets, or fantasy lore.

Users should be able to log meaningful life activity, see patterns, and feel respected even if they never touch the Pitchfork RPG client or any future blockchain feature.

### Accounting Below Experience

Pitchfork should keep accounting consistent across clients.

Clients may describe the same underlying event differently:

- Pancakes: "You logged a walk."
- Pitchfork RPG: "Your walk gathered ember moss from the ley road."
- Redwitch: "Movement was recorded during the late luteal phase."

Those interfaces can differ, but the underlying event, permissions, caps, and derived resources should remain coherent.

### Privacy By Boundary

Not every client should see every event.

Pitchfork should support boundaries around:

- Sensitive health data.
- Cycle and fertility data.
- Household data.
- Location-derived data.
- Social and covenant data.
- Crypto wallet or financial data.

The accounting layer should avoid becoming a universal surveillance database. It should store what is needed for explicit user-facing value and future auditability, not everything that can be measured.

### Fantasy Is Optional

The RPG client can be richly magical, but Pancakes should not require the player to accept the fantasy frame.

This helps separate:

- Personal quantified-self tools.
- Cozy game mechanics.
- Health-adjacent clients.
- Future cooperative economic systems.

### Crypto Is Behind Pitchfork

If blockchain integration happens, it should be mediated by Pitchfork.

Pancakes clients should not each invent their own wallet, token, contract, or ledger logic. They should ask Pitchfork for accounting operations, and Pitchfork should decide whether those operations remain internal, symbolic, database-backed, or blockchain-backed.

## Shared Concepts

These concepts may appear differently across clients but should eventually share a common substrate:

| Base Concept | Pancakes Human Layer | Pitchfork RPG Client | Future Crypto Analogy |
| --- | --- | --- | --- |
| Identity | Account, profile | Soul sigil | Wallet |
| Event | Logged activity | Ritual | Signed action or oracle input |
| Resource | Material, credit, marker | Moss, dew, salt, essence | Token |
| Commitment | Plan, promise | Covenant | Smart contract |
| Locked value | Held reward | Sealed ritual | Escrow |
| History | Timeline | Codex | Ledger |
| Shared group | Household, circle | Guild | DAO or cooperative |
| Shared store | Pool | Guild vault | Treasury |
| Service exchange | Help, chore, job board listing | Quest, covenant, ritual work | Marketplace or work contract |
| Map layer | Pancakes Earth | Ley map, local sanctuary map | Location-aware oracle input |

## Early Build Guidance

Do not begin by integrating everything.

A pragmatic early path:

1. Stabilize Pitchfork as a Python accounting module.
2. Define a small event model that can represent self-attested life activity.
3. Let Pancakes consume that model through direct Python imports.
4. Build one simple human-facing Pancakes flow.
5. Build one Pitchfork RPG flow that interprets the same event magically.
6. Add persistence, caps, and inventory.
7. Only then decide whether Pitchfork needs to become a separate service.

The first integration win should be small:

```text
One real-life event
-> one Pitchfork accounting record
-> one Pancakes human view
-> one Pitchfork RPG interpretation
```

## Open Questions

- Does Pancakes own identity, or does Pitchfork own identity?
- Should identity be a separate Pancakes Identity layer shared by Pancakes, Pancakes Earth, Pitchfork, Redwitch, UBI-like systems, and nodes?
- Is Pitchfork a Python package, a local service, or both?
- Do clients share one database at first, or does Pitchfork own its own database?
- Which concepts belong in Pancakes Core versus Pitchfork?
- How much of the old token/contract/commodity model should survive?
- Should `pancakes.love` be a beta for all experiments or specifically the blockchain-connected environment?
- How should Pancakes credits relate to Pitchfork materials, essences, and rewards?
- Can Pancakes Earth provide local service discovery without becoming location surveillance?
- What is the minimum viable self-hosted Pancakes node?
- How should self-hosted nodes handle export, import, backups, identity, and federation?
- How should Redwitch protect sensitive reproductive health data while still participating in the broader ecosystem?

## Working Assumption

For now, Pitchfork should be built as a Python base layer that can be imported by Flask/Gunicorn clients.

That keeps the system simple while preserving the future option to expose Pitchfork as an API or connect it to blockchain infrastructure. The architecture should support eventual separation, but the early product should optimize for learning, iteration, and a coherent user experience.
