import json
import os

from dotenv import load_dotenv
from google import genai

from src.schemas import ClassificationResult


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not set in the .env file."
    )


client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"


def classify_message(
    message: str,
    max_retries: int = 3,
) -> ClassificationResult:
    """
    Classify a customer-support message.

    Returns validated JSON containing:
    category, priority, sentiment, and needs_human.
    """

    prompt = f"""
You are a customer support classification assistant.

Classify the following customer-support message:

{message}

Return ONLY valid JSON with exactly these fields:

{{
    "category": "billing | technical | account | shipping | product | refund | other",
    "priority": "low | medium | high | critical",
    "sentiment": "positive | neutral | negative",
    "needs_human": true
}}

Rules:
- Return JSON only.
- Do not include Markdown.
- Do not include explanations.
- Do not add extra fields.
- Do not invent information.
- needs_human must be true or false.
""".strip()

    last_error = None

    for attempt in range(1, max_retries + 1):

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config={
                    "response_mime_type": "application/json"
                },
            )

            if not response.text:
                raise ValueError(
                    "Gemini returned an empty response."
                )

            data = json.loads(response.text)

            return ClassificationResult.model_validate(data)

        except (
            json.JSONDecodeError,
            ValueError,
        ) as error:

            last_error = error

            print(
                f"Classification attempt "
                f"{attempt}/{max_retries} failed: {error}"
            )

    raise RuntimeError(
        f"Classification failed after {max_retries} attempts."
    ) from last_error


if __name__ == "__main__":

    message = (
        "My payment was deducted twice and "
        "I need this fixed immediately."
    )

    result = classify_message(message)

    print("\nClassification Result:")
    print(result.model_dump_json(indent=2))