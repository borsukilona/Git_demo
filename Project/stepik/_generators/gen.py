# можно определить генератор без привязки к каой-либо коллекции (спискам, словарям и т.д.)

# вернуть числа в квадрате в диапазоне
a = (x ** 2 for x in range(6))
# переменная a и есть теперь сам генератор


next(a)
# 0
next(a)
# 1
next(a)
# 4 и т.д.


# мы можем перебрать эелементы генератора только один раз от начала до конца
for x in a:
    print(x)


# превращаем генератор в список
# мы сможем воспользоваться этой функцией для одного и того же генератора всего один раз (генератор можно перебирать только один раз!)
list(a)
# [0, 1, 4, 9, 16, 25]


# превращаем генератор в множество
# мы сможем воспользоваться этой функцией для одного и того же генератора всего один раз (генератор можно перебирать только один раз!)
set(a)
# {0, 1, 4, 9, 16, 25}


# можем прописать генератор внутри функции
# мы сможем воспользоваться этой функцией для одного и того же генератора всего один раз (генератор можно перебирать только один раз!)
sum(a) # sum((x ** 2 for x in range(6)))
# 55
max(a) # max((x ** 2 for x in range(6)))
# 25


# зачем нужны такие генераторы?
'''
если нам нужен огромный рендж цифр range(1000000000), то список такой не создашь, не хватить у него места
а генератор создашь, потому что генератор не хранит в себе все эти числа, генератор ГЕНЕРИРУЕТ их по ходу дела
'''
numbers = (x for x in range(1000000000))
for x in numbers:
    print(x, end=" ")
    if x > 50:
        break
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51


for x in numbers:
    if x < 50:
        print(x, end=" ")
    else:
        break

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49