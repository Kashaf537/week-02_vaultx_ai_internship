import json
import time
from pathlib import Path

from src.classifier import classify_message


DATA_FILE = (
    Path(__file__).parent.parent
    / "eval"
    / "classification_samples.json"
)

OUTPUT_FILE = (
    Path(__file__).parent.parent
    / "outputs"
    / "classifier_results.json"
)


def main():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        samples = json.load(file)

    results = []

    for index, sample in enumerate(samples, start=1):

        print(f"\nProcessing sample {index}/{len(samples)}...")
        print(f"Input: {sample['text']}")

        try:
            result = classify_message(sample["text"])

            print(f"Predicted: {result.model_dump()}")

            results.append({
                "text": sample["text"],
                "expected": {
                    "category": sample["category"],
                    "priority": sample["priority"],
                    "sentiment": sample["sentiment"],
                    "needs_human": sample["needs_human"],
                },
                "predicted": result.model_dump(),
            })

        except Exception as error:

            print(f"Sample {index} failed: {error}")

            results.append({
                "text": sample["text"],
                "expected": {
                    "category": sample["category"],
                    "priority": sample["priority"],
                    "sentiment": sample["sentiment"],
                    "needs_human": sample["needs_human"],
                },
                "predicted": None,
                "error": str(error),
            })

        # Wait before the next API request.
        # This helps avoid Gemini free-tier rate limits.
        if index < len(samples):
            print("Waiting 15 seconds...")
            time.sleep(15)

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)

    print("\n" + "=" * 60)
    print("20-SAMPLE RUN COMPLETE")
    print("=" * 60)
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()