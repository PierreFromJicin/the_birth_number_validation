from number_parsing import list_convertor


def test_output_list_convertor_positive():
    result = list_convertor(["8", "0", "5", "2", "2", "8", "4", "0", "2", "0"])
    assert result == [8, 0, 5, 2, 2, 8, 4, 0, 2, 0]
