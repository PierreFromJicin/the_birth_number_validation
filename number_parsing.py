import string


def list_convertor(*tu_str):
    li_str = list(tu_str[0])
    li_num = []
    for _i in range(len(li_str)):
        if str(li_str[_i]) not in string.digits:
            return False
        else:
            li_num.append(int(li_str[_i]))
            continue
    return li_num


# TODO samotný algoritmus analýzy (ify) a výstup True/False (this file)

def num_validator(num_list):
    pass
