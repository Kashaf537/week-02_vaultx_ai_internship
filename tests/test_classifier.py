from src.schemas import ClassificationResult


def test_classification_result_valid():
    result = ClassificationResult(
        category="billing",
        priority="high",
        sentiment="negative",
        needs_human=True,
    )

    assert result.category == "billing"
    assert result.priority == "high"
    assert result.sentiment == "negative"
    assert result.needs_human is True


def test_classification_result_fields():
    result = ClassificationResult(
        category="technical",
        priority="medium",
        sentiment="neutral",
        needs_human=False,
    )

    assert result.model_dump() == {
        "category": "technical",
        "priority": "medium",
        "sentiment": "neutral",
        "needs_human": False,
    }