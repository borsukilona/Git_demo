import time
#алгоритм евклида
#нахождение наибольшего общего делителя (НОД)

a = 18
b = 24

# b = b - a = 24 - 18 = 6
#вычитаем из большего значения меньшее -> и результат записываем в переменную, где было большее значение

# a = 18, b = 6
# a = a - b = 18 - 6 = 12
# a = 12, b = 6
# a = a - b = 12 - 6 - 6
# a = 6, b - 6 (одинаковые числа - это и есть общий делитель)

# пока a != b, мы находим большее число и из большего вычитаем меньшее, результат пишем в большее

def get_nod (a, b):
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

    return a #пофиг что возвращать, ведь a и b будут в итоге иметь одинаковое значение


#протестируем, правильно ли работает наша функция для всех чисел
def test_nod(func): #func - это та функция, которую мы  будем тестировать
    # --- test N1 --- рандомные числа
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('test N1 OK')
    else:
        print('test N1 FAIL')

    # --- test N2 --- числа, где второе число 1, чтоб нодом всегда была 1ца
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('test N2 OK')
    else:
        print('test N2 FAIL')

    # --- test N3 --- скорость выполнения тестируемой функции

    a = 2
    b = 10000000
    st = time.time() #засекаем начальное время, при котором мы запустили функцию
    res = func(a, b) #запускаем саму функцию
    et = time.time() #сколько времени прошло с момент как функция стартанула и закончила своё выполнение (время после окончания функции)
    dt = et - st #время старта - время окончания = сколько длился процесс
    if res == 2 and dt < 1: #если нод найден правильно и время выполнения функии заняло меньше секунды, то оке
        print('test N3 OK')
    else:
        print('test N3 FAIL')


test_nod(get_nod)
# test N1 OK
# test N2 OK
# test N3 OK

res = get_nod(a, b)
print(res) #6

help(get_nod)
'''get_nod(a, b)
    Вычисляется НОД (наибольший общеий делитель)
    для двух натуральных чисел a, b по алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД'''

#-----------------------------------------------------------------
#суть БЫСТРОГО алгоримта евклида

x = 18
y = 24

#b = 24 % 18 = 6
#a = 18 % 6 = 0

#вычисляем остаток от деления большего на меньшее число = 6
#результат записываем на место большего числа
#опять проделываем тоже самое
#как только остаток от деления == 0, то меньшее число и будет являться НОД = 6

#пока меньшее число больше 0, большее чило == остаток от деления большего на меньшее

def get_nod_hurry(a, b):
    '''
    Вычисляется НОД (наибольший общий делитель)
    для двух натуральных чисел a, b по БЫСТРОМУ алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    '''
    if a < b:
        a, b = b, a #чтобы меньшее значение хранилось в 'a', а большее в 'b'
    while b != 0:
        a, b = b, a % b

    return a

test_nod(get_nod_hurry)
# test N1 OK
# test N2 OK
# test N3 OK