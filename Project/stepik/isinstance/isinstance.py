# проверка на тип данных

a = 5
isinstance(a, int) # True
isinstance(a, float) # False

b = True
isinstance(b, bool) # True
isinstance(b, int) # тоже True, потому что тип bool наследуется от типа int
# как проверить наверняка только булевое значение:
type(b) == bool # True
type(b) == int # False

# равенство на несколько типов данных (похоже на запрос в sql)
type(b) in (bool, str, float) # True (потому что хоть один подходит)

# равенство на несколько типов данных isinstance (похоже на запрос в sql)
isinstance(a, (int, float)) # True (потому что хоть один подходит)

'''
если type(b) это строгое равенство на определнный тип, то isinstance(b, int) делает проверку с учетом иерархии наследования типов/обьектов 
(как в случае с булевым и int) 
isinstance проверяет принадлежность обекта к тому или иному классу
'''

# --------------------------------------------------------------------------
# посчитать сумму только вещественных чисел

data = (4.5, 8.7, True, "book", 8, 10, -11, [True, False])
sum_float = sum([x for x in data if isinstance(x, float)])
# sum_float = sum(filter(lambda x: isinstance(x, float), data))
print(sum_float)
# 13.2

# --------------------------------------------------------------------------
# посчитать сумму только целых чисел

sum_int = sum(filter(lambda x: type(x) is int, data))
print(sum_int)
# 7

'''
использовали type, потому что только так мы сможем найти только целые числа
функция isinstance посчитает значение True ещё (True = 1) и прибавит его к нашей сумме, а нам оно не надо
'''

# --------------------------------------------------------------------------

