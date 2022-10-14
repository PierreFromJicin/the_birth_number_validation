from number_parsing import *
from string_parsing import *

cl_in: str = input('enter the birth number (you can use the slash separator if you want) --> ')

slash_index = slash_find(cl_in)

'''
if slash_index[0] == -1:
    print('has been entered birth number without slash')
else:
    print(f"Slash is on index:  {slash_index[0]} in the string.")
'''

tu_str_in = slash_find(cl_in)
birth_num = list_convertor(tu_str_in[1])

# NOTE num_validator in number_parsing module has been written according flowchart included in git repo.

if birth_num:
    if len(birth_num) == 10 or len(birth_num) == 9:
        if num_validator(birth_num):
            print(f"The birth number is VALID.")
        else:
            print("The birth number is NOT VALID.")
    else:
        print(f"Wrong length of the entered birth number: {len(birth_num)}")
else:
    print(f"Wrong format of the entered birth number: {birth_num}")
