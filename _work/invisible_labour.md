# Supporting the Singer: Household Labor Design Note

## Purpose

This note uses the household-labor scenario described in `_work/he-thinks-hell-keep-her.txt` as a design stress test for Pancakes and Pitchfork.

The person at the center of the song is not simply doing chores. She is carrying a household operating system: food, laundry, beds, child logistics, school participation, appointments, driving, social presentation, travel preparation, timing, polish, and emotional containment. The failure is not that tasks exist. The failure is that years of skilled domestic labor are treated as automatic, unpaid, secure, and owned by someone else.

The product question is:

```text
How should Pancakes and Pitchfork support someone whose household labor is invisible, economically undervalued, and personally depleting?
```

## Design Stance

The system should support her autonomy, safety, recognition, and transition capacity.

It should not try to keep the household running at her expense.

That distinction matters. A naive household-management tool could make her more efficient while preserving the same unfair structure. Pancakes should instead help reveal load, redistribute responsibility, preserve private reflection, and support exit or renegotiation when needed.

## What She Is Actually Doing

The visible tasks include:

- meal and drink preparation;
- bed and laundry maintenance;
- feeding the household;
- child transportation;
- school and parent-organization participation;
- medical and dental appointment logistics;
- household driving;
- holiday and family-image administration;
- travel packing and spouse support logistics;
- timing, cleanliness, polish, and emotional composure.

The less visible work includes:

- remembering what needs to happen;
- anticipating other people's needs;
- protecting the household's public image;
- smoothing schedules;
- maintaining continuity across years;
- absorbing emotional cost;
- deferring personal change;
- bearing economic risk from unpaid domestic work.

This is not only household stewardship. It is domestic operations, caregiving, relationship labor, civic/school labor, transport logistics, social administration, and economic dependency.

## Product Risks

### Efficiency Without Justice

If Pancakes only helps her plan, remind, and optimize, it may make an unfair arrangement more durable.

The product should ask:

```text
Who is carrying this?
Who benefits?
Who has choice?
Who has rest?
Who has money, mobility, and exit capacity?
```

### Surveillance By Household Members

Shared household dashboards can become tools of control.

Avoid:

- exposing private reflections to a spouse or household steward;
- showing every incomplete task as failure;
- making emotional depletion visible to someone unsafe;
- letting one household member monitor another's domestic output;
- requiring proof of household work through sensors, photos, or location traces.

### Rewarding Her For Staying Overloaded

Pitchfork rewards must not create incentives to keep taking on unfair work.

Avoid:

- infinite rewards for doing more domestic labor;
- spouse-visible streaks;
- public chore prestige;
- economic conversion from intimate labor by default;
- rewards that make overload look like excellence.

### Misclassifying The Problem

The issue is not merely "laundry" or "carpool." It is accumulated dependency, unequal recognition, constrained choice, and loss of self.

The model needs support signals for load and agency, not just task categories.

## Pancakes Support Model

Pancakes should support her through private, human-facing tools.

### 1. Private Load Inventory

Help her see the full scope of what she carries.

Categories:

- food;
- laundry and textiles;
- cleaning and presentation;
- child logistics;
- school and civic obligations;
- health appointments;
- transportation;
- social correspondence and holidays;
- spouse or partner support;
- household administration;
- emotional labor;
- planning and anticipation;
- financial dependency risk.

The inventory should be private by default. Sharing should be explicit and reversible.

### 2. Fairness Review

Provide a household load review that can be used privately first.

Review prompts:

- Which tasks happen only because she remembers them?
- Which responsibilities would fail if she stopped?
- Which tasks are visible to others?
- Which tasks are assumed rather than agreed?
- Which tasks are connected to child, health, money, or safety risk?
- Which responsibilities could be transferred, rotated, outsourced, simplified, or stopped?

The output should avoid moral scoring. It should produce a practical map of load and options.

### 3. Rest And Depletion Support

Track depletion as a private wellbeing signal, not as a household performance metric.

Useful states:

- rested;
- stretched;
- overloaded;
- depleted;
- resentful;
- numb;
- unsafe to discuss openly;
- needs outside support.

These should never be shared into household dashboards by default.

### 4. Economic Continuity Review

Support the financial risk created by long-term unpaid domestic labor.

Possible tools:

- personal document checklist;
- work history reconstruction;
- skills inventory from household labor;
- income and expense visibility;
- separate emergency fund planning where safe;
- benefit, training, employment, and legal-resource reminders;
- exportable personal timeline;
- private transition plan.

This should be framed as autonomy and continuity, not as advice to leave or stay.

### 5. Transition Planning

Support major life transitions carefully.

Transitions may include:

- renegotiating household labor;
- returning to paid work;
- separating finances;
- seeking counselling or mediation;
- leaving a relationship;
- moving;
- changing custody or care arrangements;
- rebuilding identity after long domestic service.

The system should keep transition planning private unless she chooses otherwise.

### 6. Outside Support

The app should make it easy to identify safe support channels:

- trusted friends;
- family;
- counsellors;
- legal clinics;
- employment services;
- domestic violence resources where relevant;
- financial counsellors;
- childcare supports;
- community groups;
- mutual-aid circles.

Do not assume the situation is abusive, but design so the safer path exists if it is.

## Pitchfork Support Model

Pitchfork should receive only minimized, permissioned events or covenants.

### Event Types

Candidate event types:

```text
household_admin_completed
transport_support_completed
appointment_logistics_completed
school_community_support_completed
social_correspondence_completed
travel_prep_supported
adult_support_labor_completed
care_load_reviewed
rest_need_acknowledged
life_transition_supported
economic_continuity_reviewed
household_labor_redistribution_covenant_ratified
household_labor_redistribution_covenant_settled
```

These events should usually be `personal`, `household`, or `sensitive` depending on context.

### Sensitive Defaults

The following should default to `sensitive`:

- emotional depletion;
- relationship dissatisfaction;
- financial vulnerability;
- transition planning;
- legal or counselling support;
- safety planning;
- household conflict;
- private load inventories;
- child or custody implications.

### Symbolic Materials

Possible symbolic resources:

| Material | Meaning |
| --- | --- |
| Hearthlight | care that keeps daily life warm and fed |
| Order Salt | cleaning, laundry, timing, and domestic order |
| Mending Thread | repair, logistics, and continuity work |
| Road Dust | transportation, errands, appointments, and carpooling |
| Ledger Dust | paperwork, bills, records, and administrative labor |
| School Chalk | school, PTA, child-development, and civic-parent work |
| Memory Ink | holiday cards, social continuity, family records |
| Threshold Wax | boundary setting, safety, privacy, and transition protection |
| Rest Ash | recovery after overload |
| Mirror Shard | seeing the pattern clearly after years of invisibility |

Mirror Shard should be used carefully. It represents recognition and clarity, not punishment or blame.

### Covenants

The core Pitchfork tool should be a redistribution covenant, not a chore reward loop.

Example:

```text
Covenant: Make the Household Load Visible
Purpose: Identify and redistribute recurring household operations.
Participants: Household adults, where safe and consented.
Steward: The person requesting review, or a mutually trusted steward.
Witness rule: Self-attestation plus optional participant acknowledgement.
Settlement rule: Load inventory completed; two responsibilities reassigned or explicitly retired.
Reward rule: Household Continuity +1; Threshold Wax +1; no public sharing.
Privacy boundary: Household or private, chosen by initiating person.
```

For unsafe or high-conflict situations, use a private covenant:

```text
Covenant: Preserve My Future Capacity
Purpose: Build personal continuity and transition options.
Participants: Initiating person only.
Witness rule: Self-attested.
Settlement rule: Documents gathered, support contact identified, next step chosen.
Reward rule: Mirror Shard +1; Threshold Wax +1.
Privacy boundary: Private.
```

## UX Requirements

### Private First

Any recognition of invisible labor should begin privately.

The user can later choose to:

- keep it private;
- export it;
- share a summary;
- invite household review;
- create a covenant;
- seek outside support.

### No Automatic Spouse View

There should be no automatic household-owner or spouse-level visibility.

Household membership is not consent to see intimate records.

### No Productivity Tone

Avoid language such as:

```text
You completed 97% of wife tasks this week.
Your household output increased.
You are falling behind on domestic duties.
```

Prefer:

```text
You carried many kinds of work this week.
Some of this load may need support.
This routine depends heavily on you.
You may want a private review before sharing anything.
```

### Agency-Oriented Options

The product should offer choices:

- keep going with more support;
- simplify;
- redistribute;
- pause;
- ask for help;
- make a plan;
- document skills;
- prepare for transition;
- create a covenant;
- export a record.

It should not imply there is one correct life decision.

## Implementation Notes

### First Pancakes Feature

Build a private "Invisible Household Load" review.

Minimum fields:

```text
LoadItem
- id
- category
- description
- frequency
- who_benefits
- who_knows
- who_can_do_it
- transfer_possible
- stop_possible
- risk_if_dropped
- emotional_cost_band
- privacy_level
```

The output should be a private summary:

```text
You are carrying food, laundry, transport, school, appointment, social, and admin work.
Several items are invisible unless they fail.
Some items could be reassigned, simplified, or retired.
Some items may affect money, children, health, or safety and need careful handling.
```

### First Pitchfork Event

Record only a minimized completion:

```json
{
  "event_type": "care_load_reviewed",
  "data_class": "sensitive",
  "permission_scope": "private",
  "attestation_method": "self_attested",
  "measures": {
    "domain": "household_labor",
    "review_type": "private_load_inventory",
    "detail_level": "summary_only"
  },
  "projection_intent": ["pitchfork_rpg_private"]
}
```

### First Projection

Private RPG projection:

```text
You found a Mirror Shard beneath the polished floor.
It shows the work that held the house together.
```

This should be private, gentle, and optional.

## Safety Review

Before shipping shared household features, review:

- Can an unsafe partner discover private transition planning?
- Can a household member demand proof or access?
- Can task data be used in custody, conflict, employment, or financial coercion?
- Can children or dependents be exposed through household records?
- Can a support feature accidentally advise someone into danger?
- Are exports clear about what they include?
- Are audit logs helpful without creating another surveillance trail?

## Success Criteria

The design is succeeding if it helps someone:

- name invisible work;
- feel less alone in the pattern;
- protect private reflection;
- identify support options;
- reduce or redistribute load;
- preserve future capacity;
- document transferable skills;
- make a transition plan if needed;
- share only what they choose to share.

It is failing if it:

- makes her more efficient without increasing agency;
- exposes private dissatisfaction;
- rewards overload;
- turns domestic labor into a spouse-visible score;
- treats unpaid care as an infinite resource;
- pressures her toward staying, leaving, sharing, or performing.

## Summary

To support the singer, Pancakes should help her see and protect herself inside the household system she has been maintaining.

Pitchfork should recognize selected moments of household labor, review, redistribution, and transition as meaningful symbolic events, while keeping the raw truth private.

The goal is not to keep the house polished.

The goal is to keep the person whole.
