# Saga Pattern — Short Notes

## The problem

In a monolith, a multi-step operation is wrapped in one database transaction — atomic commit or full rollback, for free. In microservices, each service owns its own database, so there is no shared transaction. [Two-phase commit](https://en.wikipedia.org/wiki/Two-phase_commit_protocol) exists but is avoided: it forces blocking locks across services and hurts availability.

## The pattern

A **saga** replaces one atomic transaction with a **sequence of local transactions**. Each service commits its own step. If a later step fails, previously-committed steps are undone by **compensating transactions** — explicit business-level "undo" logic. See [Chris Richardson's canonical write-up](https://microservices.io/patterns/data/saga.html) for the full treatment.

Two properties to internalize:

- **Compensation is semantic, not physical.** You don't un-charge a card; you *refund*. You write this logic yourself.
- **Sagas give up isolation.** Other transactions can see intermediate state (a charged card before the order is confirmed). Design around it.

## Two flavors

The pattern splits on one question: **who decides what step happens next?**

### Orchestration

A central **orchestrator** holds the workflow. It sends commands ("charge card"), waits for replies, and decides the next step. On failure, it explicitly invokes compensations in reverse order.

- Saga logic lives in **one readable place** (a state machine)
- Failure detection is **built in** — the orchestrator times out on missing replies
- Cost: the orchestrator is a component that must be highly available
- Real tools that do this for you: [Temporal](https://temporal.io), [AWS Step Functions](https://aws.amazon.com/step-functions/), [Camunda](https://camunda.com)

### Choreography

No coordinator. Each service listens for events it cares about, does its local work, and emits a new event. The saga's flow is **emergent** — it exists only as the collective behavior of the services.

- Loosely coupled, simple locally
- **No component watches the flow.** Failures show up via reconciliation jobs, customer complaints, or event-timeout monitoring
- **Cycle risk**: A emits → B reacts → emits → A reacts → … Nobody wrote the loop; each subscription looked reasonable in isolation
- Global behavior is understood by no one because there's no artifact representing it

## Tradeoff summary

| | Orchestration | Choreography |
|---|---|---|
| Flow lives in | One place | Spread across services |
| Failure detection | Built in (timeouts) | External (reconciliation/monitoring) |
| Coupling | To the orchestrator | To event contracts |
| Adding a step | Edit orchestrator | Add a service subscribing to the right event |
| Cycle risk | Low | High |
| Single point of failure | Orchestrator (must be HA) | None inherently |

**Rule of thumb:** orchestration for complex, long-lived business workflows (order fulfillment, loan approval). Choreography for simple, event-driven reactions with 2–3 loosely-related steps (signup → welcome email + provision workspace).

## Compensation ≠ rollback

A DB rollback pretends the writes never happened. A saga compensation says *they happened, and here's what we did about it* — net effect restored, history preserved.

Consequences:

- **Compensations can themselves fail.** Need retries, dead-letter queues, and eventually a human. Orchestrators usually model a "compensation failed" terminal state that pages someone.
- **Some steps have no compensation.** A sent email, a shipped package, a placed trade. Design the workflow so the irreversible step is **last** — the [pivot transaction](https://microservices.io/patterns/data/saga.html) — after everything that could still fail has succeeded.
- **Customers see the seams.** Good UX around sagas makes the sequence (charge → apology → refund) feel intentional, not buggy.

## Related plumbing

Both saga topologies need the [outbox pattern](https://microservices.io/patterns/data/transactional-outbox.html) to reliably publish events alongside a local DB commit, and every step (and every compensation) must be **idempotent** because message brokers deliver at-least-once.
