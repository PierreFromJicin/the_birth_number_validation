import string_parsing,*

cl_in: str = input('enter the birth number (you can use slash separator or not) --> ')

slash_index = string_parsing.slash_find(cl_in)

if slash_index == -1:
    print('has been entered birth number without slash')
else:
    print(f"Slash is on index:  {slash_index} in the string.")


# převod list stringu na list číslic
li_num = []
def list_convertor(li_str_in):
    for _i in range(len(li_str_in)):
        if li_str_in[_i] isdigit:
            li_num += int(li_str_in[_i])
            continue
        else:
            return _i
            break
    return li_num


li_num = list_convertor(li_str_in)
print(f"list čísel: {li_num})
