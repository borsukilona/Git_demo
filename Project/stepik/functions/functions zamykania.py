def say_name(name):
    def say_goodbye():
        print("don't say me goodbye, " + name + "!")

    say_goodbye()


say_name("Ilona") #don't say me goodbye, Ilona!

# ---------------------------------------------------------------

def say_name(name):
    def say_goodbye():
        print("don't say me goodbye, " + name + "!")

    return say_goodbye


f = say_name("Ilona")
f2 = say_name("Python")
f() #don't say me goodbye, Ilona!
f2() #don't say me goodbye, Python!

# ---------------------------------------------------------------
# счетчик, который при каждом новом запуске бцдет увеличивать свое значение на единицу


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = counter(10) #start с 10
c2 = counter() #start с нуля

print(c1(), c2()) #11 1
print(c1(), c2()) #12 2
print(c1(), c2()) #13 3


# ---------------------------------------------------------------
# удаляем ненужные символы вначале и в конце строки

def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars) #удаляем определенные нами пробелы по умолчанию вначае и в конце заданной строки при помощи встроенной уже функции strip()

    return do_strip


strip1 = strip_string() #будет удалять пробелы по умолчанию
strip2 = strip_string(" !?,.;") #будет удалять все указанные нами символы

print(strip1(" hello python!.. ")) #hello python!..
print(strip2(" hello python!.. ")) #hello python

typ = input()
numbers = input()

