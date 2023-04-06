# 789991 = 700000 + 80000 + 9000 + 900 + 90 + 1
import math


def expanded_form(num):
    i = 10
    lst = []
    number = num

    while num % i != num:
        n = number % i
        number = number - n
        if n not in lst and n > 0:
            lst.append(n)
        i *= 10

    s = f'{num} = {number}'

    for el in lst[::-1]:
        s += f' + {el}'

    return s


# -----------------------------------------------
# remove all values from list a, which are present in list b keeping their order

def array_diff(a, b):
    lst_3 = []
    for el in a:
        if el not in b:
            lst_3.append(el)
    return lst_3


# -----------------------------------------------
# count all the occurring characters in a string

def count(string):
    values = []
    values = [x for x in string if x not in values]
    keys = [string.count(x) for x in values]
    d = {x[0]: x[1] for x in list(zip(values, keys))}
    return d


# -----------------------------------------------
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(string):
    lst = []
    for i in range(len(string)):
        lst_str = list(string.lower())
        if lst_str[i] != ' ':
            lst_str[i] = lst_str[i].upper()
            lst.append("".join(lst_str))
        else:
            continue
    return lst


# -----------------------------------------------

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        print(f'{year} is leap')
    else:
        print(f'{year} NOT leap')


# -----------------------------------------------

def print_text(text):
    number = int(input())
    i = 0
    while i < number:
        print(text)
        i += 1


# -----------------------------------------------


def calcul(a, b):
    operator = input()
    res = 0
    if operator == '/':
        res = a / b
    elif operator == '*':
        res = a * b
    elif operator == '-':
        res = a - b
    elif operator == '+':
        res = a + b
    print(f'{a} {operator} {b} = {res}')


# -----------------------------------------------
value = 1
'''
match value:
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print('no such value')
'''


# -----------------------------------------------
def between(a, b):
    i = a
    lst = []
    while i != b + 1:
        lst.append(i)
        i += 1
    return lst


# -----------------------------------------------

'''
family_1 = input().split()
family_2 = input().split()

if len(family_1) > len(family_2):
    print(family_1)
elif len(family_2) > len(family_1):
    print(family_2)
else:
    print('Equal')
'''


# -----------------------------------------------
def sum_dig_pow(a, b):
    res = []
    lst = list(range(a, b + 1))
    for el in lst:
        summ = 0
        k = 1
        s = str(el)
        for n in s:
            summ += int(n) ** k
            k += 1
        if summ == el:
            res.append(el)
    return res


# -----------------------------------------------
'''берем список и возвращаем второй список, 
где каждый элемент равен произведению элементов первого списка (всех, кроме элемента со своим индексом)

список 1 = [3,27,4,2]
результат = [216,24,162,324]

216 = 27 * 4 * 2
24 = 3 * 4 * 2
162 = 3 * 27 * 2
324 = 3 * 27 * 4
'''


def product_array(numbers):
    x = 0
    res = 1
    lst = []

    while len(lst) != len(numbers):
        for i in range(len(numbers)):
            if i != x:
                res *= numbers[i]
        lst.append(res)
        res = 1
        x += 1

    return lst


# -----------------------------------------------
'''
To get to the health camp, the organizers decided to order buses. 
It is known that some children kids and adults adults are going to go to the camp. 
Each bus has a certain number of seats places. 
There must be at least two adults on each bus in which children will travel.
Determine whether it will be possible to send all children and adults to the camp, 
and if so, what is the minimum number of buses required to order for this.
'''


def buses(kids, adults, places):
    if places == 0:
        return 0
    elif kids == 0:
        buses = math.ceil(adults / places)
        return buses
    else:
        people = kids + adults
        buses = math.ceil(people / places)
        adults_per_bus = adults / buses

        if adults_per_bus < 2:
            return 0
        else:
            return buses


# -----------------------------------------------
'''
A string is considered to be in title case if each word in the string is either 
(a) capitalised (that is, only the first letter of the word is in upper case) 
or 
(b) considered to be an exception and put entirely into lower case unless it is the first word, which is always 
capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). 
The list of minor words will be given as a string with each word separated by a space. 
Your function should ignore the case of the minor words string -- 
it should behave in the same way even if the case of the minor word string is changed.

https://www.codewars.com/kata/5202ef17a402dd033c000009/python
'''


def title_case(title, minor_words=''):
    title_list = title.lower().split()
    minor_list = minor_words.lower().split()
    res = []

    for i in range(len(title_list)):
        if title_list[i] in minor_list and i != 0:
            res.append(title_list[i])
        else:
            res.append(''.join([x.upper() if i == 0 else x.lower() for i, x in enumerate(title_list[i])]))

    return ' '.join(res)


# -----------------------------------------------
# https://www.codewars.com/kata/582aafca2d44a4a4560000e7/train/python

def keep_order(ary, val):
    indx = 0

    if val > ary[-1]:
        indx = len(ary)
    else:
        for i, el in enumerate(ary):
            if el > val or el == val:
                indx = i
                break
    return indx


# -----------------------------------------------
# https://www.codewars.com/kata/61c78b57ee4be50035d28d42/train/python


def merge_strings(first, second):
    s = ''
    start = 0
    stop = len(first)

    while True:
        if first[start:len(first)] == second[0:stop]:
            s += second[0:stop]
            break
        else:
            start += 1
            stop -= 1

    return first[0:start] + second


# -----------------------------------------------
# https://www.codewars.com/kata/58b972cae826b960a300003e/solutions/python


def missing(nums, s):
    sort = sorted(nums)
    str = s.lower().replace(' ', '')

    res = ''

    for i, el in enumerate(str):
        for j in sort:
            if j not in range(len(str)):
                res = "No mission today"
                break
            if i == j:
                res += el

    return res


# -----------------------------------------------
# https://www.codewars.com/kata/571d2e9eeed4a150d30011e7/python

def scoreboard(who_ate_what):
    lst = []

    for el in who_ate_what:
        scores = 0
        for k, v in el.items():
            if k == 'chickenwings':
                scores += v * 5
            elif k == 'hamburgers':
                scores += v * 3
            elif k == 'hotdogs':
                scores += v * 2
        lst.append({"name": el.get("name"), "score": scores})

    return sorted(lst, key=lambda x: (-x.get("score"), x.get("name")), reverse=True)


print(scoreboard([{"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
                  {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
