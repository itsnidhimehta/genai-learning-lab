# LangGraph Human-in-the-Loop

A practical implementation of a Human-in-the-Loop workflow using LangGraph and Large Language Models.

## Overview

This project demonstrates how human approval or intervention can be incorporated into an AI workflow using LangGraph.

The workflow allows an AI agent to pause at a specific point and involve a human before continuing with the next step.

## Concepts Covered

- LangGraph
- Human-in-the-Loop workflows
- Graph-based AI workflows
- State management
- LLM integration
- Human approval and intervention
- LangChain
- Python

## Project Structure

```text
LangGraph-Human-In-The-Loop/
│
├── human_in_the_loop.ipynb
└── README.md
```

## Technologies Used

- Python
- LangChain
- LangGraph
- LLM
- Jupyter Notebook

## How It Works

The workflow follows a graph-based approach where different nodes represent different stages of the AI process.

A typical flow is:

```text
User Input
    ↓
AI Processing
    ↓
Human Review / Approval
    ↓
Continue Workflow
    ↓
Final Response
```

The human-in-the-loop mechanism provides an additional layer of control and allows a human to review or approve an AI-generated action before the workflow continues.

## Learning Outcome

This project helped me understand how LangGraph can be used to build controlled and stateful AI workflows where human intervention can be introduced when required.

## Author

**Nidhi Mehta**

GitHub: [itsnidhimehta](https://github.com/itsnidhimehta)