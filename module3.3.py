def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(7, None, False)
print()
print_params(b = 25)
print('Функция print_params(b=25) работает корректно')
print_params(c = [1, 2, 3])
print('Функция print_params(c = [1,2,3]) работает корректно')

values_list = [23, False, ([2, 1], 'Yes')]
print(type(values_list))
values_dict = {'a': None, 'b': None, 'c': None}
print(values_dict)
print_params(**values_dict)
print_params(*values_list)

values_list_2 = [27, 'собака']
print_params(*values_list_2, 42) # работает тк мы все три места в функции заняли и вывели



