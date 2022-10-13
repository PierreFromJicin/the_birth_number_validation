def slash_find(str_in=""):
    li_str_in = list(str_in)

    for _i in range(len(str_in)):
        if li_str_in[_i] != chr(0x2f):
            continue
        else:
            li_str_in.pop(_i)  # remove the first slash
            return _i, li_str_in
    return -1, li_str_in
