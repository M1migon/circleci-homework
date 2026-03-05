from text_stats import text_stats


def test_empty_string():
    assert text_stats("") == {"digits": 0, "letters": 0, "upper": 0, "lower": 0, "symbols": 0}


def test_only_digits():
    assert text_stats("012345") == {"digits": 6, "letters": 0, "upper": 0, "lower": 0, "symbols": 0}


def test_only_lower_letters():
    assert text_stats("abcxyz") == {"digits": 0, "letters": 6, "upper": 0, "lower": 6, "symbols": 0}


def test_only_upper_letters():
    assert text_stats("ABC") == {"digits": 0, "letters": 3, "upper": 3, "lower": 0, "symbols": 0}


def test_mixed_letters_cases():
    assert text_stats("aBcD") == {"digits": 0, "letters": 4, "upper": 2, "lower": 2, "symbols": 0}


def test_letters_digits_symbols():
    assert text_stats("Ab12!") == {"digits": 2, "letters": 2, "upper": 1, "lower": 1, "symbols": 1}


def test_spaces_are_symbols():
    assert text_stats("A a") == {"digits": 0, "letters": 2, "upper": 1, "lower": 1, "symbols": 1}


def test_punctuation_symbols_count():
    assert text_stats("Hi, Bob!") == {"digits": 0, "letters": 5, "upper": 2, "lower": 3, "symbols": 3}


def test_unicode_letters():
    assert text_stats("ПривітAa") == {"digits": 0, "letters": 8, "upper": 1, "lower": 7, "symbols": 0}


def test_none_input():
    assert text_stats(None) == {"digits": 0, "letters": 0, "upper": 0, "lower": 0, "symbols": 0}
