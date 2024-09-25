def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(26)
print_params(5, 'столбец', False)
print_params("","","")
print_params(b=25)
print_params(c=[1,2,3])

values_list = [123, None, 'Urban']
values_dict = {'a':1234.876, 'b':'Привет', 'c':True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = (54.32, 'Строка')
print_params(*values_list_2, 42)