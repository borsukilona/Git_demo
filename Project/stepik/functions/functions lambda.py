from functools import reduce

s = lambda a, b: a + b
a = 2
b = 3
s(a, b) #5

a = [4, 5, lambda: print('lambda'), 7, 8]
#[4, 5, <function <lambda> at 0x0000025D021BF9C0>, 7, 8]
a[2]() #lambda вызываем функцию

#------------------------------------------------------------
#выбрать значения из списка по определенному фильтру
lst = [5, 3, 0, -6, 8, 10, 1]


def get_filter(lst, filter=None):
    if filter is None:
        return lst
    else:
        res = []
        for el in lst:
            if filter(el):
                res.append(el)
        return res


r = get_filter(lst, lambda el: el % 2 == 0) #только четные числа, наша лямбда и есть фильтр (возвращает TRUE если число положительное)
print(r) #[0, -6, 8, 10]

# ------------------------------------------------------------
# reduce выполняет действие указанное по цепочке
# вот здесь мы отнимаем элементы: 20 - 15 - 8 - 7 - 6 = -16
# суммируем все элементы: 20 + 15 + 8 + 7 + 6 = 56
# можем перемножить все элементы или что угодно сделать: 20 * 15 * 8 * 7 * 6 = 100800


lst = [20, 15, 8, 7, 6]
result = reduce(lambda x, y: x - y, lst) # -16
result = reduce(lambda x, y: x + y, lst) # 56
result = reduce(lambda x, y: x * y, lst) # 100800

# ------------------------------------------------------------
# отсортируем список по числовым значениям

lst = ['aaa 12', 'bbb 3', 'ccc 15', 'ddd 2']
sorted(lst, key=lambda x: int(x.split()[1]))
# ['ddd 2', 'bbb 3', 'aaa 12', 'ccc 15']

