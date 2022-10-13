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
	i = num_list
	if i[2] != 0:
		if not((i[2] = 1) or (i[2] = 6)):
			if i[2] = 5:
				if i[4] != 1:
					if i[4] != 3:
						if i[4] = 2:
							if i[5] != 9:
								if len(i)=10:
									for _i in range(0, 9):
										# n *= 10
										n = n*10+i[_i]
									if n // 11 = 0:
										return True
										else:
											return False
								elif len(i)=9:
									for _i in range(6, 8):
										# n *= 10
										ns = ns*10+i[_i]
										if ns == 0:
											return True
										else:
											False
										
								
    return False
