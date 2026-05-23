# Pitchfork Client API Spec

## Status

Rough draft for Pancakes and Pitchfork client projects.

This document defines the first client-facing contract for applications that want to use Pitchfork primitives. It is intentionally conservative. The goal is to give clients enough structure to build against Pitchfork without turning Pitchfork into a universal life-data warehouse.

The first implementation may be a Python package imported by Flask/Gunicorn clients. The same contract should later be able to become a node-local HTTP API or service boundary.

---

# Purpose

Pitchfork clients need a stable way to:

- identify the node, actor, and client source;
- request permission to record or project activity;
- submit bounded life events;
- receive settlement results;
- query derived state;
- create client-specific projections;
- export user-owned records;
- preserve auditability.

Clients should not bypass Pitchfork by inventing their own ledgers, wallets, token logic, cross-client event streams, or settlement rules.

---

# Core Boundary

Pitchfork accounts.

Clients interpret.

Nodes govern.

Identity authorizes.

Pancakes humanizes.

The client API must preserve this boundary:

```text
client-private record
-> node identity and permission check
-> Pitchfork event
-> capped settlement
-> derived resources or projections
-> client-specific display
```

Pitchfork should usually receive derived, minimal, permissioned events rather than raw intimate records.

---

# Implementation Shapes

## Phase 1: Python Module

Early clients may call Pitchfork as a local Python module:

```python
result = pitchfork.record_event(event_request)
```

This is the preferred first shape for local Pancakes nodes and Flask clients.

## Phase 2: Node-Local HTTP API

The same contract may later be exposed over a node-local API:

```http
POST /pitchfork/v1/events
```

This API should usually be node-local or trusted-service-only at first. Public internet exposure requires additional authentication, rate limiting, audit, and abuse protections.

## Phase 3: Federated Or Hosted API

Federation, hosted sync, and remote node-to-node calls should come later. The event and permission model must be stable before federation.

---

# Required Concepts

## Node

A node is the deployment and governance boundary.

Minimum fields:

```text
Node
- id
- type
- display_name
- policy_version
- created_at
```

Example node types:

- personal
- household
- guild
- cooperative
- institutional
- hosted

## Client

A client is a domain-specific interface over Pancakes and Pitchfork state.

Minimum fields:

```text
Client
- id
- name
- version
- node_id
- allowed_event_types
- allowed_projection_types
- created_at
```

Examples:

- pancakes_wellness_notebook
- pitchfork_rpg
- nexus
- redwitch
- ambient_world

## Actor

An actor is the identity that performs or authorizes an action.

Minimum fields:

```text
ActorRef
- actor_id
- node_id
- identity_claim_id
- assurance_level
```

Pitchfork consumes actor references and permission decisions. It does not impose one global identity provider.

## Permission Grant

A permission grant says that a client may do a specific thing with a specific class of data for a specific purpose.

Minimum fields:

```text
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
- expires_at
- revoked_at
- created_at
```

Permission grants should be understandable to normal users. Do not hide broad consent in terms of service.

## Data Class

Every client-owned record and every Pitchfork event must carry a data classification.

Allowed initial values:

```text
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

Default to `personal` for ordinary private records and `sensitive` for journals, mood, symptoms, sleep notes, cycle details, location traces, household conflict, raw reflections, child or dependent records, and health-adjacent notes.

## Permission Scope

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

Most Wellness Notebook records should start as `private` or `local_client`.

## Event Type

An event type describes the bounded action being accounted.

Example initial event types:

```text
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
```

Sensitive event types must not produce public, economic, or guild-visible effects by default.

## Attestation Method

Pitchfork must know whether an event is self-attested, device-derived, witnessed, imported, or verified.

Allowed initial values:

```text
self_attested
manual_entry
device_import
node_witnessed
participant_witnessed
institution_verified
```

Most early events should be `self_attested` or `manual_entry`.

---

# Event Request

Clients submit events through a single event-recording contract.

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
    projection_intent=[
        "pitchfork_rpg_private"
    ],
    idempotency_key="client-event-uuid"
)

result = pitchfork.record_event(request)
```

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
  "projection_intent": ["pitchfork_rpg_private"]
}
```

## Required Rules

- `node_id`, `client_id`, `actor_id`, `event_type`, `occurred_at`, `data_class`, `permission_scope`, `permission_grant_id`, and `attestation_method` are required.
- `client_record_ref` must refer to a client-owned record, not expose raw sensitive content.
- `measures` must be minimized and coarse by default.
- `projection_intent` is advisory. Pitchfork and node policy decide what is allowed.
- Events must be idempotent.

---

# Event Response

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
  "projections": [
    {
      "projection_type": "pitchfork_rpg_private",
      "projection_id": "proj_001",
      "visibility": "private"
    }
  ],
  "audit_id": "audit_001"
}
```

If rejected:

```json
{
  "accepted": false,
  "error_code": "permission_denied",
  "message": "The permission grant does not allow this event type or data class."
}
```

Do not include sensitive payloads in errors.

---

# Measures

Measures are structured event details.

They should be coarse, bounded, and domain-specific.

## Movement

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

Exact steps may be stored in the client if useful, but Pitchfork usually only needs a band or completion signal.

## Food Balance

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

## Activity

Prefer:

```json
{
  "activity_family": "walking",
  "duration_band": "10_29_minutes",
  "intensity": "light"
}
```

## Reflection

Prefer:

```json
{
  "reflection_completed": true
}
```

Avoid sending raw text, mood details, trauma-adjacent material, or health notes to Pitchfork by default.

---

# Permission API

Clients should ask the node identity and permission layer for grants before submitting Pitchfork events.

## Request Permission

```http
POST /pitchfork/v1/permission-grants
```

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
    "daily_session_completed",
    "challenge_completed"
  ],
  "allowed_projection_types": [
    "pitchfork_rpg_private"
  ],
  "expires_at": null
}
```

## Revoke Permission

```http
POST /pitchfork/v1/permission-grants/{grant_id}/revoke
```

Revocation must stop future use. Existing settlement records may remain where needed for audit or covenant consistency, but raw client records should remain governed by client and node retention policies.

---

# Query API

Queries must respect node policy, actor identity, data class, permission scope, and client grants.

## Get Event

```http
GET /pitchfork/v1/events/{event_id}
```

Use for audit and debugging. Sensitive payloads should not be returned because sensitive payloads should not be stored in Pitchfork events.

## List Actor Events

```http
GET /pitchfork/v1/actors/{actor_id}/events?from=2026-05-01&to=2026-05-23
```

Returns only events the requesting actor or client is allowed to see.

## Get Derived Resources

```http
GET /pitchfork/v1/actors/{actor_id}/resources
```

```json
{
  "actor_id": "actor_456",
  "resources": [
    {
      "resource_type": "ember_moss",
      "amount": 12,
      "scope": "private"
    }
  ]
}
```

## Get Projections

```http
GET /pitchfork/v1/projections?client_id=pitchfork_rpg&scope=private
```

Projection results should reveal symbolic or derived state, not raw client records.

---

# Projection API

Clients may request projections from Pitchfork state.

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
  "projection_type": "rpg_resource_grant",
  "visibility": "private",
  "permission_grant_id": "grant_789"
}
```

Projection visibility values:

```text
private
local_client
node_local
household
guild
trusted_participants
public_symbolic
```

Sensitive source events must not be projected outside `private`, `local_client`, or explicitly trusted scopes unless the projection is symbolic, ambiguous, and specifically permitted.

---

# Settlement And Caps

Pitchfork should cap participation-derived accounting.

Clients must not convert unlimited activity into unlimited resources or economic value.

Minimum cap concepts:

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
-> baseline reward access
-> reduced pressure
```

Not:

```text
more tracking
-> more yield
-> more pressure
```

---

# Audit API

Sensitive access, export, admin override, projection, and permission changes must leave audit records.

## List Audit Events

```http
GET /pitchfork/v1/audit?actor_id=actor_456
```

Audit event shape:

```json
{
  "audit_id": "audit_001",
  "node_id": "node_123",
  "actor_id": "actor_456",
  "accessor_id": "client:pitchfork_rpg",
  "action": "event_recorded",
  "data_class": "personal",
  "permission_grant_id": "grant_789",
  "created_at": "2026-05-23T14:30:02-04:00"
}
```

Audit records must not contain raw sensitive content.

---

# Export API

Export is a first-class node feature.

Pitchfork exports should include:

- events;
- settlements;
- derived resources;
- permission grants;
- projections where permitted;
- audit metadata;
- schema version;
- node identity metadata.

Raw client-private records are exported by the origin client or node, not necessarily by Pitchfork.

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
  "encrypt_to": "gpg:fingerprint"
}
```

Sensitive exports should be encrypted. Signed exports are recommended where identity continuity matters.

---

# Client Requirements

Every client integrating with Pitchfork must:

- classify every record it owns;
- distinguish raw records from derived events;
- request permission before submitting events or projections;
- submit only the minimum data Pitchfork needs;
- use idempotency keys for event writes;
- avoid raw sensitive content in events, logs, analytics, errors, Redis, and AI context;
- respect revocation;
- support export for client-owned records;
- support deletion or retention policy by data class;
- treat admin access as exceptional and auditable;
- avoid third-party analytics in sensitive flows;
- avoid public leaderboards based on raw life metrics.

---

# Hard Lines

Clients must not submit these to Pitchfork by default:

- raw journal text;
- detailed mood entries;
- symptoms;
- cycle or fertility details;
- sexual health details;
- pregnancy-related details;
- trauma-adjacent reflections;
- household conflict notes;
- child or dependent private records;
- raw GPS traces;
- real-time location;
- identity documents;
- secrets, access tokens, private keys, or wallet keys.

Clients must not use Pitchfork for:

- public health scoring;
- productivity scoring;
- insurance, employment, credit, or policing use;
- health-data resale;
- covert AI ingestion;
- direct pay-per-step or pay-per-chore mechanics;
- blockchain storage of sensitive personal data.

---

# Wellness Notebook Example

The Pancakes Wellness Notebook can store a private detailed record:

```text
MovementLog
- exact manual step count
- local session id
- local created_at
```

It should submit a minimal Pitchfork event:

```json
{
  "event_type": "movement_logged",
  "data_class": "personal",
  "permission_scope": "private",
  "attestation_method": "manual_entry",
  "measures": {
    "movement_band": "light",
    "step_band": "2500_4999"
  }
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

# Open Questions

- Does the first implementation expose this as pure Python dataclasses, Pydantic models, SQLAlchemy models, or all three?
- Should Pitchfork own persistence early, or should clients persist events and call Pitchfork for settlement?
- What is the first canonical export format?
- How should GPG identity claims be represented in local development?
- What are the first resource types and caps for Wellness Notebook events?
- Which projections should exist before Nexus and ambient clients are implemented?
- How should node policy be versioned and migrated?
- What should be immutable audit history versus deletable personal history?

---

# Working Rule

If a client cannot explain:

- what raw data it collects;
- what derived event it sends;
- who can see it;
- which permission grant allows it;
- how it is capped;
- how it is audited;
- how it can be exported;
- how it can be deleted or retained;

then the client is not ready to integrate with Pitchfork.

