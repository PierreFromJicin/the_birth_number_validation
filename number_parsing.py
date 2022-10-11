def slash_find(str_in=""):
    # str_in_len = len(str_in)
    print(len(str_in))
    li_str_in = list(str_in)
    print(li_str_in)

    for _i in range(len(str_in)):
        print(_i)
        if li_str_in[_i] != chr(0x2f):
            continue
        else:
            return _i
    return -1
    
# TODO z listu stringu vyjmout slash (Main)
# TODO převést list stringu na list číslic (Main)
# TODO samotný algoritmus analýzy (ify) a výstup True/False (this file)

Def num_validator(*arg):
	pass


