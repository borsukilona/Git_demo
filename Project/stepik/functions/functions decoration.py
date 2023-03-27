import math
import time
from functools import wraps

def func_decorator(func):  # func - этот параметр будет функцией, которую мы будем вызывать потом
    def wrapper():
        print("---do something before func()---")
        func()
        print("---do something after func()---")

    return wrapper


def some_func():
    print("we call some_func functions")


# some_func = func_decorator(some_func)
# some_func()

# ---do something before func()---
# we call some_func functions
# ---do something after func()---

# в итоге мы расширили функционал функции some_func
# и some_func() и wrapper() должны иметь одинаковое количество агрументов внутри
# чтобы не заморачиваться над количество аргументов в обеих функциях, можно сделать так:

'''
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("---do something before func()---")
        func(*args, **kwargs)
        print("---do something after func()---")

    return wrapper


def some_func():
    print("we call some_func functions")
'''


# ---------------------------------------------------------------
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("---do something before func()---")
        res = func(*args, **kwargs)
        print("---do something after func()---")
        return res

    return wrapper


def some_func(title, tag):
    print("we call some_func functions")
    return f"<{tag}>{title}</{tag}>"


# some_func = func_decorator(some_func)
# a = some_func("Phyton", "h1")
# print(a)

# ---do something before func()---
# we call some_func functions
# ---do something after func()---
# <h1>Phyton</h1>

# ---------------------------------------------------------------
# измерение работы функции (любой функции)
def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()  # время начала работы
        res = func(*args, **kwargs)
        et = time.time()  # время окончания работы
        dt = et - st  # затраченное время на работу
        print(f"function work time: {round(dt, 2)} sec.")
        return res

    return wrapper


# медленный алгоритм евклида
@test_time  # можно сделать так, и это будет означать, что теперь наша функция get_nod декорирована функцией test_time
def get_nod(a, b):
    '''Вычисляется НОД (наибольший общий делитель)
    для двух натуральных чисел a, b по алгоритму Евклида
    :param a: первое натурльное число
    :param b: второе натуральное число
    :return: НОД
    '''

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


# get_nod = test_time(get_nod)
res = get_nod(2, 1000000)
print(res)


# function work time: 0.03 sec.
# 2

# ---------------------------------------------------------------
# вычисляем производное функции (производная функции описывает, как и с какой скоростью эта функция меняется в данной конкретной точке)
def f_decorator(func):
    def wrapper(x, *args, **kwargs):  # x это точка, в которой мы будем вычислять производное функции
        dx = 0.0001
        res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
        return res

    return wrapper


@f_decorator
def sin_df(x):
    return math.sin(x)


# print(sin_df(math.pi/3))
# 0.4999566978958203 - это значение производной в точке Pi/3'''


# ---------------------------------------------------------------
# декоратор с параметром

'''def df_decorator(dx=0.01):
    def decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        return wrapper
    return decorator


@df_decorator(dx=0.00001)
def sin_df(x):
    return math.sin(x)


#f = df_decorator(dx=0.00001)
#sin_df = f(sin_df)
print(sin_df(math.pi/3)) #0.499995669867026'''


# ---------------------------------------------------------------
# сохранение имени функции

def df_decorator(dx=0.01):
    def decorator(func):
        @wraps(func) #вместо строк wrapper.__name__ = func.__name__ и т.д.
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        #wrapper.__name__ = func.__name__ #сохранить имя функции
        #wrapper.__doc__ = func.__doc__ #сохранить описание функции
        return wrapper

    return decorator


@df_decorator(dx=0.00001)
def sin_df(x):
    '''Функуция для вычисления производной синуса'''
    return math.sin(x)


print(sin_df.__name__)  # sin_df
print(sin_df.__doc__) # Функуция для вычисления производной синуса
