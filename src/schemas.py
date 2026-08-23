from typing import Literal

from pydantic import BaseModel, Field


class ClassificationResult(BaseModel):
    """Validated output for customer-support classification."""

    category: Literal[
        "billing",
        "technical",
        "account",
        "shipping",
        "product",
        "refund",
        "other",
    ] = Field(description="Customer support category.")

    priority: Literal[
        "low",
        "medium",
        "high",
        "critical",
    ] = Field(description="Priority of the support request.")

    sentiment: Literal[
        "positive",
        "neutral",
        "negative",
    ] = Field(description="Customer sentiment.")

    needs_human: bool = Field(
        description="Whether the issue requires human intervention."
    )