import json
from pathlib import Path

from src.classifier import classify_message


BASE_DIR = Path(__file__).parent.parent

INPUT_FILE = BASE_DIR / "eval" / "evaluation_samples.json"
OUTPUT_FILE = BASE_DIR / "eval" / "evaluation_results.json"


def compare_results(expected, predicted):
    """
    Compare expected and predicted classification fields.
    """

    fields = [
        "category",
        "priority",
        "sentiment",
        "needs_human",
    ]

    correct = 0

    for field in fields:
        if expected[field] == predicted[field]:
            correct += 1

    return correct == len(fields), correct


def main():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        samples = json.load(file)

    results = []

    fully_correct = 0
    total_fields = 0
    correct_fields = 0

    for index, sample in enumerate(samples, start=1):

        print(f"\nEvaluating sample {index}/{len(samples)}")

        try:
            prediction = classify_message(sample["text"])

            predicted = prediction.model_dump()

            is_correct, field_count = compare_results(
                sample["expected"],
                predicted,
            )

            if is_correct:
                fully_correct += 1

            correct_fields += field_count
            total_fields += 4

            results.append({
                "id": sample["id"],
                "text": sample["text"],
                "expected": sample["expected"],
                "predicted": predicted,
                "correct": is_correct,
            })

            print("Expected:", sample["expected"])
            print("Predicted:", predicted)

        except Exception as error:

            print("Error:", error)

            results.append({
                "id": sample["id"],
                "text": sample["text"],
                "expected": sample["expected"],
                "predicted": None,
                "correct": False,
                "error": str(error),
            })

    accuracy = fully_correct / len(samples)

    field_accuracy = (
    correct_fields / total_fields
    if total_fields > 0
    else 0
    )

    summary = {
        "total_samples": len(samples),
        "fully_correct": fully_correct,
        "accuracy": accuracy,
        "field_accuracy": field_accuracy,
    }

    output = {
        "summary": summary,
        "results": results,
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=2)

    print("\n" + "=" * 50)
    print("EVALUATION COMPLETE")
    print("=" * 50)

    print(f"Samples: {len(samples)}")
    print(f"Fully correct: {fully_correct}")
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Field accuracy: {field_accuracy:.2%}")

    print(f"\nResults saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()