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


def end_f(param):
    i = param
    n = 0
    if len(i) == 10:  # length is 10
        for _i in range(0, 9):
            # n *= 10
            n = n * 10 + i[_i]
        if n // 11 == 0:  # modulo 11 must be 0
            return True
        else:
            return False
    elif len(i) == 9:  # length is 9
        for _i in range(6, 8):
            # n *= 10
            n = n * 10 + i[_i]
        if n == 0:
            return True
        else:
            return False
    else:
        return False


def num_validator(num_list):
    i = num_list
    n = 0
    if i[2] != 0:
        if not ((i[2] == 1) or (i[2] == 6)):
            if i[2] == 5:
                if i[4] != 1:
                    if i[4] != 3:
                        if i[4] == 2:
                            if i[5] == 9:
                                for _i in range(0, 1):
                                    n = n * 10 + i[_i]
                                if n // 4 == 0:
                                    return end_f(i)
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
