'''
Необходимо записать генератор, который бы используя этот список, выдавал 1 000 000 наименований городов по циклу.
То есть, дойдя до конца списка, возвращался в начало и повторял перебор. И так, для выдачи миллиона названий.
'''
import math
from typing import Any

cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

lst = []

for i in range(11):
    lst.append(cities[i % len(cities)])

print(lst)

# gen = (cities[i % n] for i in range(1_000_000))

# ---------------------------------------------------------------------------------------------------------------------
# функция, которая формирует диапазон с вещественным шагом (ибо range принимает только целые числа в этом плане и возникает ошибка)
import decimal #десятичный модуль
# тип float имеет точность до 15 знаков, а decimal — настраиваемую пользователем

def float_range(start, stop, step):
  while start < stop:
      yield float(start)
      start += decimal.Decimal(step)


print(list(float_range(0, 1, '0.1')))
# [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# ---------------------------------------------------------------------------------------------------------------------
#простое ли число или нет


def isPrime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count > 0:
        return False
    else:
        return True

# ---------------------------------------------------------------------------------------------------------------------
# пирамидка и сумма чисел в каждой строке пирамидки
'''
numbers = (x for x in range(56) if x % 2 != 0)
l = list(numbers)

#1 -> 0 + 1 = 1 [0:1]
#2 -> 1 + 2 = 3 [1:3]
#3 -> 3 + 3 = 6 [3:6]
#4 -> 6 + 4 = 10 [6:10]

#print(l[0:1])
#print(l[1:3])
#print(l[3:6])
#print(l[6:10])
l2 = []

start = 0
finish = 0

for i in range(len(l)):
    start += i
    finish += i+1
    row = l[start:finish]
    if len(row) == 0:
        break
    l2.append(row)

print(l2)
n = 3
summ = 0
for i, el in enumerate(l2):
    if i == (n-1):
        summ = sum(el)
print(summ)
'''


def row_sum_odd_numbers(n):
    numbers = (x for x in range(56) if x % 2 != 0)
    l = list(numbers)

    l2 = []

    start = 0
    finish = 0

    for i in range(len(l)):
        start += i
        finish += i + 1
        row = l[start:finish]
        if len(row) == 0:
            break
        l2.append(row)

    itog = 0
    for i, el in enumerate(l2):
        if i == (n - 1):
            itog = sum(el)

    return itog

print(row_sum_odd_numbers(3))

# -----------------------------------------------------
lst = []
lst2 = []
count = 1
for _ in range(6):
    lst.append('*'*count)
    count += 2

for el in lst:
    last_el = len(lst[-1])
    if len(el) < last_el:
        x = int((last_el - len(el)) / 2)
        lst2.append(' '*x + el + ' '*x)
    else:
        lst2.append(el)
    print(el)

print(lst2)

# -----------------------------------------------------
n = [1, 1, 1]

step = 0

while len(n) < 10:
    n.append(sum(n[step:step+3]))
    step += 1

print(n)
# [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

# -----------------------------------------------------
w = "breakCamelCase"
for el in w:
    if el.upper() == el:
        w = w.replace(el, f" {el}").replace("  ", " ")
print(w)

# -----------------------------------------------------
# Rot13 шифр (каждая буква заменяется за букву, которая идет через 13 букв после), символы и числа остаются на месте как есть

def rot13(message):
    alph = "0abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    symbols = ' ^{);<|&#?:]}>-$(/\=%~ *+@_[.!'
    numbers = '0123456789'

    s = ""

    for el in message:
        if el in numbers or el in symbols:
            s += el
        elif el == alph[alph.index(el.lower())].upper():
            s += alph[alph.index(el.lower()) + 13].upper()
        else:
            s += alph[alph.index(el) + 13]

    return s









