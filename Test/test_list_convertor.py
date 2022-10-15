from number_parsing import list_convertor


def test_output_list_convertor_positive():
    result = list_convertor(["7", "6", "1", "1", "2", "0", "5", "0", "8", "5"])
    assert result == [7, 6, 1, 1, 2, 0, 5, 0, 8, 5]
