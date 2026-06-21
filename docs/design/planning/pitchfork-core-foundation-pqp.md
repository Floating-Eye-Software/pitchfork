# Pitchfork Core Foundation — Project Quality Plan

## Status

Draft

## Controlled Item

Pitchfork Core Foundation

## Purpose

This Project Quality Plan defines how the Pitchfork Core Foundation project applies the FLEY QMS.

The project establishes Pitchfork as an installable Python accounting library used by Pancakes nodes and clients.

## QMS Activity Configuration

| QMS Activity       | Selected Method                    | Tool / Platform          | Notes                                                   |
| ------------------ | ---------------------------------- | ------------------------ | ------------------------------------------------------- |
| Change Control     | GitHub Pull Request workflow       | GitHub                   | All controlled changes reviewed before merge.           |
| Document Control   | Markdown under version control     | GitHub                   | Design artifacts stored under `pitchfork/docs/design/`. |
| Quality Planning   | Project Quality Plan               | Repository docs          | This document.                                          |
| Project Management | GitHub issues / project board      | GitHub                   | Work tracked by issues and milestones.                  |
| Risk Management    | FLEY risk register                 | Markdown / GitHub issues | Project risks tracked in `risks/`.                      |
| Design Control     | FLEY Design Control Plan           | Repository docs          | See DCP.                                                |
| Verification       | Automated tests and review records | pytest / CI              | Unit, contract, and package tests.                      |
| Validation         | Scenario-based validation          | Local test environment   | Confirms intended use as Pancakes accounting library.   |

## Quality Objectives

* Establish a deterministic accounting engine.
* Preserve clear Pitchfork/Pancakes ownership boundaries.
* Prevent database or framework coupling in the core library.
* Provide testable, documented public interfaces.
* Support traceability from requirements to verification evidence.

## Documentation Location

All design-control artifacts are stored under:

```text
pitchfork/docs/design/
```

## Version Control

All artifacts are controlled through Git.

## Review Cadence

Reviews occur at:

* design control kickoff,
* requirements approval,
* architecture approval,
* verification completion,
* release readiness.

## Risk Management

Risks are tracked in:

```text
pitchfork/docs/design/risks/
```

Risk review occurs at each major design review.

## Design Control Reference

The project Design Control Plan is:

```text
pitchfork/docs/design/planning/pitchfork-core-foundation-dcp.md
```

## Release Criteria

The project may release when:

* requirements are approved,
* architecture is reviewed,
* implementation satisfies requirements,
* verification evidence passes,
* traceability is complete,
* release review is recorded.
