from src.structured_output import classify, extract


def test_empty_classification_input():
    try:
        classify("")
        assert False
    except ValueError:
        assert True


def test_empty_extraction_input():
    try:
        extract("")
        assert False
    except ValueError:
        assert True