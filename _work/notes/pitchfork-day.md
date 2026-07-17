Yes — that is a better abstraction.

You are not looking for a todo API. You are looking for a **Pitchfork Day primitive**.

## Core idea

Pitchfork should define a native concept like:

```text
PitchforkDay
```

or better:

```text
AccountingDay
```

because the day is not just calendar UI. It is a **settlement boundary**.

It is the unit that answers:

```text
What counts as today?
What has already been counted?
What caps apply?
What resets?
What rolls forward?
What remains private?
What projects into clients?
```

That matters for Redwitch, Wellness Notebook, RPG gathering, symbolic UBI, streak avoidance, daily closure, and caps.

## The primitive should not be “midnight to midnight”

It should support several day definitions:

```text
civil_day
wake_day
ritual_day
cycle_day
node_day
```

Examples:

```text
civil_day:
2026-06-08 in America/Toronto

wake_day:
from user wake anchor to next wake anchor

ritual_day:
from 4:00 AM to 3:59 AM

cycle_day:
Redwitch day 17 of current cycle

node_day:
the settlement day used by a household/guild/node
```

This is the missing layer.

## Proposed Pitchfork object

```text
AccountingDay
- id
- node_id
- actor_id
- local_date
- timezone
- day_type
- starts_at
- ends_at
- settlement_status
- cap_policy_id
- privacy_scope
- created_at
- closed_at
```

Then events attach to it:

```text
PitchforkEvent
- id
- accounting_day_id
- event_type
- occurred_at
- source_client
- data_class
- permission_scope
- measures
- settlement_result
```

## Why this belongs in Pitchfork

Because caps are accounting logic, not app logic.

Pitchfork Economics already says participation rewards should be capped and daily/weekly bounded, because uncapped reward systems create optimization pressure and extraction risk.

Wellness Notebook also depends on finite daily closure: the daily session should feel achievable, bounded, and emotionally complete.

Pitchfork Client API already has events, caps, settlement, permission scope, data class, and idempotency; the “day” should be the missing settlement context around those events.

## Reference implementation target

A good first implementation would be:

```text
pitchfork.day
```

with:

```python
resolve_accounting_day(actor, occurred_at, policy)
record_event_for_day(event_request)
get_day_summary(actor, date)
close_day(actor, date)
apply_daily_caps(day)
```

The reference app does not need to be a todo app.

It could be a tiny test client called:

```text
Pitchfork Daybook
```

Its only job:

```text
log one movement event
log one rest event
log one reflection-completed event
show daily caps
close the day
emit private symbolic resources
```

That would become the reference implementation for:

```text
“how Pancakes apps use a day”
```

not:

```text
“how Pancakes apps manage tasks”
```

## My revised assessment

Condution is mostly irrelevant here.

The relevant reference is not GTD. It is:

```text
daily accounting boundary
+ capped settlement
+ local timezone
+ client-private records
+ permissioned events
+ daily closure
```

That should be first-class Pitchfork infrastructure.
