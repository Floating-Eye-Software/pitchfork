# Pancakes Node Infrastructure

## Purpose

Pancakes should be able to run as more than a hosted service.

The hosted domains can provide convenient public entry points:

- `pancakes.ca`: stable public app.
- `pancakes.love`: experimental, cooperative, or blockchain-connected environment.

But the long-term architecture should also support self-hosted Pancakes nodes for families, households, guilds, circles, cooperatives, clinics, schools, mutual-aid groups, and other communities that need stronger control over data, governance, and value boundaries.

## Core Idea

A Pancakes node is a locally controlled server that runs the Pancakes human layer and selected Pitchfork accounting primitives for a bounded group.

It should let a group retain control over:

- Personal logs.
- Household or guild records.
- Ritual history.
- Materials, essences, and crafted items.
- Covenants and commitments.
- Cooperative pools.
- Permissions and membership.
- Local policies.
- Backups and export.
- Whether any data ever leaves the group.

The node can be open source infrastructure. A group should be able to stand up its own instance without depending on `pancakes.ca`, `pancakes.love`, Google, Meta, or other large platform infrastructure.

## Why This Matters

Pancakes and Pitchfork handle unusually intimate data:

- Rest.
- Health-adjacent patterns.
- Care work.
- Household labor.
- Mood and reflection.
- Relationship maintenance.
- Mutual aid.
- Financial or cooperative support.
- Future crypto-adjacent state.

That data should not be forced into a centralized platform by default.

Self-hosted nodes support:

- Privacy.
- Local ownership.
- Consent.
- Data minimization.
- Value segmentation.
- Community governance.
- Exit rights.
- Resilience.
- Cultural adaptation.
- Reduced dependency on extractive infrastructure.

## Terminology

The best umbrella term is probably **community data stewardship**.

Related terms:

- **Data trust**: a legal or governance structure where trustees steward data or data rights for beneficiaries.
- **Civic data trust**: a public-interest or community-oriented version of data-trust governance.
- **Data cooperative**: a member-owned structure for pooling and governing data.
- **Data commons**: shared data governed for collective benefit.
- **Data steward**: a person or body responsible for managing data according to agreed rules.
- **Data custodian**: the operator responsible for technical care, storage, security, and continuity.
- **Digital commons infrastructure**: open infrastructure that supports shared civic or community control.

`Privacy trust` is understandable as a phrase, but `data trust` and `civic data trust` are more established terms. For Pancakes, the product language can stay simpler:

> A Pancakes node is a community-run home for private life data.

The governance language can be:

> Pancakes nodes should be capable of operating as community data trusts, data cooperatives, or local data commons, depending on the legal and social structure of the group.

## Node Types

### Personal Node

For one person.

Goals:

- Local-first logging.
- Personal archive.
- Private ritual history.
- Optional sync to hosted Pancakes.

### Household Node

For a family, household, or chosen household.

Goals:

- Shared household stewardship.
- Private family records.
- Care coordination.
- Household resources and rituals.
- Strong consent boundaries between members.

### Guild Node

For a game group, mutual-aid circle, club, school group, or community.

Goals:

- Shared rituals.
- Guild vaults.
- Cooperative pools.
- Local governance.
- Group covenants.
- Optional federation with other nodes.

### Institutional Node

For clinics, schools, nonprofits, cooperatives, or care organizations.

Goals:

- Strict privacy controls.
- Role-based access.
- Audit trails.
- Policy enforcement.
- Legal compliance.
- Clear separation between personal, group, and institutional data.

## Federation

Pancakes nodes should not require federation at first.

The first architecture can support:

- Standalone local nodes.
- Export and import.
- Manual backup.
- Optional hosted sync later.

Federation can come later when the local data model is stable.

Future federation questions:

- Can two households share selected covenant state?
- Can guilds trade crafted items without exposing personal logs?
- Can a Pancakes node publish only aggregate public signals?
- Can a user move from one node to another with a complete export?
- Can hosted Pancakes act as one node among many rather than the central authority?

## Data Boundaries

A Pancakes node should distinguish:

- Private personal data.
- Household-shared data.
- Guild-shared data.
- Public or published data.
- Economic or treasury data.
- Sensitive health or cycle data.
- Future wallet or crypto-facing data.

Default rule:

> Raw personal logs stay private unless explicitly shared.

Derived state can be shared more safely:

- "A ritual was completed."
- "A material was contributed."
- "A covenant condition was satisfied."
- "A pool received a contribution."

But even derived state can reveal patterns, so sharing should be intentional, scoped, and reversible where possible.

## Governance Model

Each node should have a governance file or admin surface that answers:

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

For a trust-like node, distinguish:

- **Members**: people whose data and participation the node exists to serve.
- **Stewards**: people or bodies responsible for governance decisions.
- **Custodians**: people or operators responsible for technical operation.
- **Beneficiaries**: people or groups the node is obligated to benefit.

One person can hold more than one role in a small household node, but the roles should still be conceptually separate.

## Anti-Oligarchy Direction

The long-term aspiration is not only privacy.

Pancakes nodes can be part of a broader replacement pattern for extractive platform infrastructure:

- Local ownership instead of platform dependency.
- Open source software instead of opaque SaaS lock-in.
- User-held exports instead of trapped histories.
- Community governance instead of unilateral terms of service.
- Cooperative pools instead of ad-funded behavioral extraction.
- Local-first operation where possible.
- Federation or interoperability instead of centralized network capture.

This does not require rejecting hosted Pancakes. Hosted Pancakes can remain useful for convenience, onboarding, and people who cannot run infrastructure.

But hosted Pancakes should not become the only legitimate place where Pancakes can exist.

The broader doctrine is described in [Non-Exploitative Infrastructure](non_exploitative_infrastructure.md).

## Collective Data Value

A distant-future Pancakes node could let a group earn value from aggregate data.

The premise is:

> If data has economic value, the value should be able to flow back to the people and communities who produced it, not only to large platforms, brokers, advertisers, insurers, or analytics companies.

This must not mean selling raw personal logs.

Acceptable future direction:

- A household, guild, cooperative, or community chooses to publish or sell an aggregate data product.
- Members understand what is being shared.
- Members can opt in or opt out.
- Sensitive domains are excluded by default.
- Raw personal records stay inside the node.
- Buyers receive only scoped, minimized, aggregate outputs.
- Revenue terms are visible to members.
- Value is distributed through a clear local governance model.
- A group can refuse extractive buyers.
- A group can revoke future access.

Examples of possible aggregate outputs:

- Participation trends.
- Recipe or ritual completion patterns.
- Anonymous product feedback.
- Community-level wellness or care indicators.
- Household-stewardship burden summaries.
- Guild-level economic or crafting activity.

These should be treated as **data products**, not casual exports.

Each data product should define:

- Purpose.
- Buyer or recipient.
- Included fields.
- Excluded fields.
- Aggregation threshold.
- Re-identification risk.
- Consent model.
- Expiration date.
- Revenue distribution.
- Audit trail.

## Aggregate Data Guardrails

Aggregate data can still harm people.

Risks:

- Re-identification.
- Small-group exposure.
- Buyer misuse.
- Pressure from household or guild leaders.
- Selling sensitive health, cycle, fertility, location, or financial patterns.
- Communities becoming dependent on data sales.
- Turning participation into a new extraction pipeline.

Guardrails:

- No sale of raw personal logs.
- No sale of sensitive health or reproductive data by default.
- Minimum group-size thresholds before any aggregate export.
- Differential privacy or similar protections where appropriate.
- Member-level opt-in for each data product.
- Plain-language explanations of risks.
- Independent review for high-stakes data products.
- Node-level buyer allowlists or denylists.
- Public ledger of data products sold by the node.
- Strong exit rights for members who do not consent.

The key distinction:

```text
bad: people generate data -> platform sells it -> platform captures value
better: community governs data -> community chooses scoped use -> community captures value
```

## Product Validation and Research Markets

Another distant-future use case is group-mediated product validation.

A company might ask a guild, household network, cooperative, or community node to test or validate a product.

Low-stakes examples:

- Does this household planning tool reduce scheduling friction?
- Does this recipe app help families plan meals?
- Does this educational game help a study guild stay engaged?
- Does this ergonomic object improve subjective comfort?

This can be a legitimate cooperative research market if it remains voluntary, scoped, compensated, and governed by the node's members.

It becomes much more sensitive when the product touches:

- Health.
- Mental health.
- Fertility or cycles.
- Children.
- Disability.
- Medication.
- Medical devices.
- Diagnosis or treatment.
- Vulnerable populations.

Those cases need a regulated research pathway, not ordinary guild validation.

## Clinical Trial Mode

Clinical trials are not normal Pancakes activity.

If Pancakes nodes ever support clinical trials or health-product validation, that should be a specialized, regulated mode with separate safeguards.

Minimum assumptions:

- Independent ethics review.
- IRB or equivalent review where required.
- Informed consent.
- Clear sponsor identity.
- Clear investigator responsibilities.
- Protocol registration where required.
- Eligibility criteria.
- Adverse-event reporting.
- Data safety monitoring where appropriate.
- Separation from ordinary gameplay rewards.
- No coercion through guild status, household pressure, or economic dependency.
- Extra protections for children, disabled people, pregnant people, patients, and other vulnerable groups.
- No hidden secondary use of health data.

Pancakes should not present clinical trial participation as a game quest.

The user-facing frame should be closer to:

> This is a research study. It is separate from ordinary Pancakes play. Participation is voluntary and governed by a reviewed protocol.

Possible node role:

- Recruiting eligible members who opt in to research opportunities.
- Managing consent records.
- Holding participant data locally until transfer is explicitly approved.
- Providing aggregate or de-identified results under protocol.
- Distributing compensation transparently.
- Auditing sponsor access.

The node should protect members from sponsors, not merely supply members to sponsors.

## Revenue Distribution

If a node earns money from aggregate data or research participation, distribution should be explicit.

Possible models:

- Equal member dividend.
- Contributor-weighted distribution.
- Cooperative treasury allocation.
- Household support fund.
- Mutual-aid pool.
- Node maintenance fund.
- Participant-only compensation for regulated studies.

The correct model depends on context.

For clinical trials or human-subjects research, compensation should follow the approved study protocol and should not be laundered through game rewards.

For aggregate data products, the node should disclose:

- Gross payment.
- Fees.
- Treasury allocation.
- Member distribution.
- Any steward or custodian compensation.
- Any retained funds.

## Hard Lines

Pancakes nodes should not support:

- Secret data sales.
- Retroactive consent.
- Broad consent hidden in terms of service.
- Raw personal-log resale.
- Health-data resale to advertisers.
- Insurance, employment, credit, or policing uses.
- Sponsor access to private household data.
- Pay-to-pressure clinical participation.
- Guild leaders coercing members into research.
- Selling data from children or dependents without special protections.

## Architecture Implications

Pancakes and Pitchfork should be designed so that:

- The core accounting layer can run locally.
- The hosted app is not privileged in the data model.
- Identity can be local first.
- Export is a first-class feature.
- Import is a first-class feature.
- Backups are simple.
- Secrets and keys are not centralized unnecessarily.
- Node-to-node communication is optional and permissioned.
- Personal data and economic state can be separated.
- Sensitive domains can be disabled at the node level.

Early implementation should not attempt full decentralized infrastructure. The practical first step is:

```text
single local Pancakes node
-> local database
-> local users
-> local Pitchfork accounting module
-> export/import
-> optional hosted deployment
```

## Node Appliance

Earlier exploration imagined a preconfigured Pancakes node appliance: a small, inexpensive computer that a household, guild, or community could plug in at home.

This remains a useful adoption path.

Possible appliance traits:

- Low-power mini-computer.
- Preinstalled Pancakes node software.
- Guided setup.
- Local web dashboard.
- Automatic updates.
- Local backup.
- Export tools.
- Clear health/status indicators.
- Optional mesh or federation support later.

The appliance should lower the operational burden for nontechnical groups. It should not become the only way to run a node.

## Mesh Direction

Pancakes nodes may eventually form local or internet-connected meshes.

Possible uses:

- Neighborhood service discovery.
- Redundant local infrastructure.
- Shared job-board listings.
- Cross-household covenants.
- Guild coordination.
- Community event support.

This is a distant direction. The first node should work as a standalone local server before Pancakes attempts resilient mesh networking.

## Open Questions

- Should a Pancakes node be packaged as Docker Compose, a Python package, a small appliance image, or all three?
- Should a node expose ActivityPub, AT Protocol, Matrix, or no federation protocol at first?
- What is the minimum viable export format?
- Can a person belong to multiple nodes?
- How does identity work when someone leaves a household or guild?
- Can a child or dependent have data rights that override household admins?
- How do cooperative pools avoid coercion by local administrators?
- What legal forms make sense for different node operators?
- When does a node become a data controller, trustee, cooperative, or fiduciary?
- How do nodes prove they are running trustworthy open source code?

## Working Assumption

The first Pancakes node should be boring, local, and practical.

It should prove that ordinary people can run a private Pancakes instance for a small group, retain their data, and use Pitchfork primitives without depending on centralized infrastructure.

The trust, cooperative, federation, and crypto layers should grow only after the local node model is understandable and safe.
