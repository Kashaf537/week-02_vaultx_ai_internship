"""
Reusable Prompt Template Library

This module contains reusable templates for common LLM prompting
patterns:

1. Zero-shot prompting
2. Few-shot prompting
3. Role/System prompting
4. Chain-of-thought prompting
5. Constrained-output prompting

The templates are designed to be imported and reused by later
Week 02 tasks.
"""


# ============================================================
# 1. ZERO-SHOT PROMPT
# ============================================================

def zero_shot_prompt(task: str, text: str) -> str:
    """
    Create a zero-shot prompt.

    Zero-shot prompting asks the model to perform a task
    without providing examples.
    """

    return f"""
Task:
{task}

Input:
{text}

Provide the best possible answer based on the task.
""".strip()


# ============================================================
# 2. FEW-SHOT PROMPT
# ============================================================

def few_shot_prompt(
    task: str,
    examples: list[dict[str, str]],
    text: str
) -> str:
    """
    Create a few-shot prompt.

    Few-shot prompting provides examples of inputs and
    expected outputs before asking the model to process
    a new input.
    """

    example_text = []

    for index, example in enumerate(examples, start=1):
        example_text.append(
            f"""Example {index}:
Input:
{example["input"]}

Expected Output:
{example["output"]}
"""
        )

    examples_block = "\n".join(example_text)

    return f"""
Task:
{task}

Here are examples showing the expected behavior:

{examples_block}

Now process the following input:

Input:
{text}

Return the answer following the pattern demonstrated in the examples.
""".strip()


# ============================================================
# 3. ROLE / SYSTEM PROMPT
# ============================================================

def role_system_prompt(
    role: str,
    goal: str,
    constraints: list[str],
    text: str
) -> str:
    """
    Create a role/system-style prompt.

    The prompt defines the model's role, goal, and constraints
    before providing the user's input.
    """

    constraints_text = "\n".join(
        f"- {constraint}" for constraint in constraints
    )

    return f"""
Role:
You are {role}.

Goal:
{goal}

Constraints:
{constraints_text}

Input:
{text}

Complete the task according to your assigned role and constraints.
""".strip()


# ============================================================
# 4. CHAIN-OF-THOUGHT PROMPT
# ============================================================

def chain_of_thought_prompt(task: str, text: str) -> str:
    """
    Create a reasoning-oriented prompt.

    The model is asked to reason through the task internally
    and provide the final answer clearly.
    """

    return f"""
Task:
{task}

Input:
{text}

Analyze the problem carefully and reason through the relevant
steps before producing the final answer.

Provide only the final answer unless reasoning is specifically
required.
""".strip()


# ============================================================
# 5. CONSTRAINED OUTPUT PROMPT
# ============================================================

def constrained_output_prompt(
    task: str,
    text: str,
    output_format: str
) -> str:
    """
    Create a constrained-output prompt.

    The model is explicitly instructed to follow a specified
    output format.
    """

    return f"""
Task:
{task}

Input:
{text}

Return the response using exactly the following format:

{output_format}

Do not add extra sections, explanations, or text outside
the required format.
""".strip()


# ============================================================
# EXAMPLE USAGE
# ============================================================

if __name__ == "__main__":

    sample_text = (
        "The customer received the wrong product and wants a refund."
    )

    print("\n" + "=" * 60)
    print("ZERO-SHOT")
    print("=" * 60)

    print(
        zero_shot_prompt(
            task="Classify the sentiment of the text.",
            text=sample_text
        )
    )

    print("\n" + "=" * 60)
    print("FEW-SHOT")
    print("=" * 60)

    examples = [
        {
            "input": "The product arrived damaged.",
            "output": "Negative"
        },
        {
            "input": "The product works perfectly.",
            "output": "Positive"
        }
    ]

    print(
        few_shot_prompt(
            task="Classify the sentiment of the text.",
            examples=examples,
            text=sample_text
        )
    )

    print("\n" + "=" * 60)
    print("ROLE / SYSTEM")
    print("=" * 60)

    print(
        role_system_prompt(
            role="a professional customer support analyst",
            goal="Analyze customer complaints accurately.",
            constraints=[
                "Be concise.",
                "Use professional language.",
                "Do not invent information."
            ],
            text=sample_text
        )
    )

    print("\n" + "=" * 60)
    print("CHAIN-OF-THOUGHT")
    print("=" * 60)

    print(
        chain_of_thought_prompt(
            task="Determine whether the customer requires a refund.",
            text=sample_text
        )
    )

    print("\n" + "=" * 60)
    print("CONSTRAINED OUTPUT")
    print("=" * 60)

    print(
        constrained_output_prompt(
            task="Classify the customer's sentiment.",
            text=sample_text,
            output_format="Sentiment: <Positive | Negative | Neutral>"
        )
    )