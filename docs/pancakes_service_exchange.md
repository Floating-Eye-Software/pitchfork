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

## Tasks Are Not Services

Pancakes should distinguish personal or household tasks from Pancakes Earth services.

Tasks:

- Belong to a person, household, or node.
- Can be private.
- Include chores, routines, reminders, plans, and household responsibilities.
- May produce internal recognition, materials, or household state.
- Do not automatically become available to outsiders.

Services:

- Are offered to or requested from other people.
- Have a visibility scope.
- May involve credits, money, barter, or covenant rewards.
- Need trust, safety, scheduling, and dispute handling.
- May appear in Pancakes Earth or a local job board.

The same real-world action can be represented differently depending on context.

Example:

```text
Task: Vacuum our living room.
Service: Offer vacuuming help to three nearby households.
Pitchfork interpretation: Gather Order Salt and reduce household entropy.
```

This separation matters because service markets create social and economic risk that ordinary private task tracking should not inherit.

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

## Rate Neutrality

Pancakes should avoid centrally pricing ordinary work.

The platform can define rules, units, caps, and safety boundaries, but it should not declare a universal exchange rate for "doing the dishes" or "vacuuming a carpet."

Better:

- Local users propose rates.
- Households ratify internal rates.
- Guilds define their own norms.
- Service providers can accept, decline, or negotiate.
- Nodes can publish local guidance without forcing global prices.
- Pancakes can show historical local ranges where privacy allows.

Avoid:

- A universal chore price table.
- Platform-imposed wages for intimate household work.
- One global ranking of chores, care, study, rest, or skill.
- Hidden algorithmic pricing.

For consistency, Pancakes can still define conversion rules between local credits and Pitchfork symbolic rewards. Those rules should be transparent, capped, and node-aware.

## Baseline Credits and UBI

Earlier design explored a Universal Basic Income-like credit model.

Carry forward only as a cautious future direction:

- A node or sponsor may issue baseline Pancakes credits.
- Baseline credits should support participation, not create pressure.
- Additional credits may come from services, household covenants, or cooperative contributions.
- Credits should not become a substitute for wages, benefits, public support, or care obligations.

This overlaps with Pitchfork's symbolic basic income model. Any real-money version belongs behind the economic safeguards in [Pitchfork Economics](pitchfork_economics.md).

## Family Accounts and Child Companion Mode

The early design imagined Pancakes as a parent or household companion and Pitchfork as a child-friendly magical layer.

Possible model:

- A family or household has one subscription or node account.
- Children or household members have linked profiles.
- Household tasks can be assigned, witnessed, and ratified.
- Rewards can be split among linked profiles.
- Pitchfork presents appropriate rewards as tokens, materials, spells, or sanctuary progress.

Guardrails:

- Children should not be pushed into public service markets by default.
- Household chores should not become coercive surveillance.
- Parents or guardians should not be the only authority if a child's safety or data rights are at stake.
- Rewards should teach responsibility and care without turning family life into wage labor.

Subscription-linked mentor tokens were an early monetization idea. If used, they should be tied to the account or household, not multiplied by the number of children in a way that creates farming incentives.

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

## Domain-to-Essence Framework

The service exchange should eventually use the same domain mapping as Pitchfork.

Any domain can define:

- Activities.
- Categories.
- Colors or attunements.
- Materials.
- Essences.
- Credit rules.
- Privacy level.
- Verification model.

Example domains:

- Household: groceries, cleaning, cooking, school logistics, laundry.
- School: subjects, projects, attendance, study sessions.
- Health-adjacent tracking: movement, nutrition, rest, reflection.
- Service exchange: gardening, tutoring, transport, repair.

This lets new domains plug into the same accounting substrate without forcing every domain into the same UX.

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

## Physical Tokens and Exchange Nodes

Earlier design explored physical Pancakes or Pitchfork tokens: for example copper rounds, silver rounds, serial-numbered objects, or redeemable artifacts.

This is distant future.

Useful idea:

- Physical objects can make symbolic value tangible.
- A token can represent membership, achievement, credit, event participation, or a redeemable claim.
- Exchange should not depend on a single central issuer.

If physical tokens ever exist, Pancakes needs exchange-node rules:

- How tokens are authenticated.
- Who can issue them.
- Who can redeem them.
- How serial numbers or keys are managed.
- How fraud is handled.
- Whether physical tokens represent money, symbolic credit, collectible value, or node-local privileges.
- How to avoid making the project operator a choke point for the whole economy.

This should not precede a healthy internal credit system.

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
