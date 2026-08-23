import json
import os

from dotenv import load_dotenv
from google import genai

from src.schemas import ExtractionResult


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not set in the .env file."
    )


client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.6-flash"


def extract_fields(
    text: str,
    max_retries: int = 3,
) -> ExtractionResult:
    """
    Extract structured fields from messy text.

    Missing fields are returned as null.
    """

    prompt = f"""
You are an information extraction assistant.

Extract the following fields from the provided text:

- name
- email
- invoice_number
- date
- total_amount
- currency

Text:

{text}

Return ONLY valid JSON using exactly these fields:

{{
    "name": null,
    "email": null,
    "invoice_number": null,
    "date": null,
    "total_amount": null,
    "currency": null
}}

Rules:
- Return JSON only.
- Do not add explanations.
- Do not add extra fields.
- If a field is missing, return null.
- Do not guess or invent missing information.
- total_amount must be a number or null.
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

            return ExtractionResult.model_validate(data)

        except (
            json.JSONDecodeError,
            ValueError,
        ) as error:

            last_error = error

            print(
                f"Extraction attempt "
                f"{attempt}/{max_retries} failed: {error}"
            )

    raise RuntimeError(
        f"Extraction failed after {max_retries} attempts."
    ) from last_error


if __name__ == "__main__":

    sample_text = """
    Invoice #INV-2026-1042
    Date: August 20, 2026

    Customer: Sarah Ahmed
    Email: sarah@example.com

    Total: USD 245.50

    Thank you for your business.
    """

    result = extract_fields(sample_text)

    print("\nExtraction Result:")
    print(result.model_dump_json(indent=2))