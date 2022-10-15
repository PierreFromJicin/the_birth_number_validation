from number_parsing import list_convertor


def test_string_length_10_without_slash():
    result = list_convertor(["7", "6", "1", "1", "2", "0", "5", "0", "8", "5"])
    assert result == [7, 6, 1, 1, 2, 0, 5, 0, 8, 5]
