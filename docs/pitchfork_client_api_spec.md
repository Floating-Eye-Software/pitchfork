# Pitchfork Client API Specification

## Status

Foundational

Companion to:

* Pitchfork Overview
* Pitchfork Contracts
* Pitchfork Symbolic Frequencies
* Pitchfork Symbolic Crafting
* Pitchfork Symbolic Projections
* Pancakes Client and Node Architecture
* Pancakes Node Infrastructure
* Pancakes Reference Services
* Pancakes Node Capabilities

---

# Purpose

This document defines the stable programming contract between clients and the
Pitchfork runtime.

Clients need a predictable way to:

* operate within a Pancakes node;
* identify the acting client and actor;
* request permission to record or project activity;
* submit bounded events;
* receive settlement results;
* request projections;
* query derived symbolic state;
* preserve auditability;
* support export and migration.

The API should give clients enough structure to build against Pitchfork without
turning Pitchfork into a universal life-data warehouse.

Pitchfork should receive minimal, permissioned, structured events.

Clients remain responsible for their own user experience and private records.

---

# Non-Goals

This specification does not define:

* Pancakes node governance;
* node deployment;
* federation protocols;
* application user interfaces;
* long-term network architecture;
* product-specific workflows;
* legal compliance programs.

Those subjects are defined in companion documents.

This specification defines the callable contract a client uses when it needs
Pitchfork services.

---

# Core Boundary

The Pitchfork client boundary is:

```text id="lm8o63"
Client-private record
        │
        ▼
Node identity and permission check
        │
        ▼
Pitchfork event
        │
        ▼
Settlement
        │
        ▼
Derived symbolic state
        │
        ▼
Client-specific projection
        │
        ▼
Client display
```

This boundary preserves the ecosystem's core separation of responsibilities.

```text id="u58yun"
Nodes govern.

Identity authorizes.

Pitchfork accounts.

Clients interpret.

Pancakes humanizes.
```

Clients must not bypass Pitchfork by inventing their own ledgers, wallets,
token logic, cross-client event streams, settlement rules, or symbolic
accounting systems.

---

# Design Principles

## Stable Client Contract

Clients should be able to integrate with Pitchfork through a stable conceptual
contract.

The first implementation may be a local Python module.

Later implementations may expose the same contract as a node-local HTTP API,
SDK, mobile runtime, or service boundary.

The API shape may evolve.

The underlying contract should remain stable.

---

## Node-Governed

Every call occurs in the context of a node.

The node determines:

* local policy;
* permissions;
* actor identity;
* data classification;
* retention rules;
* available capabilities.

Pitchfork does not impose one global governance model.

---

## Capability-Oriented

Clients should discover available capabilities rather than assume that every
node supports identical services.

Some nodes may support rich location services, product registries, or symbolic
projection engines.

Others may support only the minimal Pitchfork event and settlement surface.

Clients should degrade gracefully when capabilities are unavailable.

---

## Reference-Service-Aware

Clients may rely on reference services for shared public or community knowledge.

Examples include:

* places;
* products;
* species;
* civic infrastructure;
* symbolic reference data.

Reference services provide context.

Pitchfork should not become a general-purpose reference database.

---

## Permission Before Settlement

Clients must obtain an appropriate permission grant before submitting events,
requesting projections, or querying derived state.

Permission evaluation occurs before settlement and before projection.

---

## Minimal Event Recording

Pitchfork events should be bounded, structured, and minimized.

Clients should submit the smallest useful event required for accounting,
settlement, and projection.

Raw intimate records generally remain in the originating client or node storage.

---

## Projection Rather Than Duplication

Clients should consume Pitchfork projections rather than duplicating symbolic
state.

Different clients may interpret the same event differently, but they should not
create independent accounting systems for the same underlying activity.

---

## Implementation Independent

The client contract should work across multiple implementation shapes:

* local Python module;
* node-local HTTP API;
* hosted node API;
* mobile runtime;
* virtual node;
* future service boundary.

Clients target the contract, not the deployment.

---

# Runtime Context

Before a client records events or requests projections, it must establish a
runtime context.

The runtime context identifies:

* which node is active;
* which client is acting;
* which actor is authorizing the action;
* which permission grants apply;
* which capabilities are available;
* which reference services are available;
* which policy version governs the request.

A typical startup sequence is:

```text id="xpv9du"
Client starts
        │
        ▼
Resolve active node
        │
        ▼
Establish client identity
        │
        ▼
Establish actor identity
        │
        ▼
Inspect node policy
        │
        ▼
Request or load permission grants
        │
        ▼
Discover capabilities
        │
        ▼
Discover reference services
        │
        ▼
Ready to record events or request projections
```

---

## Active Node

The active node is the governance and runtime boundary for client calls.

Clients do not call Pitchfork in an abstract global context.

They call Pitchfork through a node.

Minimum fields:

```text id="iyzjk2"
Node
- id
- type
- display_name
- policy_version
- created_at
```

Example node types:

```text id="52c11f"
personal
household
community
cooperative
institutional
hosted
virtual_hosted
virtual_mobile
virtual_offline
```

---

## Client

A client is a domain-specific application or interface that uses Pitchfork
services.

Minimum fields:

```text id="ni94jf"
Client
- id
- name
- version
- node_id
- allowed_event_types
- allowed_projection_types
- required_capabilities
- optional_capabilities
- required_reference_services
- created_at
```

Examples:

```text id="56wyr3"
pancakes_wellness_notebook
pancakes_service_exchange
pitchfork_rpg
redwitch
ambient_world
lone_honk_observation
```

---

## Actor

An actor is the identity that performs or authorizes an action.

The actor may represent a person, organization, household, service account, or
future automated agent.

Minimum fields:

```text id="d9gdmj"
ActorRef
- actor_id
- node_id
- identity_claim_id
- actor_type
- assurance_level
```

Allowed initial actor types:

```text id="bmq30k"
person
household
organization
service_account
device
agent
```

Pitchfork consumes actor references and permission decisions.

It does not impose one global identity provider.

---

## Identity Claims

An identity claim represents evidence that a node has associated an actor with
an identity.

Examples may include:

* local account authentication;
* device authentication;
* administrator-issued membership;
* household membership;
* institutional identity;
* future cryptographic identity.

Minimum fields:

```text id="6p2ur6"
IdentityClaim
- id
- node_id
- actor_id
- claim_type
- issuer
- assurance_level
- issued_at
- expires_at
```

The interpretation of identity claims belongs to the node.

Pitchfork requires only enough information to preserve accountability and
auditability.

---

## Node Policy

A node policy describes the local rules governing Pitchfork interaction.

Minimum fields:

```text id="30hsv1"
NodePolicy
- node_id
- policy_version
- allowed_event_types
- allowed_projection_types
- enabled_capabilities
- enabled_reference_services
- retention_profile
- audit_profile
- created_at
```

Clients should not assume that a node permits every event, projection, or
capability.

---

## Permission Grants

A permission grant authorizes a client to perform a specific class of action
for a specific actor, purpose, data class, and scope.

Minimum fields:

```text id="h4f23c"
PermissionGrant
- id
- node_id
- actor_id
- client_id
- scope
- data_class
- purpose
- allowed_event_types
- allowed_projection_types
- allowed_capabilities
- allowed_reference_services
- expires_at
- revoked_at
- created_at
```

Permission grants should be understandable to normal users.

Clients must not hide broad consent in terms of service language.

---

## Capability Discovery

Clients discover node capabilities before using them.

A capability is a reusable service provided by the node.

Minimum fields:

```text id="69b8pl"
CapabilityReference
- id
- node_id
- capability_type
- name
- version
- status
- required_permission_scope
- data_classes_supported
```

Example capability types:

```text id="dcvw1l"
notification
storage
search
calendar
location
barcode_lookup
gis_lookup
media_storage
projection_engine
sync
export
```

Capability discovery allows clients to adapt to nodes with different service
sets.

---

## Reference Service Discovery

Reference services provide shared public, community, or node-scoped knowledge.

Minimum fields:

```text id="trptt5"
ReferenceServiceReference
- id
- node_id
- service_type
- name
- version
- scope
- provenance_policy
- cache_policy
```

Example service types:

```text id="aatb6g"
place
gis
barcode
product
species
civic_infrastructure
recipe_reference
symbolic_reference
```

Reference services provide context for clients and projections.

They should not become hidden channels for private life data.

---

# Core Data Types

This section defines shared types used throughout the API.

Transport-specific schemas may refine these structures, but the conceptual
fields should remain stable.

---

## DataClass

Every client-owned record and every Pitchfork event must carry a data
classification.

Allowed initial values:

```text id="mql6z9"
public
node_shared
household
group
personal
sensitive
regulated_high_risk
economic
cryptographic_secret
```

Default to `personal` for ordinary private records.

Use `sensitive` for journals, mood, symptoms, sleep notes, cycle details,
location traces, household conflict, raw reflections, child or dependent
records, and health-adjacent notes.

Use `regulated_high_risk` for domains requiring formal regulated handling.

Use `cryptographic_secret` for keys, credentials, wallet secrets, access
tokens, and similar material. These should generally never be submitted to
Pitchfork.

---

## PermissionScope

Permission scope describes the intended visibility and use of an event,
projection, or derived state.

Allowed initial values:

```text id="f6l2am"
private
local_client
node_local
household
guild
trusted_participants
public_symbolic
economic_settlement
```

Most personal applications should start with `private` or `local_client`.

Sensitive domains should not produce broader projections by default.

---

## EventType

An event type describes the bounded action being accounted.

Example initial event types:

```text id="d9sg6k"
movement_logged
activity_logged
food_balance_logged
daily_session_completed
challenge_completed
reflection_completed
rest_logged
household_ritual_completed
care_ritual_completed
study_ritual_completed
service_completed
contract_fulfilled
observation_recorded
crafting_completed
```

Sensitive event types must not produce public, economic, or guild-visible
effects by default.

---

## AttestationMethod

Attestation describes how the event was established.

Allowed initial values:

```text id="hg0pw4"
self_attested
manual_entry
device_import
node_witnessed
participant_witnessed
institution_verified
```

Most early events should be `self_attested` or `manual_entry`.

Higher-assurance attestations should be used only where appropriate.

---

## ProjectionType

Projection type describes the form of derived information requested by a
client.

Example projection families:

```text id="pydtcs"
wellness_private
service_exchange
rpg_private
rpg_guild
ambient_symbolic
redwitch_private
redwitch_symbolic
lone_honk_observation
economic_settlement
public_symbolic
```

Projection types should reveal derived or symbolic state, not raw client
records.

---

## SettlementResult

Settlement result describes the outcome of a Pitchfork event.

Minimum fields:

```text id="xno1vp"
SettlementResult
- event_id
- accepted
- settlement_state
- applied_caps
- derived_resources
- updated_contracts
- generated_projections
- audit_id
```

Settlement may create symbolic resources, update contracts, satisfy recipes, or
produce projections.

---

## ProjectionResult

Projection result describes information returned to a client for presentation.

Minimum fields:

```text id="kim789"
ProjectionResult
- projection_id
- projection_type
- actor_id
- source_refs
- visibility
- data_class
- payload
- generated_at
- expires_at
```

Projection payloads should be minimized and appropriate to the requested
visibility.

---

# Implementation Shapes

The same API contract may be exposed through multiple implementation forms.

---

## Python Module

Early implementations may call Pitchfork as a local Python module.

```python
result = pitchfork.record_event(event_request)
```

This is the preferred first implementation for local Pancakes nodes and
Flask/Gunicorn clients.

---

## Node-Local HTTP API

The same contract may later be exposed over a node-local HTTP API.

```http
POST /pitchfork/v1/events
```

This API should usually be local, node-internal, or trusted-service-only at
first.

Public internet exposure requires additional authentication, rate limiting,
abuse protection, and audit controls.

---

## Hosted Node API

Official hosted nodes may expose the same contract through hosted
infrastructure.

Hosted APIs are ordinary node APIs.

They should not receive architectural privileges unavailable to self-hosted
nodes.

---

## Mobile or Virtual Node Runtime

Mobile clients may operate through a virtual node runtime.

A virtual node must still respect:

* permission grants;
* data classification;
* audit metadata;
* retention policy metadata;
* export where practical.

A virtual node is not a shortcut around privacy or governance.

---

# Readiness Rule

A client is not ready to call Pitchfork until it can establish:

* active node;
* client identity;
* actor identity;
* applicable node policy;
* permission grant;
* required capabilities;
* required reference services.

Once these are established, the client is ready to submit events, request
settlement, and consume projections.

---

# Write APIs

This section defines the API surfaces used when clients send information into
Pitchfork or request state-changing operations.

Write APIs include:

* capability discovery and invocation;
* reference service discovery and lookup;
* permission grants;
* event recording;
* settlement;
* projection requests.

Clients should treat write APIs as governed operations.

Every write must occur within an active node context and must respect identity,
permissions, data classification, node policy, idempotency, and audit
requirements.

---

# Runtime Workflow

The ordinary write workflow is:

```text id="9ztlak"
Client
    │
    ▼
Runtime Context
    │
    ▼
Permission Grant
    │
    ▼
Capability / Reference Context
    │
    ▼
Event Request
    │
    ▼
Pitchfork Settlement
    │
    ▼
Projection Request
    │
    ▼
Client Response
```

A client may not need every step for every operation.

For example, a reference lookup may not create a Pitchfork event.

A private event may not request any projection.

A projection request may refer to existing settled state rather than a newly
submitted event.

The general rule is:

> State-changing activity must be permissioned, bounded, auditable, and
> idempotent.

---

# Capability API

Clients should discover available node capabilities before invoking them.

Capabilities are reusable services provided by a node.

Examples include:

* notification;
* storage;
* search;
* calendar;
* location;
* barcode lookup;
* GIS lookup;
* media storage;
* projection engine;
* synchronization;
* export.

Capability discovery allows clients to adapt to different nodes without
assuming every deployment offers identical runtime services.

---

## Discover Capabilities

```http
GET /pitchfork/v1/capabilities
```

Example response:

```json
{
  "node_id": "node_123",
  "capabilities": [
    {
      "id": "cap_gis_001",
      "capability_type": "gis_lookup",
      "name": "Node GIS Lookup",
      "version": "0.1.0",
      "status": "enabled",
      "required_permission_scope": "node_local",
      "data_classes_supported": ["public", "node_shared"]
    },
    {
      "id": "cap_projection_001",
      "capability_type": "projection_engine",
      "name": "Pitchfork Projection Engine",
      "version": "0.1.0",
      "status": "enabled",
      "required_permission_scope": "private",
      "data_classes_supported": ["personal", "sensitive", "economic"]
    }
  ]
}
```

---

## Get Capability Metadata

```http
GET /pitchfork/v1/capabilities/{capability_id}
```

Capability metadata should describe:

* supported operations;
* required permission scopes;
* supported data classes;
* version;
* provenance;
* operational status;
* local policy constraints.

---

## Invoke Capability

```http
POST /pitchfork/v1/capabilities/{capability_id}/invoke
```

Example request:

```json
{
  "node_id": "node_123",
  "client_id": "lone_honk_observation",
  "actor_id": "actor_456",
  "permission_grant_id": "grant_789",
  "operation": "lookup_place",
  "parameters": {
    "place_ref": "place:marsh:east-pond"
  },
  "idempotency_key": "capability-call-uuid"
}
```

Capabilities must not become hidden routes around Pitchfork permissions.

If a capability uses sensitive information, the request must carry appropriate
data classification and permission context.

---

# Reference Service API

Reference services provide shared knowledge used by clients and projections.

Examples include:

* place;
* GIS;
* barcode;
* product;
* species;
* civic infrastructure;
* recipe reference;
* symbolic reference.

Reference services are not private life-data warehouses.

They provide public, community, or node-scoped context.

---

## Discover Reference Services

```http
GET /pitchfork/v1/reference-services
```

Example response:

```json
{
  "node_id": "node_123",
  "reference_services": [
    {
      "id": "ref_place_001",
      "service_type": "place",
      "name": "Node Place Reference",
      "version": "0.1.0",
      "scope": "node_shared",
      "provenance_policy": "required",
      "cache_policy": "allowed"
    },
    {
      "id": "ref_barcode_001",
      "service_type": "barcode",
      "name": "Open Barcode Reference",
      "version": "0.1.0",
      "scope": "public",
      "provenance_policy": "required",
      "cache_policy": "allowed"
    }
  ]
}
```

---

## Query Reference Service

```http
POST /pitchfork/v1/reference-services/{reference_service_id}/query
```

Example request:

```json
{
  "node_id": "node_123",
  "client_id": "pancakes_service_exchange",
  "actor_id": "actor_456",
  "query_type": "lookup",
  "parameters": {
    "identifier": "barcode:0000000000000"
  },
  "permission_grant_id": "grant_789"
}
```

Example response:

```json
{
  "reference_service_id": "ref_barcode_001",
  "result": {
    "identifier": "barcode:0000000000000",
    "name": "Example Product",
    "source": "open_barcode_reference",
    "provenance": [
      {
        "source": "manufacturer",
        "claim": "product_identity",
        "created_at": "2026-06-01T00:00:00Z"
      }
    ]
  }
}
```

Reference results should preserve provenance whenever practical.

Clients should not treat reference data as automatically true simply because it
was returned by a service.

---

# Permission API

Clients must obtain permission grants before submitting events, invoking
sensitive capabilities, querying protected derived state, or requesting
projections.

---

## Request Permission Grant

```http
POST /pitchfork/v1/permission-grants
```

Example request:

```json
{
  "node_id": "node_123",
  "actor_id": "actor_456",
  "client_id": "pancakes_wellness_notebook",
  "scope": "private",
  "data_class": "personal",
  "purpose": "Record private wellness participation for local Pitchfork accounting.",
  "allowed_event_types": [
    "movement_logged",
    "activity_logged",
    "daily_session_completed"
  ],
  "allowed_projection_types": [
    "wellness_private",
    "rpg_private"
  ],
  "allowed_capabilities": [
    "cap_projection_001"
  ],
  "allowed_reference_services": [],
  "expires_at": null
}
```

Example response:

```json
{
  "permission_grant_id": "grant_789",
  "accepted": true,
  "scope": "private",
  "data_class": "personal",
  "expires_at": null,
  "created_at": "2026-06-28T00:00:00Z"
}
```

Permission grants should be understandable to ordinary users.

Broad consent must not be hidden inside general terms of service.

---

## Inspect Permission Grant

```http
GET /pitchfork/v1/permission-grants/{grant_id}
```

Use this to confirm the active grant before submitting events or requesting
projections.

---

## Renew Permission Grant

```http
POST /pitchfork/v1/permission-grants/{grant_id}/renew
```

Renewal should require user comprehension comparable to the original grant.

---

## Revoke Permission Grant

```http
POST /pitchfork/v1/permission-grants/{grant_id}/revoke
```

Revocation must stop future use.

Existing settlement records may remain where needed for audit, consistency, or
contractual history.

Raw client records remain governed by the origin client and node retention
policies.

---

# Event API

Clients submit events through a single event-recording contract.

Events should be:

* bounded;
* minimized;
* classified;
* permissioned;
* idempotent;
* auditable.

---

## Python Shape

```python
from pitchfork.api import EventRequest

request = EventRequest(
    node_id="node_123",
    client_id="pancakes_wellness_notebook",
    actor_id="actor_456",
    event_type="movement_logged",
    occurred_at="2026-05-23T14:30:00-04:00",
    data_class="personal",
    permission_scope="private",
    permission_grant_id="grant_789",
    attestation_method="manual_entry",
    client_record_ref="MovementLog:abc123",
    measures={
        "movement_band": "light",
        "step_band": "2500_4999"
    },
    reference_context=[
        {
            "reference_service_id": "ref_place_001",
            "reference_id": "place:local:park-loop"
        }
    ],
    capability_context=[
        {
            "capability_id": "cap_projection_001",
            "capability_type": "projection_engine"
        }
    ],
    projection_intent=[
        "wellness_private",
        "rpg_private"
    ],
    idempotency_key="client-event-uuid"
)

result = pitchfork.record_event(request)
```

---

## HTTP Shape

```http
POST /pitchfork/v1/events
Content-Type: application/json
Idempotency-Key: client-event-uuid
```

```json
{
  "node_id": "node_123",
  "client_id": "pancakes_wellness_notebook",
  "actor_id": "actor_456",
  "event_type": "movement_logged",
  "occurred_at": "2026-05-23T14:30:00-04:00",
  "data_class": "personal",
  "permission_scope": "private",
  "permission_grant_id": "grant_789",
  "attestation_method": "manual_entry",
  "client_record_ref": "MovementLog:abc123",
  "measures": {
    "movement_band": "light",
    "step_band": "2500_4999"
  },
  "reference_context": [
    {
      "reference_service_id": "ref_place_001",
      "reference_id": "place:local:park-loop"
    }
  ],
  "capability_context": [
    {
      "capability_id": "cap_projection_001",
      "capability_type": "projection_engine"
    }
  ],
  "projection_intent": ["wellness_private", "rpg_private"]
}
```

---

## Required Fields

The following fields are required for event submission:

* `node_id`
* `client_id`
* `actor_id`
* `event_type`
* `occurred_at`
* `data_class`
* `permission_scope`
* `permission_grant_id`
* `attestation_method`
* `idempotency_key`

`client_record_ref` is recommended where the client maintains an origin record.

It must refer to a client-owned record without exposing raw sensitive content.

---

## Optional Context

Events may include:

* `measures`
* `reference_context`
* `capability_context`
* `projection_intent`

Optional context must still respect minimization and permission boundaries.

---

## Measures

Measures are structured event details.

They should be coarse, bounded, and domain-specific.

### Movement

Prefer:

```json
{
  "movement_band": "light",
  "step_band": "2500_4999"
}
```

Avoid by default:

```json
{
  "exact_steps": 4327,
  "route_trace": "...",
  "gps_points": []
}
```

### Food Balance

Prefer:

```json
{
  "meal_type": "lunch",
  "balance_categories": ["fruits_vegetables", "protein"],
  "quantity_estimate": "some"
}
```

Avoid:

```json
{
  "calories": 520,
  "macros": {},
  "barcode": "..."
}
```

### Activity

Prefer:

```json
{
  "activity_family": "walking",
  "duration_band": "10_29_minutes",
  "intensity": "light"
}
```

### Reflection

Prefer:

```json
{
  "reflection_completed": true
}
```

Avoid sending raw text, mood details, trauma-adjacent material, or health notes
to Pitchfork by default.

---

## Event Validation Rules

Events must satisfy the following rules:

* The active node must permit the event type.
* The permission grant must permit the event type, data class, and scope.
* The client must be registered or recognized by the node.
* The actor must be recognized by the node.
* Measures must be minimized and bounded.
* Reference context must come from permitted reference services.
* Capability context must come from available capabilities.
* Events must be idempotent.
* Errors must not contain raw sensitive payloads.

---

# Settlement API

Settlement may occur as part of event submission or through an explicit
settlement operation depending on implementation.

The conceptual contract remains the same.

Settlement transforms accepted events into durable symbolic state.

---

## Event Response with Settlement

Example response:

```json
{
  "event_id": "evt_001",
  "accepted": true,
  "settlement_state": "settled",
  "applied_caps": [
    {
      "cap_id": "daily_movement_participation",
      "status": "within_cap"
    }
  ],
  "derived_resources": [
    {
      "resource_type": "ember_moss",
      "amount": 1,
      "scope": "private"
    }
  ],
  "updated_contracts": [],
  "generated_projections": [
    {
      "projection_type": "rpg_private",
      "projection_id": "proj_001",
      "visibility": "private"
    }
  ],
  "audit_id": "audit_001"
}
```

---

## Rejected Event Response

```json
{
  "accepted": false,
  "error_code": "permission_denied",
  "message": "The permission grant does not allow this event type, data class, or scope."
}
```

Errors must not include sensitive payloads.

---

## Settlement Request

Some implementations may expose settlement separately.

```http
POST /pitchfork/v1/settlements
```

```json
{
  "node_id": "node_123",
  "actor_id": "actor_456",
  "client_id": "pancakes_wellness_notebook",
  "event_ids": ["evt_001"],
  "permission_grant_id": "grant_789",
  "idempotency_key": "settlement-uuid"
}
```

---

## Settlement Caps

Pitchfork should cap participation-derived accounting.

Clients must not convert unlimited activity into unlimited resources or economic
value.

Minimum cap concept:

```text
Cap
- id
- node_id
- event_type
- actor_id or group_id
- period
- limit
- resource_type
- policy_version
```

Example:

```text
daily_movement_participation:
  event_type: movement_logged
  period: day
  max_private_resource_grants: 1
```

Caps should preserve the product principle:

```text
basic participation
→ baseline reward access
→ reduced pressure
```

Not:

```text
more tracking
→ more yield
→ more pressure
```

---

# Projection Request API

Clients may request projections from settled Pitchfork state.

A projection is derived information prepared for a particular client, actor,
scope, and purpose.

Projection requests are state-changing when they create new cached projection
records or audit records.

---

## Request Projection

```http
POST /pitchfork/v1/projections
```

```json
{
  "node_id": "node_123",
  "actor_id": "actor_456",
  "requesting_client_id": "pitchfork_rpg",
  "source_event_ids": ["evt_001"],
  "source_resource_ids": [],
  "projection_type": "rpg_private",
  "visibility": "private",
  "permission_grant_id": "grant_789",
  "idempotency_key": "projection-request-uuid"
}
```

---

## Projection Visibility

Allowed initial values:

```text
private
local_client
node_local
household
guild
trusted_participants
public_symbolic
economic_settlement
```

Sensitive source events must not be projected outside `private`,
`local_client`, or explicitly trusted scopes unless the projection is symbolic,
ambiguous, minimized, and specifically permitted.

---

## Projection Response

```json
{
  "projection_id": "proj_001",
  "projection_type": "rpg_private",
  "actor_id": "actor_456",
  "visibility": "private",
  "data_class": "personal",
  "payload": {
    "message": "Your walk gathered Ember Moss from the ley road.",
    "resources": [
      {
        "resource_type": "ember_moss",
        "amount": 1
      }
    ]
  },
  "source_refs": [
    {
      "type": "event",
      "id": "evt_001"
    }
  ],
  "generated_at": "2026-05-23T14:30:02-04:00",
  "expires_at": null,
  "audit_id": "audit_002"
}
```

Projection payloads should contain derived or symbolic state.

They should not reveal raw client records unless explicitly permitted and
appropriate to the scope.

---

# Idempotency

All write operations must support idempotency.

Clients should provide idempotency keys for:

* event submission;
* capability invocation;
* settlement requests;
* projection requests;
* export requests;
* permission grant requests where appropriate.

Idempotency prevents accidental duplicate settlement, duplicate symbolic
resources, duplicate contracts, and duplicate audit trails.

---

# Write API Rule

If a client cannot explain:

* what it is sending;
* which permission grant authorizes it;
* which capability or reference service is involved;
* which data class applies;
* which settlement may occur;
* which projection may be produced;
* and how duplicate writes are prevented;

then the client is not ready to send the request.

---

# Read APIs

This section defines the API surfaces used when clients retrieve information
from Pitchfork or from Pitchfork-adjacent runtime services.

Read APIs include:

* projections;
* events;
* resources;
* contracts;
* recipes;
* audit records;
* capabilities;
* reference services;
* exports.

Read APIs must respect the same runtime context as write APIs.

A client may retrieve only information authorized by:

* the active node;
* the actor identity;
* the requesting client identity;
* permission grants;
* data classification;
* projection visibility;
* node policy.

Read APIs must not become back doors around permissioned projections.

---

# Projection API

Clients should prefer projections over raw event or settlement queries.

A projection is derived information prepared for a particular client, actor,
scope, and purpose.

Projection responses should expose what the client needs to render its
experience without revealing unnecessary underlying records.

---

## Get Projection

```http
GET /pitchfork/v1/projections/{projection_id}
```

Example response:

```json
{
  "projection_id": "proj_001",
  "projection_type": "rpg_private",
  "actor_id": "actor_456",
  "visibility": "private",
  "data_class": "personal",
  "payload": {
    "message": "Your walk gathered Ember Moss from the ley road.",
    "resources": [
      {
        "resource_type": "ember_moss",
        "amount": 1
      }
    ]
  },
  "source_refs": [
    {
      "type": "event",
      "id": "evt_001"
    }
  ],
  "generated_at": "2026-05-23T14:30:02-04:00",
  "expires_at": null,
  "audit_id": "audit_002"
}
```

---

## List Projections

```http
GET /pitchfork/v1/projections?actor_id=actor_456&client_id=pitchfork_rpg&visibility=private
```

List responses should be scoped by:

* actor;
* requesting client;
* projection type;
* visibility;
* time range;
* permission grant.

Example response:

```json
{
  "actor_id": "actor_456",
  "client_id": "pitchfork_rpg",
  "projections": [
    {
      "projection_id": "proj_001",
      "projection_type": "rpg_private",
      "visibility": "private",
      "generated_at": "2026-05-23T14:30:02-04:00"
    }
  ]
}
```

---

## Projection Families

Projection types may be grouped into families.

Initial projection families include:

```text
wellness
service_exchange
rpg
ambient
redwitch
lone_honk
economic
public_symbolic
```

Families help clients discover compatible projections without hard-coding every
future projection type.

---

## Projection Cache and Invalidation

Some projections may be cached.

Cached projections must preserve:

* source references;
* visibility;
* data classification;
* generation time;
* invalidation rules.

A projection should be invalidated when:

* source events change;
* settlement changes;
* permission is revoked;
* node policy changes;
* projection logic changes;
* relevant reference data changes.

Cached projections must not outlive their permissions.

---

# Event Query API

Event queries are intended for audit, debugging, migration, and specialized
client workflows.

Ordinary user experience should usually consume projections rather than raw
events.

---

## Get Event

```http
GET /pitchfork/v1/events/{event_id}
```

Example response:

```json
{
  "event_id": "evt_001",
  "node_id": "node_123",
  "client_id": "pancakes_wellness_notebook",
  "actor_id": "actor_456",
  "event_type": "movement_logged",
  "occurred_at": "2026-05-23T14:30:00-04:00",
  "data_class": "personal",
  "permission_scope": "private",
  "attestation_method": "manual_entry",
  "client_record_ref": "MovementLog:abc123",
  "measures": {
    "movement_band": "light",
    "step_band": "2500_4999"
  },
  "reference_context": [
    {
      "reference_service_id": "ref_place_001",
      "reference_id": "place:local:park-loop"
    }
  ],
  "created_at": "2026-05-23T14:30:02-04:00",
  "audit_id": "audit_001"
}
```

Event responses must not include raw sensitive payloads.

---

## List Actor Events

```http
GET /pitchfork/v1/actors/{actor_id}/events?from=2026-05-01&to=2026-05-23
```

List responses should support filtering by:

* event type;
* client;
* data class;
* permission scope;
* attestation method;
* time range;
* settlement state.

Example response:

```json
{
  "actor_id": "actor_456",
  "events": [
    {
      "event_id": "evt_001",
      "client_id": "pancakes_wellness_notebook",
      "event_type": "movement_logged",
      "occurred_at": "2026-05-23T14:30:00-04:00",
      "data_class": "personal",
      "permission_scope": "private",
      "settlement_state": "settled"
    }
  ]
}
```

---

# Resource Query API

Resources are derived symbolic or accounting state created by settlement.

Clients may query resources when authorized by node policy and permission
grants.

---

## Get Actor Resources

```http
GET /pitchfork/v1/actors/{actor_id}/resources
```

Example response:

```json
{
  "actor_id": "actor_456",
  "resources": [
    {
      "resource_type": "ember_moss",
      "amount": 12,
      "scope": "private",
      "source_summary": {
        "event_count": 8,
        "last_updated": "2026-05-23T14:30:02-04:00"
      }
    }
  ]
}
```

---

## Get Resource Ledger

```http
GET /pitchfork/v1/actors/{actor_id}/resources/{resource_type}/ledger
```

Resource ledgers should expose only authorized symbolic accounting history.

They should not expose raw originating records unless explicitly permitted.

---

# Contract Query API

Contracts represent structured agreements, obligations, and settlements.

---

## Get Contract

```http
GET /pitchfork/v1/contracts/{contract_id}
```

Example response:

```json
{
  "contract_id": "contract_001",
  "node_id": "node_123",
  "contract_type": "service_exchange",
  "participants": ["actor_456", "actor_999"],
  "state": "active",
  "visibility": "trusted_participants",
  "created_at": "2026-06-28T00:00:00Z",
  "updated_at": "2026-06-28T12:00:00Z"
}
```

---

## List Contracts

```http
GET /pitchfork/v1/contracts?actor_id=actor_456&state=active
```

Contract list responses should be scoped by permission and visibility.

---

# Recipe Query API

Recipes describe repeatable symbolic transformations.

---

## Get Recipe

```http
GET /pitchfork/v1/recipes/{recipe_id}
```

Example response:

```json
{
  "recipe_id": "recipe_ember_tea",
  "name": "Ember Tea",
  "version": "0.1.0",
  "required_resources": [
    {
      "resource_type": "ember_moss",
      "amount": 2
    }
  ],
  "outputs": [
    {
      "resource_type": "ember_tea",
      "amount": 1
    }
  ],
  "visibility": "public_symbolic"
}
```

---

## List Available Recipes

```http
GET /pitchfork/v1/recipes?actor_id=actor_456&client_id=pitchfork_rpg
```

Recipe lists may depend upon:

* actor resources;
* node policy;
* client type;
* symbolic domain;
* enabled capabilities.

---

# Capability Query API

Clients may query capability metadata after discovery.

---

## List Capabilities

```http
GET /pitchfork/v1/capabilities
```

This endpoint returns capabilities available to the current runtime context.

Capabilities unavailable to the actor or client should be omitted or marked
unavailable according to node policy.

---

## Get Capability

```http
GET /pitchfork/v1/capabilities/{capability_id}
```

Capability metadata should include:

* capability type;
* version;
* status;
* supported operations;
* required permission scopes;
* supported data classes;
* operational constraints.

---

# Reference Service Query API

Clients may query reference service metadata and public or permitted reference
records.

---

## List Reference Services

```http
GET /pitchfork/v1/reference-services
```

The response should describe available reference services and their scopes.

---

## Get Reference Service

```http
GET /pitchfork/v1/reference-services/{reference_service_id}
```

Metadata should include:

* service type;
* version;
* scope;
* provenance policy;
* cache policy;
* supported query types.

---

## Get Reference Record

```http
GET /pitchfork/v1/reference-services/{reference_service_id}/records/{reference_id}
```

Reference responses should preserve provenance.

Clients should distinguish reference claims from private user records.

---

# Audit API

Sensitive access, export, admin override, projection, event recording, and
permission changes must leave audit records.

---

## List Audit Events

```http
GET /pitchfork/v1/audit?actor_id=actor_456
```

Example response:

```json
{
  "audit_events": [
    {
      "audit_id": "audit_001",
      "node_id": "node_123",
      "actor_id": "actor_456",
      "accessor_id": "client:pancakes_wellness_notebook",
      "action": "event_recorded",
      "data_class": "personal",
      "permission_grant_id": "grant_789",
      "created_at": "2026-05-23T14:30:02-04:00"
    }
  ]
}
```

Audit records must not contain raw sensitive content.

---

## Get Audit Event

```http
GET /pitchfork/v1/audit/{audit_id}
```

Audit responses should be understandable enough for user review and precise
enough for technical accountability.

---

# Export API

Export is a first-class node and Pitchfork feature.

Pitchfork exports should include:

* events;
* settlements;
* derived resources;
* contracts;
* recipes where permitted;
* projections where permitted;
* permission grants;
* audit metadata;
* schema version;
* node identity metadata.

Raw client-private records are exported by the origin client or node, not
necessarily by Pitchfork.

---

## Request Export

```http
POST /pitchfork/v1/exports
```

```json
{
  "node_id": "node_123",
  "actor_id": "actor_456",
  "scope": "private",
  "include_audit": true,
  "format": "json",
  "encrypt_to": "gpg:fingerprint",
  "idempotency_key": "export-request-uuid"
}
```

---

## Get Export Status

```http
GET /pitchfork/v1/exports/{export_id}
```

Example response:

```json
{
  "export_id": "export_001",
  "state": "ready",
  "format": "json",
  "encrypted": true,
  "created_at": "2026-06-28T00:00:00Z",
  "expires_at": "2026-07-05T00:00:00Z"
}
```

Sensitive exports should be encrypted.

Signed exports are recommended where identity continuity matters.

---

# Read API Rule

If a client cannot explain:

* why it needs the requested information;
* which actor is requesting it;
* which permission grant permits access;
* which data class applies;
* which visibility applies;
* whether a projection would be safer than raw data;
* how the access will be audited;

then the client is not ready to retrieve the information.

---

# Client Contract

This section defines the obligations every client must satisfy before
integrating with Pitchfork.

The previous sections describe how clients connect, send information, and
retrieve information.

This section defines the rules that keep those interactions safe,
permissioned, auditable, and consistent with the Pancakes runtime.

---

# Client Requirements

Every client integrating with Pitchfork must satisfy the following
requirements.

---

## Resolve a Node

Every client must operate against an active node.

The client must know:

* which node it is using;
* which node policy version applies;
* whether the node is hosted, local, or virtual;
* which runtime services are available.

Clients must not call Pitchfork as if it were a global service without node
context.

---

## Establish Identity

Every client must establish the acting identity before submitting or retrieving
information.

The client must know:

* which actor is acting;
* which identity claim supports the actor;
* what assurance level applies;
* whether the actor represents a person, organization, device, or service
  account.

Pitchfork consumes identity context.

The node governs identity.

---

## Obtain Permission

Every client must obtain appropriate permission before:

* submitting events;
* invoking sensitive capabilities;
* querying protected information;
* requesting projections;
* exporting information.

Permission grants must be specific enough to explain:

* who is acting;
* which client is acting;
* what data class applies;
* what scope applies;
* what purpose is authorized;
* what event or projection types are allowed.

---

## Discover Capabilities

Clients must discover available capabilities rather than assuming every node
provides the same services.

If a required capability is unavailable, the client should fail clearly or
degrade gracefully.

If an optional capability is unavailable, the client should continue without it
where practical.

---

## Discover Reference Services

Clients must discover reference services before relying on them.

A client should know:

* which reference service supplied information;
* what scope applies;
* what provenance policy applies;
* whether the information may be cached;
* whether the information is public, node-shared, or otherwise restricted.

---

## Minimize Event Payloads

Clients must submit only the information Pitchfork needs for accounting,
settlement, and projection.

Raw intimate records should ordinarily remain in the originating client or node
storage.

Pitchfork events should be:

* bounded;
* structured;
* classified;
* permissioned;
* auditable;
* idempotent.

---

## Respect Settlement

Clients must not create independent symbolic accounting systems for activity
that belongs in Pitchfork.

Clients may maintain private records for user experience.

Pitchfork owns shared accounting, settlement, provenance, contracts, recipes,
and symbolic state.

---

## Consume Projections

Clients should consume projections rather than duplicating derived symbolic
state.

Projections allow many clients to interpret shared activity differently while
remaining consistent with the same underlying accounting.

---

## Support Export

Clients must support export of client-owned records where appropriate.

Pitchfork exports contain Pitchfork records.

Client-private records remain the responsibility of the originating client or
node storage.

A complete user export may therefore require both:

* Pitchfork export;
* client export.

---

## Respect Retention

Clients must respect retention policies associated with:

* node policy;
* data class;
* permission grants;
* legal or institutional obligations;
* user requests.

Retention policy should be understandable to users.

---

## Preserve Auditability

Clients must preserve auditability for:

* event recording;
* projection requests;
* sensitive access;
* permission changes;
* export;
* administrative actions.

Audit records must not contain raw sensitive content.

---

# Hard Requirements

The following requirements are not optional.

---

## No Raw Sensitive Records by Default

Clients must not submit raw sensitive records to Pitchfork by default.

Examples include:

* raw journal text;
* detailed mood entries;
* symptoms;
* fertility or cycle details;
* sexual health details;
* pregnancy-related details;
* trauma-adjacent reflections;
* household conflict notes;
* child or dependent private records;
* raw GPS traces;
* real-time location;
* identity documents;
* secrets, access tokens, private keys, or wallet keys.

Clients may store some of these records locally when appropriate.

Pitchfork should ordinarily receive only minimized derived events.

---

## No Permission Bypass

Clients must not access Pitchfork data or invoke Pitchfork operations without
appropriate permission grants.

Capabilities, reference services, projections, and query APIs must not become
side channels around the permission model.

---

## No Settlement Bypass

Clients must not invent parallel ledgers, settlement rules, wallets, token
systems, or symbolic accounting systems for activity that should be governed by
Pitchfork.

Clients may present information differently.

They may not silently create independent accounting realities.

---

## No Public Scoring of Private Life

Clients must not use Pitchfork to produce public rankings, public health
scores, productivity scores, or status systems based on raw life metrics.

This includes:

* public step-count leaderboards;
* public productivity rankings;
* public care-work scores;
* public health comparisons;
* gamified shame mechanics.

Symbolic participation should reduce pressure, not increase it.

---

## No High-Stakes Misuse

Clients must not use Pitchfork for:

* insurance decisions;
* employment decisions;
* credit decisions;
* policing;
* immigration enforcement;
* covert behavioral profiling;
* health-data resale;
* covert AI ingestion.

Pitchfork exists to support humane interpretation and cooperative accounting.

It must not become infrastructure for coercive classification.

---

## No Sensitive Blockchain Storage

Clients must not place sensitive personal information on public blockchains or
other irreversible public ledgers.

Future cryptographic or economic integrations must preserve privacy, consent,
and reversibility where required.

---

## No Hidden Federation Assumptions

Clients must not assume federation exists.

A local or standalone node remains a complete and legitimate deployment.

Clients should work locally whenever practical.

---

# Integration Examples

These examples illustrate how different clients should interact with the same
Pitchfork contract.

---

## Wellness Notebook

A wellness client may maintain private detailed records locally.

Example local record:

```text
MovementLog
- exact manual step count
- local session id
- local created_at
- local notes
```

The client should submit a minimized Pitchfork event:

```json
{
  "node_id": "node_123",
  "client_id": "pancakes_wellness_notebook",
  "actor_id": "actor_456",
  "event_type": "movement_logged",
  "occurred_at": "2026-05-23T14:30:00-04:00",
  "data_class": "personal",
  "permission_scope": "private",
  "permission_grant_id": "grant_789",
  "attestation_method": "manual_entry",
  "client_record_ref": "MovementLog:abc123",
  "measures": {
    "movement_band": "light",
    "step_band": "2500_4999"
  },
  "projection_intent": ["wellness_private", "rpg_private"],
  "idempotency_key": "client-event-uuid"
}
```

Pitchfork may settle:

```json
{
  "resource_type": "ember_moss",
  "amount": 1,
  "scope": "private"
}
```

The RPG client may display:

```text
Your walk gathered Ember Moss from the ley road.
```

No other client needs the exact step count.

---

## Service Exchange

A service exchange client may create contracts between participants.

Example event:

```json
{
  "node_id": "node_123",
  "client_id": "pancakes_service_exchange",
  "actor_id": "actor_456",
  "event_type": "service_completed",
  "occurred_at": "2026-06-28T12:00:00-04:00",
  "data_class": "economic",
  "permission_scope": "trusted_participants",
  "permission_grant_id": "grant_service_001",
  "attestation_method": "participant_witnessed",
  "client_record_ref": "ServiceCompletion:svc_001",
  "measures": {
    "service_family": "repair",
    "completion_state": "completed"
  },
  "projection_intent": ["service_exchange", "economic_settlement"],
  "idempotency_key": "service-completion-uuid"
}
```

The client owns service workflow.

Pitchfork owns settlement and provenance.

---

## Pitchfork RPG

The RPG client consumes projections and symbolic state.

It should not infer private life activity directly.

Example projection query:

```http
GET /pitchfork/v1/projections?actor_id=actor_456&client_id=pitchfork_rpg&visibility=private
```

The RPG may display:

```text
Your guild satchel contains Ember Moss, Rain Glass, and Hearth Salt.
```

It should not display the private events that produced those materials unless
specifically permitted.

---

## Red Witch

Red Witch handles sensitive reproductive and cycle-related information.

Detailed records should remain local to Red Witch or the node's appropriate
private storage.

Pitchfork should ordinarily receive only minimized symbolic or participation
events when explicitly permitted.

Example symbolic event:

```json
{
  "node_id": "node_123",
  "client_id": "redwitch",
  "actor_id": "actor_456",
  "event_type": "rest_logged",
  "occurred_at": "2026-06-28T09:00:00-04:00",
  "data_class": "sensitive",
  "permission_scope": "private",
  "permission_grant_id": "grant_redwitch_private",
  "attestation_method": "manual_entry",
  "client_record_ref": "RedWitchPrivateRecord:local_ref",
  "measures": {
    "rest_signal": "completed"
  },
  "projection_intent": ["redwitch_private"],
  "idempotency_key": "redwitch-event-uuid"
}
```

The event should not expose cycle day, symptoms, fertility details, sexual
health details, or reproductive status by default.

---

# Versioning

The API must support long-term evolution without breaking clients
unnecessarily.

---

## API Versioning

Transport-level APIs should use explicit versions.

Example:

```http
/pitchfork/v1/events
```

Breaking changes require a new API version.

Non-breaking additions may occur within the same version when clients can
safely ignore unknown fields.

---

## Schema Evolution

Schemas should evolve according to the following principles:

* Add fields rather than rename fields where practical.
* Preserve stable identifiers.
* Treat unknown fields as ignorable unless explicitly marked required.
* Maintain migration notes for breaking changes.
* Preserve export compatibility wherever practical.

---

## Capability Evolution

Capabilities may evolve independently of the core API.

Capability metadata should include:

* capability type;
* version;
* supported operations;
* deprecation status;
* compatibility notes.

Clients should discover capabilities dynamically rather than hard-coding
assumptions.

---

## Reference-Service Evolution

Reference services may update their schemas and provenance policies over time.

Reference service metadata should include:

* service type;
* version;
* scope;
* cache policy;
* provenance policy;
* deprecation status.

Clients should preserve source references so that later changes remain
traceable.

---

## Node Policy Evolution

Node policy may change over time.

Policy changes may affect:

* permitted event types;
* projection visibility;
* retention;
* enabled capabilities;
* enabled reference services;
* audit rules.

Clients must inspect node policy and should not assume that yesterday's policy
still applies today.

---

# Open Questions

The remaining open questions are implementation questions rather than
architectural questions.

Examples include:

* Should the first implementation use dataclasses, Pydantic models, SQLAlchemy
  models, or a combination?
* Which transport should be implemented first after the Python module?
* How should SDK generation be handled?
* What authentication mechanism should node-local HTTP use?
* How should capability negotiation be represented in Python?
* How should reference-service caching be implemented?
* What is the first canonical export package format?
* How should projection invalidation be represented?
* How should node policy migration be tested?
* Which examples should become test fixtures?

---

# Working Rule

A client is correctly integrated with Pitchfork only when it can answer:

* Which node am I operating against?
* Which actor is acting?
* Which client is acting?
* Which identity claim supports the actor?
* Which permission grant authorizes this operation?
* Which capability am I using?
* Which reference service do I depend upon?
* Which event am I recording?
* Which data class applies?
* Which permission scope applies?
* Which settlement may occur?
* Which projection am I requesting or consuming?
* What audit trail will exist?
* How can the user export relevant information?
* How can retention or deletion be honored?

If a client cannot answer these questions, it is not ready to integrate with
Pitchfork.
