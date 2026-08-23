from prompt_templates import (
    zero_shot_prompt,
    few_shot_prompt,
    role_system_prompt,
    chain_of_thought_prompt,
    constrained_output_prompt,
)


def test_zero_shot():
    prompt = zero_shot_prompt(
        task="Classify sentiment.",
        text="The service was excellent."
    )

    assert "Classify sentiment." in prompt
    assert "The service was excellent." in prompt


def test_few_shot():
    examples = [
        {
            "input": "The service was excellent.",
            "output": "Positive"
        },
        {
            "input": "The service was terrible.",
            "output": "Negative"
        }
    ]

    prompt = few_shot_prompt(
        task="Classify sentiment.",
        examples=examples,
        text="The service was acceptable."
    )

    assert "Example 1" in prompt
    assert "Example 2" in prompt
    assert "The service was acceptable." in prompt


def test_role_system():
    prompt = role_system_prompt(
        role="a customer support analyst",
        goal="Analyze customer complaints.",
        constraints=["Be concise."],
        text="The product is damaged."
    )

    assert "customer support analyst" in prompt
    assert "Analyze customer complaints." in prompt
    assert "Be concise." in prompt


def test_chain_of_thought():
    prompt = chain_of_thought_prompt(
        task="Determine the sentiment.",
        text="The product is excellent."
    )

    assert "Determine the sentiment." in prompt
    assert "The product is excellent." in prompt


def test_constrained_output():
    prompt = constrained_output_prompt(
        task="Classify sentiment.",
        text="The service was excellent.",
        output_format="Sentiment: <Positive | Negative | Neutral>"
    )

    assert "Sentiment:" in prompt
    assert "The service was excellent." in prompt
    assert "Do not add extra sections" in prompt


if __name__ == "__main__":
    test_zero_shot()
    test_few_shot()
    test_role_system()
    test_chain_of_thought()
    test_constrained_output()

    print("All prompt template tests passed.")