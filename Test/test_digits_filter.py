from string_parsing import digits_filter


def test_output_digits_string_positive():
    result = digits_filter('080229/3140')
    assert result == "0802293140"


def test_output_digits_string_negative():
    result = digits_filter('08OQ29/3140')
    assert result == "08293140"
