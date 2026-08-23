from src.schemas import ExtractionResult


def test_extraction_with_all_fields():

    result = ExtractionResult(
        name="Sarah Ahmed",
        email="sarah@example.com",
        invoice_number="INV-2026-1042",
        date="August 20, 2026",
        total_amount=245.50,
        currency="USD",
    )

    assert result.name == "Sarah Ahmed"
    assert result.email == "sarah@example.com"
    assert result.invoice_number == "INV-2026-1042"
    assert result.total_amount == 245.50


def test_extraction_with_missing_fields():

    result = ExtractionResult(
        name="Ali Khan",
        email="ali@example.com",
        total_amount=12500,
        currency="PKR",
    )

    assert result.name == "Ali Khan"
    assert result.email == "ali@example.com"
    assert result.invoice_number is None
    assert result.date is None
    assert result.total_amount == 12500