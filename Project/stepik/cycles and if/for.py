d = [1, 2, 3, 4, 5]

#перебор символов списка
'''for i in d:
    print(i)''' ##i ссылается сам элемент из списка d

#произведение элементов списка
'''p = 1
for i in d:
    p += i
print(p)'''

#замена элементов в списке на 0
'''for i in [0, 1, 2, 3, 4]: #индексы списка
    d[i] = 0 #i ссылается на индекс элемента из списка d
print(d)'''

#замена элементов в списке на 0
'''for i in range(0, len(d)): #индексы списка от 0 до 4 
    d[i] = 0
print(d)'''

list(range(5)) #[0, 1, 2, 3, 4]
list(range(0, 10, 2)) #[0, 2, 4, 6, 8]
list(range(1, 10, 2)) #[1, 3, 5, 7, 9]
list(range(10, 0, -1)) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#s = 1/2 + 1/3 + 1/4 +... 1/1000
'''s = 0
for i in range(2,1001):
    s += 1/i
print(round(s,2))'''

'''for i in range(len(cities)-1):
    if cities[i][-1] == cities[i+1][0]:
        s = "ДА"
    elif cities[i][-2] != cities[i+1][0] and (cities[i][-1] == 'ь' or cities[i][-1] == 'ъ' or cities[i][-1] == 'ы'):
        s = "ДА"
    else:
        s = "НЕТ"'''


#факториал от числа n
'''n = int(input())
s = 1
if 1 > n or n > 100:
    print("not possible value!")
else:
    for i in range(1, n+1):
        s *= i
    print(s)'''


#отобразим елочку
#*
#**
#***
#****
#*****
'''s = ""
for i in range(1, 6):
    s += "*"
    # print("*" * i)
    print(s)'''


#объединить слова из списка в одну строку
'''lst = ["Python", "give", "me", "love"]
s = ""
for i in range(len(lst)): #for i in lst:
    s += lst[i] + " "     #s += i + " "
print(s)'''


#все двухзначные числа заменить на 0
lst = [4, 3, 100, -53, -30, 1, 34, -8]
a = 0

'''for i in range(len(lst)):
    if len(str(abs(lst[i]))) == 2: #if 10 <= abs(lst[i]) <= 99
        lst[i] = a
print(lst)'''

#enumerate
#возвращает и индекс и значение списка (тут i будет индексом элемента, n будет значением элемента)
'''for i, n in enumerate(lst):
    if 10 <= abs(n) <= 99:
        lst[i] = a #только обращаясь к текущему элементу списка по индексу мы можем изменить значение этого элемента, поэтому мы не можем записать 'n = a'
print(lst)'''


#преобразование кириллицы в латиницу
'''t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а') #значение кода для русской первой буквы алфавита - а
title = "Программирование на Python - лучший курс"
slug = '' #будет хранить преобразование кириллицы в латиницу

for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s) - start_index] #в кодовой таблице все буквы стоят по порядку; разность вернет нам индекс буквы из списка t
    elif s == 'ё':
        slug += 'yo'
    elif s in ' ?!:;.,':
        slug += '-'
    else:
        slug += s
print(slug) #programmirovanie-na-python---luchshiy-kurs

while slug.count("--"):
    slug = slug.replace("--","-")
print(slug) #programmirovanie-na-python-luchshiy-kurs'''

#iterator
'''d = [5, 3, 7, 10, 32]
it = iter(d)
next(it) #каждый раз когда мы будем вызывать эту функцию, она будет возвращать следующий элемент по списку d;
#когда мы дойдем до конца и вызовем функцию ещё раз, то итерация уже закончится и будет уже ошибка, бо больше нечего перечислять
#если нам надо повторно перебрать элементы, придется создать ещё один итератор

r = range(5)
it = iter(r)
next(it) #перебор значений от 0 до 4'''

'''
n = 4568
print(*str(n)) #4 5 6 8
'''




