# KEDA ScaledJobs

## What is it
- KEDA add-on that runs **one Kubernetes Job per event** instead of scaling pods in a Deployment.
- for each event detected on a trigger, a single Job is scheduled that pulls the event, processes to completion and terminates.
- suits **long-running, per-event, isolated batch workloads**.

## ScaledJob vs ScaledObject

> ScaledObject
- scales **pods in a Deployment**
- one pod can process **multiple events** during its lifetime

> ScaledJob
- creates **one Job per event**
- each Job processes a single event and exits
- pick this when work is long running, needs isolation per event, or naturally completes after one event

## Spec Fields

> jobTargetRef
- wraps a standard `batch/v1` JobSpec (`parallelism`, `completions`, `activeDeadlineSeconds`, `backoffLimit`, `template`)
- `template` is **mandatory**

> pollingInterval
- how often triggers are evaluated in seconds
- default: `30`

> minReplicaCount
- minimum concurrent jobs kept alive
- default: `0`
- keep it > 0 to avoid cold start / bootstrap delay

> maxReplicaCount
- max jobs created per polling cycle
- default: `100`
- caps scaling to prevent resource exhaustion

> successfulJobsHistoryLimit / failedJobsHistoryLimit
- retention count for completed / failed jobs
- both default: `100`
- similar to Kubernetes CronJob history limits

> envSourceContainerName
- container KEDA reads env vars from when passing trigger metadata
- default: first container in `jobTargetRef.template.spec.containers`

> rollout
- controls update behaviour when the spec changes
- `default` - terminates existing jobs before recreation
- `gradual` - keeps existing jobs, new ones use the updated spec
- `propagationPolicy` controls cleanup ordering
- **Note**: top-level `rolloutStrategy` is deprecated - use `rollout.strategy` instead

> scalingStrategy
- determines how job counts are calculated per polling cycle
- options: `default`, `custom`, `accurate`, `eager`
- `multipleScalersCalculation` combines metrics when multiple triggers are defined

> triggers
- list of event sources driving the scaling
- supports Kafka, RabbitMQ, AWS SQS, Azure Service Bus, Prometheus, and many more

## Pausing autoscaling
- add annotation on the ScaledJob to freeze scaling **without deleting** the resource

``` yaml
metadata:
  annotations:
    autoscaling.keda.sh/paused: "true"
```

## Sample ScaledJob ( RabbitMQ trigger )

``` yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledJob
metadata:
  name: rabbitmq-consumer
  namespace: default
spec:
  jobTargetRef:
    parallelism: 1
    completions: 1
    backoffLimit: 4
    template:
      spec:
        containers:
        - name: consumer
          image: myorg/rabbitmq-consumer:latest
          envFrom:
          - secretRef:
              name: rabbitmq-secrets
        restartPolicy: Never
  pollingInterval: 10          # check queue every 10s
  maxReplicaCount: 30          # cap concurrent jobs
  successfulJobsHistoryLimit: 5
  failedJobsHistoryLimit: 5
  scalingStrategy:
    strategy: "default"
  triggers:
  - type: rabbitmq
    metadata:
      queueName: myqueue
      queueLength: "5"         # create a job for every 5 pending messages
      host: RabbitMqHost       # env var name in the container
```

- when a message arrives on the queue KEDA creates a Job
- as more messages arrive additional Jobs are created up to `maxReplicaCount`
- completed and failed jobs are cleaned up per the history limits

## References
- [KEDA scaling jobs concept](https://keda.sh/docs/2.20/concepts/scaling-jobs/)
- [ScaledJob spec reference](https://keda.sh/docs/2.20/reference/scaledjob-spec/)
