import string_parsing

cl_in: str = input('enter the birth number (you can use slash separator or not) --> ')

slash_index = string_parsing.slash_find(cl_in)

if slash_index == -1:
    print('has been entered birth number without slash')
else:
    print(f"Slash is on index:  {slash_index} in the string.")
