# Information Sources

## Status

Proposed Architecture Extension

Draft

---

# Purpose

This document introduces **Information Sources** as a first-class architectural object within the Pancakes and Pitchfork ecosystem.

The existing architecture recognizes:

* Nodes
* Clients
* Actors
* Events

These concepts describe how people, software, governance systems, and accounting systems participate in the network.

However, many meaningful observations originate from entities that are neither actors nor clients.

Examples include:

* weather stations
* lake buoys
* thermometers
* smart watches
* GPS devices
* astronomical calculations
* environmental monitoring systems
* institutional data feeds
* ecological forecasting systems
* future AI classification systems

The ecosystem requires a first-class representation for non-human producers of observations.

Information Sources provide that representation.

---

# Core Principle

```text
Actors act.

Sources produce observations.

Clients interpret.

Nodes govern.

Pitchfork accounts.
```

---

# Motivation

The current architecture implicitly assumes that meaningful events originate from actors.

For example:

```text
Actor
↓
Client
↓
Event
↓
Pitchfork
↓
Projection
↓
Client
```

This model works well for:

* journals
* rituals
* reflections
* service exchange
* cooperative participation

It does not adequately describe:

* weather conditions
* astronomical conditions
* environmental measurements
* ecological indicators
* sensor readings
* public datasets
* derived forecasts

A weather station is not an actor.

A weather station is not a client.

A weather station is not a node.

Yet it may produce observations that influence projections and world state.

Information Sources extend the architecture to support these cases.

---

# Information Source Definition

An Information Source is an entity that produces observations that may be consumed by nodes.

Information Sources do not govern.

Information Sources do not authorize.

Information Sources do not settle accounts.

Information Sources produce observations.

---

# Existing Network Topology

```text
Actor
↓
Client
↓
Node
↓
Pitchfork
↓
Projection
↓
Client
```

---

# Revised Network Topology

```text
Actors
↓
Clients
↓
Nodes
↓
Pitchfork
↓
Projections
↓
Clients

Sources
↓
Nodes
↓
Pitchfork
↓
Projections
↓
Clients
```

Sources become an additional input path into the ecosystem.

---

# Architectural Objects

## Nodes

Responsibilities:

* governance
* stewardship
* storage
* permissions
* identity enforcement
* retention
* federation

Nodes determine which sources they trust.

Nodes remain the trust boundary.

---

## Clients

Responsibilities:

* interaction
* interpretation
* visualization
* projection
* user experience

Clients consume derived state.

Clients do not determine source trust.

---

## Actors

Responsibilities:

* authorization
* participation
* covenant creation
* event initiation
* ownership of records

Actors intentionally perform actions.

---

## Information Sources

Responsibilities:

* observation
* measurement
* reporting
* publication
* computation
* signaling

Sources produce observations.

---

# Observation Architecture

Not every observation should become a Pitchfork event.

The architecture distinguishes between:

```text
Source
↓
Observation
↓
Node Processing
↓
Source Event
↓
Pitchfork
```

This distinction prevents Pitchfork from becoming a telemetry warehouse.

Raw observations and meaningful events remain separate concepts.

---

# Observation Production Modes

Observations may be produced in different ways.

The architecture recognizes four production modes.

---

## Measured

Measured observations originate from direct interaction with the world.

Pipeline:

```text
World
↓
Measurement
↓
Observation
```

Examples:

* temperature
* humidity
* GPS position
* water level
* air quality

---

## Computed

Computed observations originate from models and calculations.

Pipeline:

```text
Inputs
↓
Model
↓
Observation
```

Examples:

* sunrise
* sunset
* moon phase
* solar altitude
* frost risk

---

## Human

Human observations originate from human interpretation or reporting.

Pipeline:

```text
Person
↓
Interpretation
↓
Observation
```

Examples:

* bird sightings
* field notes
* journal observations
* ecological surveys

---

## Hybrid

Hybrid observations combine multiple production modes.

Pipeline:

```text
Measurements
+
Human Reports
+
Models
↓
Observation
```

Examples:

* weather forecasts
* migration forecasts
* AI classifications
* ecological indicators

---

# Source Identity

A source represents a stable producer of observations.

Minimum fields:

```text
Source
- source_id
- source_type
- production_mode
- display_name
- steward
- trust_level
- provenance
- update_frequency
- created_at
```

---

# Observation

An observation is a report about the world produced by a source.

Examples:

```text
temperature = 17°C
```

```text
moon_phase = waxing_gibbous
```

```text
sunrise = 05:37
```

```text
migration_pressure = moderate
```

Minimum fields:

```text
Observation
- observation_id
- source_id
- observed_at
- observation_type
- payload
- provenance
```

Observations may remain entirely outside Pitchfork settlement.

---

# Source Events

A Source Event is a node-approved event derived from one or more observations.

Examples:

```text
fog_detected
```

```text
migration_window_open
```

```text
winter_habitat_active
```

```text
full_moon_arrived
```

Minimum fields:

```text
SourceEvent
- event_id
- source_id
- event_type
- occurred_at
- confidence
- provenance
```

Source Events may participate in settlement and projection systems.

---

# Source Categories

## Human Sources

Examples:

* journals
* field observations
* ecological surveys
* citizen science reports

---

## Device Sources

Examples:

* thermometers
* smart watches
* GPS devices
* weather stations
* environmental sensors

---

## Environmental Sources

Examples:

* lake buoys
* river gauges
* watershed monitors
* air quality stations

---

## Astronomical Sources

Examples:

* sunrise engines
* sunset engines
* moon phase calculators
* celestial position calculators

---

## Institutional Sources

Examples:

* Environment Canada
* municipal data feeds
* conservation authorities
* public weather services

---

## Derived Sources

Examples:

* migration forecasting systems
* ecological models
* AI classification systems
* habitat models

---

# Deterministic, Probabilistic, and Subjective Observations

Observations differ in certainty.

This distinction is independent of source category.

---

## Deterministic

Given the same inputs, the observation is expected to be identical.

Examples:

* sunrise
* sunset
* moon phase
* solar position

---

## Probabilistic

The observation represents an estimate.

Examples:

* weather forecast
* migration forecast
* flood forecast
* habitat suitability

---

## Subjective

The observation depends upon human interpretation.

Examples:

* bird identification
* field notes
* ecological assessments
* manual classifications

---

# Provenance

Every observation should retain provenance information.

Nodes should be able to determine:

```text
Where did this observation originate?
```

and:

```text
How was it produced?
```

Possible provenance fields:

```text
source_id
production_mode
model_name
model_version
input_sources
generated_at
```

Provenance becomes increasingly important for hybrid and computed observations.

---

# Confidence

Confidence is independent of source category.

Examples:

```text
sunrise
→ confidence = 1.0
```

```text
weather forecast
→ confidence = 0.78
```

```text
migration forecast
→ confidence = 0.62
```

Confidence should remain part of observation and event metadata.

---

# Trust and Validation

Not all sources are equally trustworthy.

Nodes evaluate:

* provenance
* confidence
* update reliability
* historical accuracy
* stewardship
* replacement strategy

Trust remains node-governed.

Different nodes may assign different trust levels to the same source.

---

# Relationship To Nodes

Nodes determine:

* which sources are accepted
* how observations are processed
* whether observations become events
* retention policies
* projection permissions

Sources never govern themselves.

Nodes remain the authority boundary.

---

# Relationship To Pitchfork

Pitchfork may consume Source Events.

Pitchfork does not need to consume every observation.

Many observations may remain:

```text
Source
↓
Observation
↓
Projection
```

without entering settlement systems.

Pitchfork should primarily consume observations that contribute to:

* accounting
* covenants
* inventories
* projections
* world state

---

# Projection Examples

## Weather

```text
Rainfall Observation
↓
Rain Detected Event
↓
Ambient Rain Projection
```

---

## Astronomy

```text
Moon Phase Observation
↓
Full Moon Event
↓
Environmental Projection
```

---

## Ecology

```text
Day Length
↓
Migration Model
↓
Migration Pressure Observation
↓
Migration Window Event
↓
Wildlife Projection
```

---

# Privacy Implications

Many sources are public.

Examples:

* weather stations
* astronomical engines
* public datasets

Other sources may be private.

Examples:

* household sensors
* personal thermometers
* wearable devices
* home environmental monitors

Nodes should classify observations using existing privacy policies.

Possible classifications:

```text
public
node_shared
personal
sensitive
regulated_high_risk
```

Not all observations should be shareable.

---

# Federation Considerations

Future federation may support:

* source discovery
* source catalogs
* source verification
* source mirroring
* source reputation

Federation should not imply universal trust.

Nodes remain free to:

* accept sources
* reject sources
* replace sources
* override trust ratings

---

# Future Directions

Potential future capabilities include:

* source marketplaces
* ecological monitoring networks
* citizen science integration
* astronomical engines
* migration forecasting systems
* hydrological models
* environmental digital twins
* AI-assisted observation systems
* source attestation systems

These are future extensions of the same architectural pattern.

---

# Design Principles

## Observation Is Not Authorization

Sources produce observations.

Actors authorize actions.

These responsibilities must remain separate.

---

## Observations Are Not Events

Raw observations should not automatically become Pitchfork events.

Nodes determine what becomes meaningful.

---

## Sources May Be Public Or Private

The architecture must support both public environmental systems and highly private personal devices.

---

## Observations Carry Provenance

Every observation should retain information describing how it was produced.

Trust depends on provenance.

---

## Clients Remain Source-Agnostic

Clients consume projections and derived state.

They should not need to understand individual source implementations.

---

## Meaning Emerges Later

Observations describe conditions.

Events represent significance.

Projections represent interpretation.

These layers should remain distinct.

---

# Final Principle

```text
Sources produce observations.

Observations carry provenance.

Nodes determine trust.

Pitchfork accounts.

Projections determine meaning.
```
