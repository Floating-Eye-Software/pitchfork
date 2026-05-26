# Pitchfork Node Quality of Life Signals

## Purpose

This document defines a possible Pancakes/Pitchfork node service for tracking aggregate quality-of-life conditions across a node.

The idea is hypothetical but important:

> If many Pancakes apps are running against the same governing node, the node can derive an ambient, aggregate view of whether life on that node is becoming more supported, strained, resilient, or fragile.

This should be a governance and support feature, not an analytics product.

The node should not ask:

```text
Is this person valuable?
Is this household productive enough?
Who has the best quality-of-life score?
```

It should ask:

```text
Is this node becoming more livable?
Where are support gaps emerging?
Which domains are under stress?
Are benefits and burdens distributed fairly?
Are node policies improving conditions over time?
```

## Reference Model

The public-policy anchor is Statistics Canada's Quality of Life Framework for Canada:

https://www.statcan.gc.ca/hub-carrefour/quality-life-qualite-vie/index-eng.htm

The framework organizes quality of life around:

- Central indicators: life satisfaction, sense of meaning and purpose, and future outlook.
- Domains: prosperity, health, society, environment, and good governance.
- Cross-cutting lenses: fairness and inclusion, and sustainability and resilience.

Pitchfork should use this as a design compass and taxonomy, not as a scoring formula.

## Core Concept

A node can run a service that observes permissioned activity across Pancakes clients and produces slow-moving aggregate signals.

Possible service names:

- Node Quality of Life Service.
- Node Wellbeing Observatory.
- Quality of Life Steward.
- Ambient Node Health.

The best early name is probably **Node Quality of Life Service** because it is plain and governance-oriented.

The service consumes consented, node-local events such as:

- Service requests.
- Service completions.
- Unmet needs.
- Household covenants.
- Care tasks.
- Budget stress markers.
- Food, transport, housing, or scheduling support requests.
- Safety incidents.
- Disputes.
- Time-use strain.
- Volunteering or contribution records.
- Local resource availability.
- Optional subjective check-ins.
- Environmental or preparedness events.

It produces aggregate signals such as:

- Prosperity is strained.
- Care support is improving.
- Time pressure is high.
- Food support requests are rising.
- Service completion is stable but concentrated among too few members.
- Safety incidents need review.
- The node is resilient in ordinary weeks but fragile during shocks.

## Ambient Value

Quality of life should be an ambient node value, not a foreground productivity metric.

Ambient means:

- It is derived in the background from many small signals.
- It updates slowly, usually over weeks or months.
- It is interpreted at domain level, not person level.
- It appears in governance, planning, and support surfaces.
- It does not interrupt users with constant optimization prompts.
- It does not become a game score, credit multiplier, insurance proxy, or eligibility gate.

The node should express quality-of-life state with qualitative language:

- Stable.
- Improving.
- Strained.
- Fragile.
- Under-supported.
- Overburdened.
- Needs review.
- Unknown.

Avoid:

- Global scores.
- Household rankings.
- Personal wellness ratings.
- Provider productivity scores.
- Public dashboards with small cohorts.
- Predictive labels about individual people.

## Data Boundary

This feature only makes sense if the data boundary is clear.

```text
Raw client data
-> consented derived event
-> node-local aggregate signal
-> privacy-thresholded quality-of-life snapshot
-> governance action
```

Raw records should stay with the originating client or under the node's normal storage and permission policy.

The Quality of Life Service should prefer minimal derived events:

```text
service_request_created
support_need_unmet
care_task_completed
budget_stress_reported
appointment_transport_requested
meal_support_fulfilled
dispute_opened
incident_closed
future_outlook_checkin_submitted
```

It should not require raw journal text, exact location history, private health details, bank transactions, message contents, or household conflict notes unless there is a separate, explicit, high-trust permission grant.

## Aggregate Only

The service should report only when aggregation thresholds are met.

Minimum safeguards:

- Minimum cohort size before reporting.
- Minimum event count before reporting.
- Time-window smoothing.
- Suppression of rare sensitive categories.
- No drill-down to individual users by default.
- No export of raw contributing records through QoL reports.
- Redaction of notes and payloads from governance views.
- Separate handling for children, dependents, health-adjacent data, domestic-safety contexts, and small communities.

Small nodes create special risk.

A household node may have too few people for meaningful anonymized aggregate reporting. In that case the feature should operate as a private household review tool, not as "anonymous analytics."

## Domain Mapping

### Central Indicators

Central indicators are subjective and should be self-reported.

Possible signals:

- Optional life satisfaction check-ins.
- Optional meaning and purpose check-ins.
- Optional future outlook check-ins.
- Household or node reflections after review periods.

Guardrails:

- Do not infer subjective well-being from chores, spending, sleep, location, or service use alone.
- Do not expose individual central indicators to node administrators by default.
- Do not make subjective well-being a condition for rewards, credits, or help.

### Prosperity

Possible signals:

- Budget stress.
- Food support requests.
- Housing support requests.
- Internet/device access support.
- Employment or scheduling instability.
- Emergency fund or income-shock requests.
- Service-credit liquidity within the node.

Node actions:

- Add mutual-aid resources.
- Sponsor grocery, transport, or childcare support.
- Adjust credit rules.
- Create emergency support pools.
- Surface public benefits or local resources.

### Health

Possible signals:

- Meal support needs.
- Movement, rest, or medication routine support where consented.
- Appointment transport requests.
- Home-care logistics.
- Unmet care tasks.
- Burnout or overload check-ins.

Node actions:

- Coordinate rides.
- Organize meal support.
- Reduce demand on overburdened caregivers.
- Improve consent flows for care circles.
- Connect members to appropriate external resources.

Pancakes is not a medical system by default. Health-adjacent signals should remain support-oriented unless a specialized regulated mode is deliberately designed.

### Society

Possible signals:

- Someone-to-count-on support maps.
- Service exchange density.
- Volunteering.
- Trust relationships.
- Local events.
- Loneliness or isolation check-ins.
- Uneven contribution burden.
- Time-use strain.

Node actions:

- Create circles for new members.
- Recruit more service providers.
- Reduce over-contribution pressure.
- Support social events or quiet help channels.
- Review whether service exchange is becoming coercive.

### Environment

Possible signals:

- Local resource availability.
- Transit or transport barriers.
- Weather, smoke, heat, outage, or emergency events.
- Repair, reuse, gardening, food, and waste-reduction activity.
- Walkability or location-access barriers where safely reported.

Node actions:

- Improve preparedness plans.
- Coordinate local pickup or shared rides.
- Support repair and reuse circles.
- Maintain emergency resource lists.
- Adjust expectations during environmental stress.

### Good Governance

Possible signals:

- Disputes.
- Safety incidents.
- Moderation actions.
- Unresolved complaints.
- Rule changes.
- Appeals.
- Consent revocations.
- Trust in node governance.

Node actions:

- Review policies.
- Open corrective actions.
- Change steward/custodian roles.
- Improve dispute handling.
- Publish non-sensitive governance summaries.
- Audit whether rules are being applied fairly.

## Fairness And Inclusion Lens

Quality-of-life signals are incomplete unless the node asks who benefits and who carries burden.

The service should support fairness review without exposing personal identities unnecessarily.

Fairness questions:

- Are support requests concentrated in one group?
- Are service burdens concentrated in one group?
- Are low-income members spending credits faster than they can earn them?
- Are disabled, rural, elder, youth, caregiver, newcomer, or low-bandwidth users able to participate?
- Are people with less social status less likely to receive help?
- Are privacy-sensitive users excluded because they refuse broad sharing?

The node should treat uneven distribution as a governance signal, not as a user defect.

## Sustainability And Resilience Lens

The node should also ask whether support is durable.

Resilience questions:

- Does the node still function during illness, conflict, outage, weather events, or financial stress?
- Are a few people carrying too much of the work?
- Are service credits accumulating in ways that make exchange brittle?
- Are households becoming more capable, or more dependent on one coordinator?
- Are emergency plans tested?
- Can members leave, export, pause, or change nodes without losing essential support?

Resilience is not maximum activity. A node can be busy and fragile.

## Example Flows

### Meal Support Pressure

```text
Many households request meal help, grocery rides, and budget relief.
-> Prosperity and Health are marked strained.
-> Society is checked for provider burden.
-> Node reviews food support capacity.
-> Node creates a meal-prep circle and grocery ride schedule.
-> Next review checks whether unmet food requests decline.
```

### Uneven Contribution

```text
Completed services are high.
The same small group completes most of them.
Disputes are low, but rest check-ins are worsening.
-> Society appears active but fairness and resilience are weak.
-> Node recruits more providers, throttles over-contribution rewards, and adds rest periods.
```

### Safety And Trust

```text
Two service disputes and one safety incident occur in a month.
Small cohort size prevents public reporting.
-> Good Governance is marked needs review internally.
-> Steward opens a policy review.
-> QoL public summary says only that service safety rules were reviewed.
```

### Household Node

```text
A household node has four members.
Anonymized aggregate reporting is not meaningful.
-> QoL service runs as a private family review surface.
-> It shows support gaps, overloaded routines, and consented reflections.
-> No claim of anonymity is made.
```

## Data Model Sketch

```text
NodeQoLSignal
  id
  node_id
  domain
  subdomain
  source_event_type
  aggregation_window
  direction
  state
  confidence
  privacy_threshold_met
  created_at

NodeQoLSnapshot
  id
  node_id
  period_start
  period_end
  central_state
  prosperity_state
  health_state
  society_state
  environment_state
  governance_state
  fairness_state
  resilience_state
  summary
  suppressed_fields
  review_status

NodeQoLReview
  id
  snapshot_id
  reviewer_actor_id
  decisions
  actions
  risks_opened
  policy_changes
  published_summary
  reviewed_at
```

Signal state values should remain qualitative:

```text
unknown
stable
improving
strained
fragile
under_supported
overburdened
needs_review
```

## API Shape

The node API could expose a trusted service boundary like:

```text
POST /node/qol/events
GET /node/qol/snapshots/current
GET /node/qol/snapshots/{period}
POST /node/qol/reviews
GET /node/qol/public-summary
```

These endpoints should be node-local or trusted-service-only at first.

Public or federated sharing should come later and should expose only privacy-thresholded summaries.

## Relationship To Pitchfork

Pitchfork can project node quality-of-life state symbolically.

Examples:

- A guild sanctuary becomes warmer when care support stabilizes.
- A settlement district looks strained when unmet needs rise.
- A covenant board highlights resource gaps.
- A council chamber shows governance review needs.
- Environmental stress appears as weather or terrain pressure.

Projection should remain ambiguous and symbolic. It should not reveal private node metrics or let players infer sensitive facts about specific households.

QoL state can inform:

- Guild quests.
- Cooperative pool priorities.
- Node stewardship rituals.
- Service board prompts.
- Seasonal review.
- Public-good projects.

QoL state should not directly create uncapped rewards.

## Risks

### Surveillance Drift

Aggregate support metrics can become individual surveillance if administrators can drill down too far.

Controls:

- Strict aggregation thresholds.
- No individual drill-down by default.
- Separate incident and support workflows.
- Audit access to sensitive contributing records.

### Score Reification

Users and admins may start treating the ambient state as objective truth.

Controls:

- Use qualitative states.
- Show uncertainty.
- Preserve narrative review.
- Avoid global composite scores.

### Coercion

Members may feel pressured to share more data because the node says it needs better QoL measurement.

Controls:

- Essential participation must not require broad sharing.
- Use minimal derived events.
- Let users opt out of sensitive domains.
- Make missing data visible as missing, not bad.

### Small Cohort Exposure

Small nodes cannot anonymize many signals.

Controls:

- Suppress reports.
- Use household-review mode.
- Avoid false anonymity claims.
- Require explicit visibility settings.

### Institutional Misuse

An employer, school, insurer, landlord, or agency could misuse QoL outputs.

Controls:

- Disable external sharing by default.
- Contractually and technically limit exports.
- Separate support planning from eligibility decisions.
- Maintain node governance logs for any external data product.

## First Version

The first version should be boring and local.

Build:

- Domain tags on events.
- A small set of aggregate counters.
- Manual node review.
- Suppression thresholds.
- Qualitative states.
- A non-sensitive summary page.

Do not build:

- Personal QoL scores.
- Predictive risk scores.
- Public dashboards.
- Automated sanctions.
- Automated eligibility decisions.
- Cross-node benchmarking.
- Sponsor-facing analytics.

## Open Questions

- Which clients are allowed to submit QoL-relevant events?
- Does each node choose its own domain weights, or are weights avoided entirely?
- What minimum cohort size is required for each signal type?
- Can household nodes use this without pretending to anonymize data?
- Who can publish a public node summary?
- How are member objections, consent revocations, and disputed interpretations handled?
- Can a node prove that a published aggregate did not expose sensitive members?
- How should Quality of Life Service records appear in node export/import?

## Working Assumption

Node quality of life should be a stewardship signal.

It exists to help a community notice stress, allocate support, review policy, and build resilience.

It should not become a measurement regime that ranks people, extracts intimate data, or lets a node optimize members for productivity.
