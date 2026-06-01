# Pitchfork Household Management Model

## Purpose

This document defines how Pitchfork should support the Pancakes Household Management Model from the accounting, covenant, resource, projection, and privacy side.

The Pancakes household model describes how a household can maintain food, shelter, care, hygiene, safety, money, relationships, records, routines, and future capacity. That full operating model belongs primarily to Pancakes because it is human-facing, contextual, private, and practical.

Pitchfork should not become the household management app.

Pitchfork should provide the durable substrate that lets Pancakes turn selected household activity into permissioned events, symbolic resources, ratified covenants, private inventories, household projections, and node-level aggregate signals without exposing raw intimate life.

## Source Relationship

Primary upstream source:

- `pancakes/docs/pancakes-household-management-model.md`

Related Pitchfork documents:

- [Pitchfork System Overview](pitchfork_overview.md)
- [Pitchfork Client API Spec](pitchfork_client_api_spec.md)
- [Pitchfork Privacy and Security](pitchfork_privacy_security.md)
- [Pitchfork Data Sovereignty](pitchfork_data_sovereignty.md)
- [Pitchfork Economics](pitchfork_economics.md)
- [Pancakes Service Exchange](pancakes_service_exchange.md)
- [Pitchfork Node Quality of Life Signals](pitchfork_node_quality_of_life.md)

## Boundary Principle

The household boundary should be:

```text
Pancakes household record
-> minimized permissioned event
-> Pitchfork settlement
-> symbolic resource, covenant state, projection, or aggregate signal
```

Not:

```text
raw household life
-> universal Pitchfork database
-> scoring, surveillance, market pricing, or public productivity display
```

Pancakes owns:

- household routines;
- tasks and reminders;
- calendars;
- journals and reflections;
- household notes;
- private health and care details;
- role negotiation;
- household UX;
- consent surfaces;
- practical support workflows.

Pitchfork owns:

- event accounting;
- data classes and permission scopes;
- idempotent settlement;
- participation caps;
- symbolic materials and essences;
- inventories;
- covenants;
- ledgers;
- audit metadata;
- projections;
- cooperative pool and service-exchange accounting where explicitly enabled.

## Design Goals

Pitchfork household support should:

- recognize household stewardship as meaningful activity;
- avoid turning domestic work into extractive behavioral labor;
- support private household covenants;
- preserve dignity for care recipients and caregivers;
- separate private tasks from public services;
- support child, dependent, reproductive, health, financial, and safety privacy;
- allow symbolic RPG interpretation without forcing game mechanics into Pancakes;
- enable local and household nodes to govern their own rules;
- support aggregate node review only with safeguards.

## Non-Goals

Pitchfork should not provide:

- a universal chore ranking;
- a global price table for domestic work;
- household productivity scores;
- family surveillance dashboards;
- public leaderboards for chores, care, rest, or hygiene;
- default economic rewards for intimate activity;
- health, fertility, conflict, child, dependent, or financial data speculation;
- raw household task storage unless it is acting as the local Pancakes node itself.

## Household Domains as Pitchfork Inputs

The Pancakes model uses twelve Lifecraft-aligned household domains. Pitchfork may use these as source classification, but it should reduce them to minimal accounting concepts.

| Pancakes household domain | Pitchfork support |
| --- | --- |
| Personal Health | private health-adjacent events, nourishment/rest materials, sensitive defaults |
| Emergency Knowledge | preparedness covenants, safety-check events, household resilience projections |
| Mental and Emotional Wellbeing | rest/recovery events, overload signals only where consented, no inferred wellness scores |
| Relationships | private relationship rituals, guest/commitment covenants, no conflict exposure by default |
| Household Stewardship | cleaning, laundry, maintenance, inventory, and order materials |
| Financial Literacy | economic records only under explicit economic scope; budget stress as sensitive |
| Civic Literacy | deadlines, services, and rights support events; node or household reminders stay in Pancakes |
| Information Literacy | document, backup, password, and record-care rituals; no secret storage in Pitchfork |
| Human Development | age-appropriate skill-transfer and transition covenants; child/dependent safeguards |
| Reproductive and Sexual Health | sensitive by default; symbolic projection only with explicit consent |
| Caregiving and Community Support | care rituals, respite covenants, service exchange, mutual aid support |
| Meaning, Purpose, and Flourishing | rituals, holidays, future-planning covenants, sanctuary or identity projections |

## Event Model

Household events should be coarse, bounded, and permissioned.

Example event types:

```text
household_ritual_completed
household_stewardship_completed
meal_support_completed
laundry_flow_supported
cleaning_round_completed
maintenance_task_completed
repair_issue_logged
safety_check_completed
emergency_prep_reviewed
care_ritual_completed
respite_support_completed
pet_care_completed
document_care_completed
household_planning_completed
relationship_ritual_completed
meaning_ritual_completed
service_request_created
service_offer_created
service_fulfilled
household_covenant_ratified
household_covenant_settled
```

Avoid event types that encode raw intimate detail:

```text
spouse_conflict_logged
child_hygiene_failure_recorded
pregnancy_symptom_reported_to_household
bank_balance_low_public
care_recipient_missed_medication_public
```

When sensitive facts matter to Pancakes, the Pitchfork event should usually be a minimal completion, support, or covenant signal.

Example:

```json
{
  "event_type": "care_ritual_completed",
  "data_class": "sensitive",
  "permission_scope": "private",
  "attestation_method": "self_attested",
  "measures": {
    "care_domain": "daily_support",
    "intensity_band": "moderate"
  },
  "projection_intent": ["pitchfork_rpg_private"]
}
```

## Measures

Measures should be structured, coarse, and domain-specific.

Good household measures:

```json
{
  "domain": "household_stewardship",
  "activity_band": "routine",
  "duration_band": "15_30_minutes",
  "visibility": "household_private"
}
```

```json
{
  "domain": "emergency_preparedness",
  "check_type": "alarm_test",
  "status": "completed"
}
```

```json
{
  "domain": "meal_support",
  "meal_type": "dinner",
  "support_level": "shared"
}
```

Avoid by default:

```json
{
  "raw_note": "Full description of family conflict or care recipient condition",
  "exact_location_trace": [],
  "bank_transactions": [],
  "child_behavior_log": "...",
  "cycle_details": "..."
}
```

## Data Classes

Default household data classification should be conservative.

| Household record | Default data class |
| --- | --- |
| ordinary private task completion | `personal` or `household` |
| shared household covenant | `household` |
| household service listing | `node_shared` or `group` |
| public community service offer | `public` only if explicitly posted |
| journals, mood, rest notes, symptoms, cycle details, conflict notes | `sensitive` |
| child, dependent, disability, pregnancy, medical, safety, or financial vulnerability records | `sensitive` or `regulated_high_risk` |
| credits, escrow, paid services, cooperative pools | `economic` |
| passwords, private keys, wallet keys, recovery secrets | `cryptographic_secret` and generally not stored by Pitchfork |

## Permission Scopes

Initial household scopes:

```text
private
local_client
household
trusted_participants
node_local
economic_settlement
public_symbolic
```

Use `private` or `local_client` for most household events.

Use `household` when the event is intentionally visible to authorized household members.

Use `trusted_participants` for care circles, mutual-aid circles, or service covenants with named participants.

Use `economic_settlement` only when credits, escrow, payment, cooperative pools, or other value-bearing settlement is involved.

Use `public_symbolic` only for deliberately ambiguous projections that do not reveal raw household facts.

## Covenants

Household covenants are the most important Pitchfork primitive for household management.

A household covenant is a structured, permissioned commitment recognized by a household node.

Minimum fields:

```text
HouseholdCovenant
- id
- node_id
- household_id
- title
- purpose
- participants
- steward_actor_id
- witness_rule
- settlement_rule
- reward_rule
- privacy_boundary
- data_class
- permission_scope
- starts_at
- ends_at
- status
- created_at
```

Example:

```text
Covenant: Keep the Kitchen Clear
Purpose: Preserve one usable food preparation area.
Participants: Alex, Sam
Steward: Alex
Witness rule: Either participant may attest; steward resolves mismatch.
Settlement rule: Three completed dinner cleanups in one week.
Reward rule: Household stability +2; Order Salt +1 each.
Privacy boundary: Household only.
Data class: household
Permission scope: household
```

Covenants should support:

- ratification;
- amendment;
- expiration;
- revocation;
- dispute state;
- settlement;
- audit metadata;
- export;
- participant visibility rules.

They should not require:

- constant surveillance;
- exact time tracking;
- punitive streaks;
- public proof;
- universal pricing.

## Attestation

Household events may be attested in different ways:

```text
self_attested
manual_entry
participant_witnessed
node_witnessed
institution_verified
```

Most household events should be `self_attested` or `manual_entry`.

Use `participant_witnessed` for shared covenants.

Use `node_witnessed` only when the node has a legitimate operational reason.

Use `institution_verified` only for high-trust workflows such as grants, benefits, school, clinical, or legal contexts.

Avoid requiring device-derived or sensor-derived proof for ordinary household stewardship.

## Symbolic Resources

Household events may generate private or household-scoped symbolic resources.

Possible materials:

| Material | Source domain |
| --- | --- |
| Order Salt | cleaning, laundry, organizing, household stewardship |
| Hearthlight | meal support, caregiving, family rituals |
| Threshold Wax | safety checks, emergency preparation, boundary setting |
| Mending Thread | repairs, maintenance, clothing care, relationship repair |
| Pantry Grain | groceries, meal planning, food continuity |
| Rest Ash | recovery, respite, burnout prevention |
| Ledger Dust | bills, documents, budgets, records |
| Memory Ink | family records, traditions, reflections |
| Garden Loam | plants, yard care, seasonal household work |
| Companion Fur | pet care and animal stewardship |

Possible essences:

```text
Hearth Essence
Order Essence
Shelter Essence
Care Essence
Resilience Essence
Continuity Essence
Belonging Essence
Flourishing Essence
```

Rewards should be capped and mostly non-tradable by default. Household resources represent recognition, not wages.

## Settlement and Caps

Household settlement must avoid yield pressure.

Recommended caps:

- daily cap per household domain;
- weekly cap per covenant;
- soft cap for repeated low-risk tasks;
- no public multiplier for sensitive care;
- no economic conversion from sensitive domains by default;
- no child/dependent farming incentives;
- no reward advantage for exposing more detail.

Example:

```text
One cleaning event may produce Order Salt today.
Additional cleaning can update household flavor or progress text.
It should not produce infinite material yield.
```

## Tasks, Services, and Covenants

Pitchfork must distinguish three related concepts.

| Concept | Owner | Visibility | Pitchfork role |
| --- | --- | --- | --- |
| Task | Person, household, or Pancakes client | Private by default | Optional completion event |
| Service | Offered or requested between people | Scoped listing | Credit, escrow, trust, fulfillment settlement |
| Covenant | Ratified commitment | Participants or household | Agreement, witness, settlement, reward, dispute path |

The same action may appear in all three forms, but only when explicitly converted.

Example:

```text
Task: Clean our kitchen after dinner.
Covenant: Keep one food-prep area usable this week.
Service: Offer kitchen cleanup help to another household.
Pitchfork projection: Order Salt gathered; hearth entropy reduced.
```

Private tasks must not automatically become services or market offers.

## Household Projections

Pitchfork may expose symbolic projections to clients.

Private RPG examples:

```text
The hearth burns steadily.
The pantry spirit has returned.
The threshold ward was refreshed.
Order Salt crystallized along the sanctuary floor.
The garden remembered your care.
```

Household dashboard examples:

```text
Kitchen covenant settled this week.
Emergency preparation was reviewed this month.
Care coverage looks under-supported.
Laundry flow is stable.
One maintenance issue needs review.
```

Node aggregate examples:

```text
Meal support requests are rising.
Care tasks are concentrated among too few participants.
Emergency preparedness participation improved this quarter.
Service fulfillment is stable.
```

Projection rules:

- Private projections may be specific to the user.
- Household projections require household permission.
- Node aggregate projections require thresholds and suppression rules.
- Public symbolic projections must be ambiguous and non-identifying.

## Quality of Life Signals

Household events can contribute to node quality-of-life signals only when consented and thresholded.

Allowed aggregate directions:

- service requests rising or falling;
- unmet support needs;
- care burden concentration;
- household preparedness trends;
- food, transport, childcare, repair, or respite support gaps;
- cooperative pool strain;
- seasonal resilience.

Forbidden directions:

- ranking households;
- scoring individual caregivers;
- inferring subjective wellbeing from chore completion;
- exposing small-cohort sensitive patterns;
- using household signals for eligibility denial, advertising, insurance, employment, or coercive governance.

For household nodes with too few people, quality-of-life reporting should operate as a private review tool rather than anonymous analytics.

## Sensitive Household Areas

The following areas require special handling:

- children and dependents;
- reproductive and sexual health;
- pregnancy and postpartum support;
- disability and chronic illness;
- medication routines;
- mental health;
- household conflict;
- domestic safety planning;
- financial vulnerability;
- identity documents;
- location traces;
- caregiving load;
- private relationship rituals.

Default posture:

```text
raw record stays in Pancakes or local client
-> minimized derived event only if useful
-> sensitive data class
-> private or explicitly scoped permission
-> no public, guild, economic, or AI reuse by default
```

## Household Nodes

A household node is a governance boundary for a household.

It may govern:

- household members;
- child or dependent profiles;
- guests;
- caregivers;
- service providers;
- household covenants;
- shared inventories;
- shared credits or pools;
- exports and retention;
- permission grants;
- audit visibility.

Household node policy should answer:

- Who can create household tasks?
- Who can ratify covenants?
- Who can witness completion?
- Who can see sensitive categories?
- Who can invite service providers?
- Who can export household records?
- Who can revoke sharing?
- What happens when someone leaves the household?
- How are child and dependent records handled?
- What data is deleted, retained, or sealed?

## Implementation Guidance

The first Pitchfork implementation should be small.

Recommended first slice:

```text
household_ritual_completed
-> EventRequest
-> data_class and permission_scope validation
-> daily cap
-> Order Salt or Hearthlight reward
-> private RPG projection
-> audit metadata
```

Recommended second slice:

```text
ratified household covenant
-> participant attestations
-> settlement rule
-> household-scoped resource reward
-> covenant ledger entry
```

Recommended third slice:

```text
household service request
-> trusted participant scope
-> credit or symbolic reward settlement
-> dispute state
-> exportable ledger
```

Do not start with:

- complete household ontology;
- automated sensor proof;
- child dashboards;
- detailed care records;
- economic pricing;
- cross-household marketplace defaults;
- aggregate analytics.

## Open Questions

- Should Pitchfork define a formal `household_id`, or should that remain node-specific metadata?
- Which household event types belong in the initial API enum?
- Should household covenants share the same contract model as service exchange covenants, or use a lighter household-local shape?
- How should participant consent work when one household action concerns multiple people?
- What minimum audit surfaces are needed for household records without creating surveillance?
- Which symbolic materials should be canonical versus client-specific flavor?
- How should household data export work when records concern multiple household members?
- What are the rules when a minor becomes an adult and wants control over past records?

## Summary

The Pancakes household model describes the human system.

Pitchfork should support it by accounting for selected, consented, minimized household events and covenants.

The correct Pitchfork abstraction is not a chore tracker. It is a privacy-preserving substrate for household meaning, symbolic resources, scoped commitments, cooperative support, and accountable settlement.
