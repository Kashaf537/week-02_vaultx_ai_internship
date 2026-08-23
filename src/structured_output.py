import json
import os

from dotenv import load_dotenv
from google import genai
from pydantic import ValidationError

from src.schemas import StructuredResponse


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not set in the .env file."
    )


client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.6-flash"


def create_prompt(text: str) -> str:
    """
    Create a prompt that requires strict JSON output.
    """

    return f"""
You are a customer support classification assistant.

Analyze the following customer message:

{text}

Return ONLY valid JSON.

The JSON must contain exactly these fields:

{{
    "category": "string",
    "priority": "low | medium | high | critical",
    "sentiment": "positive | neutral | negative",
    "needs_human": true
}}

Rules:

- Return valid JSON only.
- Do not use Markdown.
- Do not include explanations.
- Do not add extra fields.
- Do not invent information.
- needs_human must be true or false.
""".strip()


def generate_structured_output(
    text: str,
    max_retries: int = 3
) -> StructuredResponse:

    prompt = create_prompt(text)

    last_error = None

    for attempt in range(1, max_retries + 1):

        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config={
                    "response_mime_type": "application/json"
                }
            )

            if not response.text:
                raise ValueError(
                    "Gemini returned an empty response."
                )

            # Parse JSON
            data = json.loads(response.text)

            # Validate with Pydantic
            result = StructuredResponse.model_validate(data)

            return result

        except (
            json.JSONDecodeError,
            ValidationError,
            ValueError
        ) as error:

            last_error = error

            print(
                f"Attempt {attempt}/{max_retries} failed: "
                f"{error}"
            )

    raise RuntimeError(
        f"Structured output failed after "
        f"{max_retries} attempts."
    ) from last_error


if __name__ == "__main__":

    message = (
        "My payment was deducted twice and "
        "I need someone to fix this immediately."
    )

    result = generate_structured_output(message)

    print("\nValidated result:")
    print(result.model_dump_json(indent=2))