def recursive(value):
    print(value)
    if value < 4:  # функция может выпоонять себя не бесконечно, поэтому кол-во рекурсий надо ограничивать
        recursive(value + 1)


#recursive(1)


# 1
# 2
# 3
# 4

# ------------------------------------------------------------------------------------------------------------
def recursive(value):
    print(value)
    if value < 4:  # функция может выпоонять себя не бесконечно, поэтому кол-во рекурсий надо ограничивать
        recursive(value + 1)
    print(value)


#recursive(1)
# 1
# 2
# 3
# 4
# 4
# 3
# 2
# 1

# сначала выполняется сверху вниз, потом снизу вверх

# ------------------------------------------------------------------------------------------------------------
#вычисление факториала натурального числа
#n! = 1*2*3*...*n

def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n-1)


#print(fact(3)) #6
# n * fact(n-1)
# n-1 * fact(n-2)
# 1 * fact(0) = 1

#n * (n-1) * (n-2)
# 3 * 2 *1

# ------------------------------------------------------------------------------------------------------------
#выведем в консоль структуру файловой системы (с отступами)
#идем по клбчам словаря, пока не дойдем до списка

F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):
    '''
    :param path: сам словарь F
    :param depth: глубина обхода по словарю, которая изначально равно 0
    :return:
    '''

    for f in path: #перебираем словарь по ключам
        print(" "*depth, f) #выводим ключи словаря, с учетом глубины (будут отступы)
        if type(path[f]) == dict: #является ли значение словаря тоже словарем
            get_files(path[f], depth+1) #если является, то рекурсия
        else:
            print(" "*(depth+1), " ".join(path[f]))


#get_files(F)

'''
 C:
  Python39
   python.exe python.ini
  Program Files
   Java
    README.txt Welcome.html java.exe
   MATLAB
    matlab.bat matlab.exe mcc.bat
  Windows
   System32
    acledit.dll aclui.dll zipfldr.dll
'''

# ------------------------------------------------------------------------------------------------------------
