# Prompt Template Library

**VAULTX AI Internship — Week 02**
**Task 01 — Master the Core Prompt Patterns**

---

## Overview

This module provides a reusable collection of prompt templates for common Large Language Model (LLM) prompting techniques.

The library is implemented in:

```text
prompts/prompt_templates.py
```

The following prompting patterns are included:

- Zero-Shot Prompting
- Few-Shot Prompting
- Role/System Prompting
- Reasoning / Chain-of-Thought Prompting
- Constrained-Output Prompting

The templates are implemented as reusable Python functions so they can be imported and reused in later Week 02 tasks.

---

## Prompt Patterns

| Pattern | Description | Function |
|---|---|---|
| Zero-Shot | Performs a task without examples | `zero_shot_prompt()` |
| Few-Shot | Uses examples to demonstrate expected behavior | `few_shot_prompt()` |
| Role/System | Defines the model's role, goal, and constraints | `role_system_prompt()` |
| Reasoning | Encourages careful analysis before the final response | `chain_of_thought_prompt()` |
| Constrained Output | Restricts the response to a specified format | `constrained_output_prompt()` |

---

## 1. Zero-Shot Prompting

Zero-shot prompting provides the model with a task and input without providing examples.

**Function**

```text
zero_shot_prompt(task, text)
```

**Purpose**

Useful for straightforward tasks where the desired behavior is already clear from the instructions.

**Common Applications**

- Classification
- Summarization
- Question answering
- Text transformation

---

## 2. Few-Shot Prompting

Few-shot prompting provides example input/output pairs before processing a new input.

**Function**

```text
few_shot_prompt(task, examples, text)
```

**Purpose**

Examples help the model understand the expected behavior and response format.

**Common Applications**

- Classification
- Consistent formatting
- Domain-specific tasks
- Ambiguous tasks

---

## 3. Role/System Prompting

Role/System prompting establishes the model's role, objective, and constraints.

**Function**

```text
role_system_prompt(role, goal, constraints, text)
```

**Purpose**

Provides additional context and behavioral instructions for the model.

**Common Applications**

- Customer support
- Domain-specific assistants
- Professional AI applications
- Specialized workflows

---

## 4. Reasoning / Chain-of-Thought Prompting

Reasoning prompting instructs the model to carefully analyze the problem before producing its final answer.

**Function**

```text
chain_of_thought_prompt(task, text)
```

**Purpose**

Useful when a task requires consideration of multiple factors or careful analysis.

The implementation requests the final answer rather than requiring the model to expose its private reasoning process.

**Common Applications**

- Complex classification
- Decision-making
- Analytical tasks
- Ambiguous inputs

---

## 5. Constrained-Output Prompting

Constrained-output prompting specifies the expected response format and instructs the model not to include unnecessary content.

**Function**

```text
constrained_output_prompt(task, text, output_format)
```

**Purpose**

Helps produce predictable responses that can later be processed programmatically.

**Common Applications**

- Structured data generation
- JSON responses
- Information extraction
- Classification
- Automation pipelines

---

## Reusability

The templates are parameterized rather than hard-coded. This allows the same functions to be reused with different tasks and inputs.

For example:

```python
prompt = zero_shot_prompt(
    task="Classify the sentiment.",
    text="The product is excellent."
)
```

The generated prompt can then be passed to an LLM API.

---

## Implementation

The complete implementation is available in:

```text
prompts/prompt_templates.py
```

The module also contains example usage demonstrating each prompting pattern.

Run the module with:

```bash
python prompts/prompt_templates.py
```