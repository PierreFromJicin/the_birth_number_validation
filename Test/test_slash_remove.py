from string_parsing import digits_filter


def test_output_digits_string_positive():
    result = digits_filter('761120/5085')
    assert result == "7611205085"


def test_output_digits_string_negative():
    result = digits_filter('7a1120/5085')
    assert result == "711205085"
