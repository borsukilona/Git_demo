#функция-генератор

def get_list():
    for x in [1, 2, 3, 4]:
        # return x вернет 1
        yield x # вернет генератор


a = get_list()
'''
print(next(a)) # 1
print(next(a)) # 2
print(next(a)) # 3
print(next(a)) # 4
'''

for x in a:
    print(x)
# 1
# 2
# 3
# 4

# -------------------------------------------------------------
# вычисляем среднее арифметическое для последовательностей чисел
'''
1, 2, 3, 4, 5, 6, 7, 8, 9, 10 = 5.5
2, 3, 4, 5, 6, 7, 8, 9, 10 = 6.0
3, 4, 5, 6, 7, 8, 9, 10 = 6.5
4, 5, 6, 7, 8, 9, 10 = 7.0
5, 6, 7, 8, 9, 10 = 7.5
6, 7, 8, 9, 10 = 8.0
7, 8, 9, 10 = 8.5
8, 9, 10 = 9.0
9, 10 = 9.5
'''

def gen():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a)/len(a)


a = gen()
print(list(a))
# [5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5]

# -------------------------------------------------------------
# найти индексы всех слов 'в' из файла


def find_word(f, word):
    g_indx = 0 # смещение индекса в соответствии со строкой
    for line in f: # читаем файл построчно
        indx = 0 # индекс вхождения слова в строку
        while(indx != -1):
            indx = line.find(word, indx) # начиная с indx ищем word; возвращает -1, если слово в строке не найдено
            if indx > -1: # если словой найдено
                yield g_indx + indx
                indx += 1
        g_indx += len(line)


try:
    with open("lesson.txt", encoding='utf-8') as file:
        a = find_word(file, "в")
        print(list(a))
except FileNotFoundError:
    print("file not found")
except:
    print("error occurs when working with the file")

