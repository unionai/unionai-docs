---
title: "Quick Start Tutorial"
weight: 3
---

# Quick Start Tutorial

This tutorial will guide you through creating and running your first Union AI workflow.

## Create a Simple Workflow

1. Create a new Python file `hello_workflow.py`:
```python
from unionai import Workflow

@Workflow
def hello_world():
    print("Hello from Union AI!")

if __name__ == "__main__":
    hello_world()
```

## Run the Workflow

1. Execute the workflow:
```bash
unionai run hello_workflow.py
```

2. Check the workflow status:
```bash
unionai status hello_world
```

## Add Task Dependencies

1. Modify the workflow to include multiple tasks:
```python
from unionai import Workflow, task

@task
def generate_data():
    return [1, 2, 3, 4, 5]

@task
def process_data(data):
    return sum(data)

@Workflow
def data_pipeline():
    data = generate_data()
    result = process_data(data)
    print(f"Result: {result}")
```

## Monitor and Debug

1. View workflow logs:
```bash
unionai logs data_pipeline
```

2. Access the dashboard:
```bash
unionai dashboard
```

## Next Steps

- Learn about [Advanced Features](../advanced-features)
- Explore [Best Practices](../best-practices)
- Set up [Production Deployment](../../deployment/production)