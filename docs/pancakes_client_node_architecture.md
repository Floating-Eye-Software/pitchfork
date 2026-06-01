# Pitchfork Client and Pancakes Node Architecture

## Design Document for the Pitchfork Project

---

# Purpose

This document defines the architectural relationship between:

* Pancakes nodes
* Pitchfork accounting infrastructure
* The Pitchfork RPG client
* Ambient symbolic clients
* Web/mobile virtual-node clients
* Self-hosted deployments
* Future federation and cooperative infrastructure

It consolidates the current direction for the Pancakes/Pitchfork ecosystem into a single implementation-oriented reference suitable for engineering, systems design, and product planning.

This document should be read alongside:

* *Pitchfork System Overview*
* *Pitchfork RPG Client Product Concept*
* *Pancakes Node Infrastructure*
* *Pitchfork Client API Spec*
* *Ambient Symbolic Clients and Environmental Projection*

---

# Core Direction

Pancakes and Pitchfork are not a single centralized app.

They are:

```text
A node-oriented ecosystem
with multiple clients
sharing one accounting substrate.
```

The system must support:

* Official hosted nodes
* Self-hosted nodes
* Household nodes
* Cooperative nodes
* Guild nodes
* Institutional nodes
* Virtual nodes for mobile/web clients
* Future federation and mesh networking

Hosted infrastructure is important, but it must not become the sole valid deployment model.

---

# Official Hosted Nodes

The first official hosted nodes are:

| Domain          | Role                                                                |
| --------------- | ------------------------------------------------------------------- |
| `pancakes.ca`   | Stable public Pancakes experience                                   |
| `pancakes.love` | Experimental, cooperative, RPG, or blockchain-connected environment |

These are official Pancakes nodes, not “the platform itself.”

The architecture must treat them as:

```text
official hosted deployments
inside a broader node ecosystem
```

not:

```text
the irreplaceable central authority
```

This principle preserves:

* self-hosting,
* local ownership,
* export rights,
* cooperative governance,
* community data stewardship,
* and future federation.

Reference: *Pancakes Node Infrastructure*

---

# Architectural Principle

The core system principle is:

```text
Clients bind to node context.
Clients do not care whether the node is:
- official hosted,
- self-hosted,
- virtual,
- mobile-local,
- or federated.
```

The same client code should work against:

```text
pancakes.ca
pancakes.love
localhost
household node
guild node
mobile virtual node
future federated node
```

This applies especially to:

* Pitchfork RPG
* Wellness Notebook
* Redwitch
* Nexus
* Ambient symbolic worlds
* Cooperative systems
* Administrative tools

---

# Node Model

A Pancakes node is:

```text
a deployment boundary
+
a governance boundary
+
a permission boundary
+
an identity boundary
```

Reference: *Pitchfork System Overview*

A node may be:

| Node Type           | Purpose                                 |
| ------------------- | --------------------------------------- |
| personal_local      | Local-first personal archive            |
| household_local     | Shared family/chosen-family stewardship |
| guild_local         | Cooperative or group infrastructure     |
| institutional_local | Clinics, schools, nonprofits            |
| official_hosted     | pancakes.ca / pancakes.love             |
| virtual_hosted      | Lightweight hosted abstraction          |
| virtual_mobile      | Mobile-local node state                 |
| virtual_offline     | Offline-first temporary node            |

---

# Virtual Nodes

## Purpose

Mobile apps and lightweight web clients need a simpler operational model than full server deployment.

The system should therefore support:

```text
virtual nodes
```

A virtual node is:

```text
a node abstraction
with the same external contract
as a full node
```

but backed by:

* hosted infrastructure,
* local persistence,
* sync adapters,
* mobile databases,
* or future peer systems.

---

# Virtual Node Principle

A virtual node must expose the same conceptual interfaces as a full node:

```text
node_id
node_type
policy_version
identity claims
permission grants
Pitchfork accounting
audit surfaces
export/import
retention rules
projection permissions
```

This preserves:

* portability,
* architectural consistency,
* client compatibility,
* and future migration paths.

---

# Client Architecture

Clients should target:

```text
Node Interface
```

not:

```text
specific deployment environments
```

The architecture should look like:

```text
Client
→ Node Resolver
→ Active Node Context
→ Identity Layer
→ Permission Layer
→ Pitchfork API
→ Projection Systems
→ Client UX
```

---

# Node Resolver

The Node Resolver determines:

* active node,
* connection method,
* local/offline state,
* sync policy,
* federation permissions,
* identity requirements.

Example flows:

## Hosted Login

```text
User opens RPG client
→ selects pancakes.ca
→ authenticates
→ receives node session
→ accesses Pitchfork resources
```

## Self-Hosted Household

```text
User opens Wellness Notebook
→ selects household node
→ authenticates locally
→ accesses household-scoped rituals and covenants
```

## Offline Mobile

```text
User opens mobile client offline
→ virtual_mobile node activates
→ local events recorded
→ sync occurs later
```

---

# Pitchfork Role

Pitchfork is the shared accounting substrate.

Reference: *Pitchfork System Overview*

Pitchfork should remain:

* deployment-agnostic,
* client-agnostic,
* node-aware,
* permission-aware,
* privacy-aware.

Pitchfork should not assume:

* centralized hosting,
* one identity provider,
* one client,
* or one economic model.

---

# Shared Event Flow

The core event flow remains:

```text
real-world action
→ client record
→ node permission check
→ Pitchfork event
→ settlement and caps
→ derived state
→ client-specific projection
```

Reference: *Pitchfork System Overview*

Example:

```text
User logs a walk
↓
Node policy approves movement event
↓
Pitchfork settles capped participation
↓
RPG client grants Ember Moss
↓
Nexus updates Ley Road vendors
↓
Ambient client grows pathways
```

---

# Node-Aware Client Projections

Different clients interpret the same accounting event differently.

Example:

| Layer          | Interpretation                      |
| -------------- | ----------------------------------- |
| Pancakes       | “You logged a walk.”                |
| RPG            | “You gathered Ember Moss.”          |
| Nexus          | “Ley Road activity increased.”      |
| Ambient Client | “Paths emerged through the grass.”  |
| Ledger         | “Movement event settled under cap.” |

Reference: *Pitchfork System Overview*

---

# Ambient Symbolic Clients

Ambient symbolic clients should operate through:

```text
permissioned symbolic projection
```

not:

```text
diagnostic metric exposure
```

Reference: *Ambient Symbolic Clients and Environmental Projection*

Example:

```text
private emotional or cycle state
↓
permissioned symbolic event
↓
environmental modifier
↓
red moon
↓
wildlife changes
↓
dream ecology shifts
```

Not:

```text
explicit reproductive or emotional metrics
```

---

# Redwitch and Sensitive Domains

Sensitive systems require stronger boundaries.

Relevant systems:

* Redwitch
* cycle overlays
* fertility systems
* mood/reflection
* sleep
* caregiving
* health-adjacent rituals

Relevant references:

* *Threat Model for Menstrual-Cycle Tracking Data*
* *Red Witch – Modular Calendar Overlays*
* *Red Witch RMF*

Sensitive domains must default to:

* private-by-default,
* local-first where possible,
* symbolic projection only,
* explicit consent,
* opt-in sharing,
* minimized derived state.

---

# Privacy Boundary Model

The system should distinguish:

| Classification       | Meaning                           |
| -------------------- | --------------------------------- |
| private              | visible only to actor             |
| local_client         | client-only use                   |
| node_local           | available within node policy      |
| household            | visible to household participants |
| guild                | cooperative visibility            |
| trusted_participants | explicitly shared                 |
| public_symbolic      | symbolic/aggregate only           |
| economic_settlement  | covenant settlement only          |

Reference: *Pitchfork Client API Spec*

---

# Mobile and Web App Strategy

## Requirement

Web and mobile clients must work through:

```text
virtual nodes
or equivalent abstractions
```

This is required because:

* many users cannot self-host,
* mobile environments are intermittent,
* offline support matters,
* hosted onboarding matters,
* future federation requires abstraction stability.

---

# Offline-First Direction

Mobile clients should eventually support:

```text
local event queue
→ local permissions
→ deferred synchronization
→ bounded settlement replay
```

This allows:

* offline ritual logging,
* local symbolic progression,
* temporary private operation,
* delayed sync,
* resilience during outages.

---

# Self-Hosting Goals

The long-term architecture should support:

* home servers,
* mini-computer appliances,
* household infrastructure,
* guild servers,
* local-first deployments,
* export/import portability.

Reference: *Pancakes Node Infrastructure*

Potential appliance direction:

```text
small low-power node
+
preconfigured Pancakes software
+
local dashboard
+
automatic updates
+
backup/export tools
```

---

# Federation

Federation should come later.

Early architecture should prioritize:

* coherent permissions,
* stable event models,
* stable export/import,
* node-local consistency,
* privacy boundaries.

Initial federation candidates:

* selective covenant sharing,
* guild coordination,
* symbolic projections,
* aggregate economic signals,
* service listings,
* cooperative pools.

Not:

* unrestricted raw-event replication.

---

# Service Exchange Integration

Pancakes service exchange systems should also be node-aware.

Reference: *Pancakes Service Exchange*

Service systems should support:

* local job boards,
* household covenants,
* mutual aid,
* cooperative pools,
* local credits,
* symbolic RPG integration.

Important principle:

```text
tasks are not automatically services
```

Private household activity must not automatically become marketplace labor.

---

# RPG Client Role

The Pitchfork RPG client is:

```text
one optional interface
over Pitchfork accounting
```

not:

```text
the whole platform
```

Reference: *Pitchfork RPG Client Product Concept*

The RPG should:

* consume Pitchfork projections,
* remain node-aware,
* respect permission boundaries,
* function with hosted and self-hosted nodes,
* support offline virtual-node operation later.

---

# Initial Technical Shape

The near-term implementation can remain simple.

Recommended early stack:

```text
Python accounting module
+
Flask/Gunicorn web apps
+
local database
+
node-local APIs
+
shared event model
```

Reference: *Pitchfork System Overview*

Avoid premature:

* microservices,
* blockchain coupling,
* mandatory federation,
* complex distributed consensus.

---

# Minimum Coherent System

The first successful integration should prove:

```text
one event
→ one accounting settlement
→ multiple node-aware projections
```

Example:

```text
User logs a walk
↓
Pancakes records event
↓
Pitchfork settles movement participation
↓
RPG grants Ember Moss
↓
Nexus updates vendor inventory
↓
Ambient world grows paths
```

Reference: *Pitchfork System Overview*

---

# Core Engineering Principles

## 1. Node First

Every client must operate through node context.

## 2. Hosted Is A Node, Not The Platform

`pancakes.ca` and `pancakes.love` are official nodes.

They are not the sole legitimate deployments.

## 3. Privacy Before Projection

Sensitive state should become symbolic projection, not exposed metrics.

## 4. Clients Interpret

Pitchfork accounts.
Clients interpret.
Nodes govern.
Identity authorizes.

## 5. Self-Hosting Must Remain Real

Self-hosting cannot become a second-class citizen.

## 6. Federation Comes Later

Stabilize permissions and exports before distributed systems.

## 7. Virtual Nodes Are First-Class

Mobile/web abstractions must preserve the node contract.

---

# Immediate Next Steps

## Infrastructure

* Define canonical Node Interface
* Define Virtual Node contract
* Define sync semantics
* Define export/import format
* Implement node-local identity abstraction

## Pitchfork

* Stabilize event model
* Stabilize settlement/cap system
* Stabilize projection pipeline
* Finalize permission scopes

## Clients

* Build RPG client against Node Interface
* Build Wellness Notebook against same interface
* Prototype offline virtual node
* Prototype symbolic ambient projections

## Governance

* Define node governance schema
* Define steward/custodian/member roles
* Define node export guarantees
* Define local retention policy model

---

# Final Principle

The ecosystem should ultimately feel like:

```text
many humane interfaces
sharing one coherent symbolic substrate
across locally governed nodes
```

not:

```text
one centralized app
extracting behavioral data
through mandatory hosting
```
