# Understanding Pitchfork Contracts

## Status

Explanatory Companion

Draft

Companion to:

* Pitchfork Contracts
* Pitchfork System Overview
* Service Exchange
* Mentor Ecosystem

---

# Why Does Pitchfork Need Contracts?

At first glance, contracts sound like legal documents.

Most people imagine:

* lawyers,
* signatures,
* lawsuits,
* and fine print.

That is not what Pitchfork contracts are.

A Pitchfork contract is simply a way of coordinating activity.

A contract answers questions like:

* Who is involved?
* What are we trying to do?
* What is expected?
* What limits apply?
* What happens when something occurs?
* How are disagreements handled?

Almost every form of organized human activity contains contracts, even when nobody calls them that.

Examples:

A family agreement:

> Whoever cooks does not wash dishes.

A volunteer agreement:

> We meet every Saturday to maintain the garden.

A service exchange:

> I tutor you and you help me with repairs.

A participation reward:

> Show up and participate up to three times per day.

These are all contracts.

---

# Why Not Just Use Events?

Pitchfork already has events.

Examples:

```text id="vny51t"
walk happened
meal happened
lesson happened
repair happened
```

Events tell us:

> What happened.

Contracts tell us:

> What should happen because of what happened.

Examples:

```text id="n3u4b0"
walk happened
→ grant participation token
```

```text id="m0b0z4"
repair happened
→ transfer service credits
```

```text id="7on8fw"
meeting happened
→ mark obligation complete
```

Contracts connect events to meaning.

---

# Why Are Contracts So Complicated?

Because the future is uncertain.

Most contracts are attempts to answer:

> What should happen if reality does not go exactly as planned?

People get sick.

Requirements change.

Someone misunderstands instructions.

The weather changes.

A computer fails.

A project takes longer than expected.

Nobody necessarily did anything wrong.

Reality simply became messy.

Contracts exist because humans need ways to coordinate under uncertainty.

---

# Contracts Are Not About Distrust

It is easy to think:

```text id="c9ht1v"
contract
=
I do not trust you
```

Usually the truth is closer to:

```text id="tf6lud"
contract
=
we both know the future is uncertain
```

Good people acting in good faith still encounter:

* illness,
* accidents,
* ambiguity,
* changing priorities,
* incomplete information,
* and unexpected events.

Contracts provide shared expectations for handling those situations.

---

# The Building Blocks

Pitchfork contracts are constructed from reusable pieces.

Think of them as building blocks.

---

# Parties

Parties answer:

> Who is involved?

Examples:

```text id="s4v1yj"
Alice
Bob
Household
Guild
Node
```

Examples:

```text id="9rmw9i"
Tutor
Student
```

```text id="gmnnwm"
Volunteer
Community Garden
```

---

# Terms

Terms answer:

> What are we trying to accomplish?

Examples:

> Keep the kitchen reasonably clean.

> Maintain a welcoming community.

> Support newcomers.

Terms provide meaning.

They are usually written in ordinary language.

---

# Obligations

Obligations answer:

> What is expected?

Examples:

```text id="o1kz22"
walk
study
repair equipment
teach lesson
review proposal
```

An obligation may be:

* required,
* optional,
* repeatable,
* recurring.

---

# Conditions

Conditions answer:

> When does this apply?

Examples:

```text id="q1e76e"
if inventory is low
if both people confirm
if it is during school term
if participation cap not reached
```

Conditions allow contracts to adapt to circumstances.

---

# Quotas

Quotas answer:

> How much is allowed?

Examples:

```text id="e6gt2k"
3 rewards per day
5 tutoring sessions per month
100 messages per hour
```

Quotas are limits.

They are only one part of a contract.

A quota is not the contract itself.

---

# Procedures

Procedures answer:

> How do we make decisions?

Examples:

```text id="mwut1l"
majority vote
consensus
ranked choice
approval voting
```

Procedures become important whenever groups need to decide something together.

---

# Settlement

Settlement answers:

> What happens now?

Examples:

```text id="7e6ul0"
grant token
transfer credits
unlock item
record completion
change reputation
```

Settlement is usually the accounting consequence of events.

---

# Enforcement

Enforcement answers:

> What happens if expectations are not met?

Many contracts should simply say:

```text id="jwsn1q"
nothing bad happens
```

For example:

```text id="c4mwn4"
participation missed
→ no reward
```

No punishment.

Other contracts may include:

* reminders,
* reviews,
* arbitration,
* suspension.

---

# Disputes

Disputes answer:

> What if people disagree?

Examples:

```text id="7vct2s"
Did tutoring happen?
Did the vote count correctly?
Was the repair acceptable?
```

Most disputes are not about bad intentions.

They are about:

* ambiguity,
* misunderstandings,
* changing circumstances,
* incomplete information.

---

# Why Procedures Matter

Consider this vote:

```text id="yy00ij"
Proposal A wins.
```

Someone may say:

> I do not like the outcome.

That is disappointment.

Another person may say:

> Half the votes were not counted.

That is a procedural concern.

Contracts generally care more about procedural legitimacy than emotional satisfaction.

---

# Standing Service Contracts

One of the most important ideas in Pitchfork is that entire domains of life can be represented as long-lived contracts.

Examples:

* vitality,
* relationships,
* governance,
* justice,
* maintenance,
* ecology.

These are called service contracts.

A service contract is essentially:

```text id="w6pxhr"
purpose
+
indicators
+
risks
+
interventions
+
review
```

This structure closely resembles a safety case.

---

# Example: Governance Service

Purpose:

> Maintain fair and trustworthy decision-making.

Indicators:

* unresolved disputes,
* participation rates,
* appeal backlog.

Risks:

* procedural confusion,
* governance capture,
* loss of legitimacy.

Interventions:

* reviews,
* amendments,
* votes,
* arbitration.

---

# Example: Maintenance Service

Purpose:

> Preserve continuity and prevent neglect.

Indicators:

* overdue repairs,
* neglected inventories,
* recurring failures.

Risks:

* breakdown,
* fragility,
* accumulated technical debt.

Interventions:

* reminders,
* repair projects,
* stewardship initiatives.

---

# Where Mentors Fit

The contracts govern.

The mentors explain.

The service contract might determine:

```text id="39j2bo"
care burden increasing
```

The mentor might say:

> Several people have been carrying most of the care work lately. It may be time to check in with one another.

The mentor is not making decisions.

The mentor is helping people understand the system.

---

# A Different Way To Think About Contracts

Most software asks:

```text id="1gjpfd"
What happened?
```

Pitchfork asks:

```text id="r1n63h"
What happened?
What did we expect?
What does it mean?
What should happen now?
```

Contracts are the layer that answers those questions.

---

# The Big Idea

A Pitchfork contract is not a legal document.

It is a reusable coordination pattern.

Contracts allow people, households, communities, and software systems to answer:

```text id="x1snyw"
Who is involved?
What are we trying to do?
What is expected?
What limits apply?
What happens when circumstances change?
How are disagreements handled?
What should happen next?
```

The goal is not bureaucracy.

The goal is humane coordination under uncertainty.
