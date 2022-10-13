from number_parsing import *
from string_parsing import *

cl_in: str = input('enter the birth number (you can use slash separator or not) --> ')

slash_index = slash_find(cl_in)

if slash_index[0] == -1:
    print('has been entered birth number without slash')
else:
    print(f"Slash is on index:  {slash_index[0]} in the string.")

tu_str_in = slash_find(cl_in)
print(f"tu_str_in[1]: {tu_str_in[1]}")
birth_num = list_convertor(tu_str_in[1])
print(f"list čísel: {birth_num}")

# TODO postoupit do validátoru pouze pokud:
#  hodnota birth_num bude True a zároveň délka listu birt_num bude 9, nebo 10