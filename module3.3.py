def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    print(a)
    print(c)
    print(b)
    print(b + b)
    print()
    # print_params(b = 25) # работает не корректно?
    # print_params(a, b, c = [1, 2, 3]) # ?
print_params()

values_list = [23, False, ([2, 1], 'Yes')]
print(type(values_list))
values_dict = {'a': None, 'b': None, 'c': None}
if len(values_dict) == len(values_list):
    for key, value in zip(values_dict.keys(), values_list):
        values_dict[key] = value
print(values_dict)
print_params(**values_dict)
print_params(*values_list)

values_list_2 = [27, 'собака']
print_params(*values_list_2, 42) # работает тк мы все три места в функции заняли и вывели



