# Pancakes Service Exchange

## Purpose

Pancakes began partly as an app for mutual service exchange.

The original problem:

> Overworked people often buy services from large companies because grassroots exchange with peers is hard to coordinate.

Pancakes can make informal care, household work, transportation help, tutoring, cooking, cleaning, errands, repair, and other ordinary services easier to exchange without forcing every exchange through a corporate gig platform.

## Core Idea

Pancakes should support direct and indirect service exchange.

Direct exchange:

```text
I cook for you.
You clean for me.
```

Indirect exchange:

```text
I help one household.
I earn Pancakes credits.
I spend those credits later with another person or household.
```

The indirect model is important because it removes the need for perfect one-to-one reciprocity. A person can contribute where they are able and receive help from someone else later.

## Service Categories

Initial categories could include:

- Cooking.
- Cleaning.
- Laundry.
- Childcare.
- Eldercare.
- Pet care.
- Gardening.
- Tutoring.
- Transportation.
- Errands.
- Repair.
- Scheduling and organizing.
- Meal planning.
- Emotional support.
- Community work.

The old design also imagined reviving traditional or underrecognized professions as service identities:

- Baker.
- Brewer.
- Tailor.
- Cobbler.
- Herbalist.
- Blacksmith.
- Gardener.
- Tutor.
- Household manager.
- Care worker.
- Driver.
- Repairer.

This should be handled with respect. The point is not nostalgia for hierarchy. The point is to make useful local skills visible again.

## Job Board

Pancakes can include a local job board.

Users can post:

- Services offered.
- Services requested.
- Urgent needs.
- Scheduled needs.
- Recurring household support.
- Group projects.
- Community events.

Listings should support:

- Category.
- Location scope.
- Time estimate.
- Credit or money price.
- Direct barter option.
- Required trust level.
- Safety notes.
- Visibility settings.
- Expiration.

## Pancakes Credits

Pancakes credits are a local accounting unit for service exchange.

Uses:

- Earned by providing services.
- Spent to receive services.
- Held in a wallet.
- Transferred between members or nodes under local rules.
- Used by Pitchfork later as a symbolic or economic input.

Credits should not start as real money.

Early credits should be:

- Internal.
- Local.
- Capped or rate-limited where needed.
- Non-speculative.
- Clear about what they do and do not represent.

The credit system should avoid pretending that every form of care has a perfect market price. Credits are coordination tools, not a complete theory of human value.

## Ratified Household Covenants

Household chores and care work can be represented as covenants.

A household node can ratify a covenant so it becomes recognized by that household's local accounting rules.

Example:

```text
Covenant: Keep the Kitchen Clear
Members: Alex, Sam
Promise: Dishes cleared after dinner three times this week.
Ratified by: Household Steward
Witness: Either member can attest; steward resolves disputes.
Reward: Household stability +2, Order Salt +1 each
Boundary: No public sharing outside the household node
```

Ratification means:

- The covenant is legitimate within the household.
- The affected people had a chance to understand it.
- Rewards or credits can be issued under local rules.
- The privacy boundary is clear.
- Disputes have a resolution path.

Prefer **steward ratification** for social approval. Use **custodian** for technical operation unless the same person holds both roles.

## Pancakes Earth

Pancakes Earth is the geospatial layer of Pancakes.

It can show real-world service availability with strong privacy controls.

Possible features:

- Map of nearby services.
- Service markers with metadata.
- Optional user availability.
- Local events.
- Nearby help requests.
- Community resource locations.
- Household or guild territory.
- Augmented-reality overlays later.

Examples:

- A person needs help assembling furniture and sees a nearby repair marker.
- A tutor marks themselves available at a library.
- A household posts a gardening day for neighbors.
- A guild coordinates a local cleanup or meal-prep event.

Location data is sensitive.

Default rules:

- Location sharing is off by default.
- Users can share approximate location instead of exact location.
- Users can be visible only while actively offering or requesting help.
- Personal home locations should not be exposed casually.
- Children, dependents, health contexts, and domestic-safety contexts need special protections.

## BLE and Proximity

Mobile apps could use Bluetooth Low Energy for nearby discovery.

Possible uses:

- Detect nearby Pancakes users who have opted into discovery.
- Show nearby service offers without publishing a precise map location.
- Support event check-ins.
- Let a group coordinate services at a market, school, library, festival, or community center.

BLE discovery should reveal the minimum necessary information.

Safer defaults:

- Opt-in only.
- Temporary visibility.
- Service-first display, not identity-first display.
- No persistent proximity history by default.
- Easy panic/off switch.

## Mesh and Local Infrastructure

The service exchange design connects to Pancakes nodes.

Earlier exploration imagined:

- Home servers.
- Local mesh networks.
- Nodes that provide computing services for a community.
- Nodes that connect locally and over the internet.
- Preconfigured mini-computer nodes around a low price point.

This remains useful as a distant infrastructure direction.

Near-term:

- A Pancakes node can run on ordinary server hardware or a small computer.
- The node hosts local users, service listings, credits, covenants, and exports.

Later:

- Nodes can discover each other.
- Neighborhood nodes can share selected listings.
- Guild or household nodes can federate selected covenant or credit state.
- A preconfigured appliance can make self-hosting easier for nontechnical groups.

## Pitchfork Integration

Pancakes credits can eventually connect to Pitchfork.

Possible integrations:

- A Pancakes service creates a Pitchfork event.
- A completed service grants materials or essences in the Pitchfork RPG client.
- Credits can unlock symbolic Pitchfork recipes, relics, or sanctuary improvements.
- Guild service activity can contribute to shared Pitchfork infrastructure.

Guardrail:

> Pitchfork should not turn real-world service work into uncapped game yield.

Pancakes credits and Pitchfork rewards should remain capped, transparent, and designed to avoid coercion.

## Anti-Gig-Economy Position

Pancakes should not become TaskRabbit with a friendlier skin.

Avoid:

- Race-to-the-bottom pricing.
- Public output leaderboards.
- Punitive ratings.
- Hidden platform fees.
- Algorithmic pressure to accept work.
- Turning household care into gig labor.
- Making low-income members serve wealthier members for status or survival.

Prefer:

- Mutual aid.
- Local trust.
- Cooperative governance.
- Transparent credits.
- Soft reputation.
- Dispute mediation.
- Ability to pause.
- Non-market recognition of care.

## Open Questions

- Are credits time-based, task-based, locally priced, or hybrid?
- Can credits expire?
- Can credits move between nodes?
- Can credits be redeemed for money, or should that remain separate?
- Who ratifies household covenants?
- How do users dispute unfair service ratings?
- What services require background checks, certification, or special safeguards?
- Can a household node hide all service activity from broader Pancakes Earth?
- How should urgent help requests avoid becoming exploitative?
- How does Pancakes protect people in unsafe domestic situations?

## Working Assumption

The first Pancakes service exchange should be local, simple, and non-speculative.

It should prove:

```text
offer service
-> complete service
-> receive credit or recognition
-> spend credit or contribute to household/guild state
```

Only after that loop is healthy should Pancakes add broader federation, maps, BLE discovery, hardware nodes, cross-app credits, or real-money settlement.
