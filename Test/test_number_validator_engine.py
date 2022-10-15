from number_parsing import number_validator_engine


def test_number_validator_engine_positive_length_10():
    assert number_validator_engine([9, 2, 6, 1, 2, 0, 2, 0, 2, 7]) is True


def test_number_validator_engine_positive_length_9():
    assert number_validator_engine([5, 2, 0, 8, 1, 2, 9, 6, 3]) is True


def test_number_validator_engine_positive_modulo_4():
    assert number_validator_engine([0, 8, 0, 2, 2, 9, 3, 1, 4, 0]) is True


def test_number_validator_engine_negative_modulo_11():
    assert number_validator_engine([9, 2, 6, 1, 2, 0, 2, 0, 2, 8]) is False


def test_number_validator_engine_negative_wrong_month_18():
    assert number_validator_engine([5, 2, 6, 8, 1, 2, 9, 6, 3]) is False


def test_number_validator_engine_negative_wrong_month_28():
    assert number_validator_engine([5, 2, 2, 8, 1, 2, 9, 6, 3]) is False


def test_number_validator_engine_negative_wrong_day_32():
    assert number_validator_engine([9, 2, 6, 1, 3, 2, 2, 0, 2, 7]) is False


def test_number_validator_engine_negative_wrong_suffix_000():
    assert number_validator_engine([5, 3, 0, 7, 0, 7, 0, 0, 0]) is False


def test_number_validator_engine_negative_wrong_year():
    assert number_validator_engine([5, 4, 0, 8, 1, 2, 9, 6, 3]) is False


def test_number_validator_engine_negative_modulo_4():
    assert number_validator_engine([0, 3, 0, 2, 2, 9, 3, 4, 6, 7]) is False
