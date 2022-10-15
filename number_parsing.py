def list_convertor(string_in):
    output_list = []
    for item in string_in:
        output_list.append(int(item))
    return output_list


def end_f(param):
    i = param
    n = t = y = 0
    if len(i) == 10:  # length is 10
        for _i in range(0, 10):
            t = t * 10 + i[_i]
        if t % 11 == 0:  # modulo 11 must be 0
            return True
        else:
            return False
    elif len(i) == 9:  # length is 9
        for _i in range(6, 9):
            n = n * 10 + i[_i]
        if n == 0:
            return False
        else:
            for _i in range(0, 2):
                y = y * 10 + i[_i]
            if y < 54:  # year lower than 1954
                return True
            else:
                return False
    else:
        return False


def mid_f(param):
    i = param
    n = 0
    if i[4] != 3:
        if i[4] == 2:
            if i[5] == 9:
                for _i in range(0, 2):
                    n = n * 10 + i[_i]
                if n % 4 == 0:
                    return end_f(i)
                else:
                    return False
            else:
                return end_f(i)
        else:
            return False
    else:
        if i[5] == 0 or i[5] == 1:
            return end_f(i)
        else:
            return False


def number_validator_engine(num_list):
    i = num_list
    if i[2] != 0:
        if not (i[2] == 1 or i[2] == 6):
            if i[2] == 5:
                if i[4] != 1:
                    return mid_f(i)
                else:
                    return end_f(i)
            else:
                return False
        else:
            if i[3] == 0 or i[3] == 1 or i[3] == 2:
                if i[4] == 1:
                    return end_f(i)
                else:
                    return mid_f(i)
            return False
    else:
        if i[3] == 0:
            return False
        else:
            if i[4] == 1:
                return end_f(i)
            else:
                return mid_f(i)
