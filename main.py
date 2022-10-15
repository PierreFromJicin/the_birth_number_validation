from number_parsing import *
from string_parsing import *

command_line_input: str = input('enter the birth number (you can use the slash separator if you want) --> ')

# slash_index = slash_find(cl_in)
#
# '''
# if slash_index[0] == -1:
#     print('has been entered birth number without slash')
# else:
#     print(f"Slash is on index:  {slash_index[0]} in the string.")
# '''

digits_string = digits_filter(command_line_input)
birth_number = list_convertor(digits_string)

# NOTE num_validator in number_parsing module has been written according flowchart included in git repo.

if len(birth_number) == 10 or len(birth_number) == 9:
    if number_validator_engine(birth_number):
        print(f"The birth number is VALID.")
    else:
        print("The birth number is NOT VALID.")
else:
    print(f"Wrong length of the entered birth number: {len(birth_number)}")
