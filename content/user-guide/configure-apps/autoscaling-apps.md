---
title: Autoscaling apps
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Autoscaling apps

Flyte apps support autoscaling, allowing them to scale up and down based on traffic. This helps optimize costs by scaling down when there's no traffic and scaling up when needed.

## Scaling configuration

The `scaling` parameter uses a `Scaling` object to configure autoscaling behavior:

```python
scaling=flyte.app.Scaling(
    replicas=(min_replicas, max_replicas),
    scaledown_after=idle_ttl_seconds,
)
```

### Parameters

- **`replicas`**: A tuple `(min_replicas, max_replicas)` specifying the minimum and maximum number of replicas
- **`scaledown_after`**: Time in seconds to wait before scaling down when idle (idle TTL)

## Basic example

Here's a simple example with scaling from 0 to 1 replica:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=basic-scaling lang=python >}}

This configuration:
- Starts with 0 replicas (no running instances)
- Scales up to 1 replica when there's traffic
- Scales back down to 0 after 5 minutes (300 seconds) of no traffic

## Scaling patterns

### Always-on app

For apps that need to always be running:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=always-on lang=python >}}

### Scale-to-zero app

For apps that can scale to zero when idle:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=scale-to-zero lang=python >}}

### High-availability app

For apps that need multiple replicas for availability:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=high-availability lang=python >}}

### Burstable app

For apps with variable load:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=burstable lang=python >}}

## Idle TTL (Time To Live)

The `scaledown_after` parameter (idle TTL) determines how long an app instance can be idle before it's scaled down. 

### Considerations

- **Too short**: May cause frequent scale up/down cycles, leading to cold starts
- **Too long**: Keeps resources running unnecessarily, increasing costs
- **Optimal**: Balance between cost and user experience

### Common idle TTL values

- **Development/Testing**: 60-180 seconds (1-3 minutes) - quick scale down for cost savings
- **Production APIs**: 300-600 seconds (5-10 minutes) - balance cost and responsiveness
- **Batch processing**: 900-1800 seconds (15-30 minutes) - longer to handle bursts
- **Always-on**: Set `min_replicas > 0` - never scale down

## Example: vLLM app with autoscaling

Here's an example using autoscaling with a vLLM model serving app:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-vllm-example.py" lang=python >}}

This is ideal for model serving because:
- Model loading is expensive, so scaling to zero saves resources
- 10 minutes idle time prevents frequent cold starts
- Scales up automatically when requests come in

## Monitoring scaling behavior

You can monitor your app's scaling behavior:

1. **Flyte Console**: View app status, replica counts, and scaling events
2. **Logs**: Check app logs to see scaling events
3. **Metrics**: Monitor request rates and response times to tune scaling

## Best practices

1. **Start conservative**: Begin with longer idle TTL values and adjust based on usage
2. **Monitor cold starts**: Track how long it takes for your app to become ready after scaling up
3. **Consider costs**: Balance idle TTL between cost savings and user experience
4. **Use appropriate min replicas**: Set `min_replicas > 0` for critical apps that need to be always available
5. **Test scaling behavior**: Verify your app handles scale up/down correctly (e.g., state management, connections)

## Limitations

- Scaling is based on traffic/request patterns, not CPU/memory utilization
- Cold starts may occur when scaling from zero
- Stateful apps need careful design to handle scaling (use external state stores)
- Maximum replicas are limited by your cluster capacity

## Troubleshooting

**App scales down too quickly:**
- Increase `scaledown_after` value
- Set `min_replicas > 0` if app needs to stay warm

**App doesn't scale up fast enough:**
- Ensure your cluster has capacity
- Check if there are resource constraints

**Cold starts are too slow:**
- Pre-warm with `min_replicas = 1`
- Optimize app startup time
- Consider using faster storage for model loading

