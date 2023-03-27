import time
from functools import reduce
import my_calc


def square(x):
    perimeter = 4 * x
    sq = x**2
    diagonal = (x**2) * 2
    return perimeter, sq, diagonal


print('---Ex. 4.1:---\n')
print(square(5))

# --------------------------


def print_values(**kwargs):
    d = dict(kwargs)
    [print(f'{keys} : {values}') for keys, values in d.items()]


print('\n---Ex. 4.2:---\n')
print_values(name='John', last_name='Smith', age=35, position='web developer')

# --------------------------

my_list = [20, -3, 15, 2, -1, -21]
new_lst = filter(lambda x: x > 0, my_list)

print('\n---Ex. 4.3:---\n')
print(list(new_lst))

# --------------------------

result = reduce(lambda x, y: x * y, my_list)

print('\n---Ex. 4.4:---\n')
print(result)

# --------------------------


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        result_time = end_time - start_time
        print(f"function work time: {result_time} sec.")
        return func(*args, **kwargs)
    return wrapper


@decorator
def get_nod(a, b):
    '''Вычисляется НОД (наибольший общий делитель)
    для двух натуральных чисел a, b по алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    '''

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


print('\n---Ex. 4.5:---\n')
print(get_nod(2, 1000000))


# --------------------------

print('\n---Ex. 4.6:---\n')
print(my_calc.minus_args(5, 3))
print(my_calc.divide_args(5, 2))
print(my_calc.multiple_args(5, 2))
print(my_calc.sum_args(5, 2))



