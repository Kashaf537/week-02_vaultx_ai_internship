"""
Reusable Structured Output Module

Provides reusable functions for:
- Customer-support classification
- Structured field extraction
- Logging
- Error handling
"""

import logging
from typing import Any

from src.classifier import classify_message
from src.extractor import extract_fields


# ============================================================
# LOGGING
# ============================================================

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


# ============================================================
# CLASSIFICATION
# ============================================================

def classify(text: str) -> dict[str, Any]:
    """
    Classify a customer-support message.

    Returns:
        Dictionary containing:
        category, priority, sentiment, needs_human.
    """

    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")

    try:
        logger.info("Classifying input text.")

        result = classify_message(text)

        logger.info("Classification completed successfully.")

        return result.model_dump()

    except Exception as error:
        logger.error("Classification failed: %s", error)
        raise


# ============================================================
# FIELD EXTRACTION
# ============================================================

def extract(text: str) -> dict[str, Any]:
    """
    Extract structured fields from messy text.

    Missing fields are handled by the extraction function.
    """

    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")

    try:
        logger.info("Extracting structured fields.")

        result = extract_fields(text)

        logger.info("Extraction completed successfully.")

        if hasattr(result, "model_dump"):
            return result.model_dump()

        return result

    except Exception as error:
        logger.error("Extraction failed: %s", error)
        raise


# ============================================================
# MODULE TEST
# ============================================================

if __name__ == "__main__":

    print("Structured Output Module")
    print("------------------------")
    print("Available functions:")
    print("- classify(text)")
    print("- extract(text)")