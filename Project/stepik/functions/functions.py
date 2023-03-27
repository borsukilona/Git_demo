def addition_numbers(a, b):
    print(a + b)


# Alt + Ctrl + L (форматирование, между функцией и её вызовом желательно иметь две строки отступа)
addition_numbers(2, 4)  # 6


# ------------------------------------------------------------------------------------------------------

def send_mail(from_name):
    text = f'Dear {from_name}, I love you'
    print(text)


send_mail('Ilona Borsuk')  # Dear Ilona Borsuk, I love you


# ------------------------------------------------------------------------------------------------------

def get_sqrt(x):
    res = None if x < 0 else x ** 0.5  # умножение на 0.5 это и есть квадратный корень
    return int(res)


a = get_sqrt(49)
print(a)  # 7


# ------------------------------------------------------------------------------------------------------

def get_sqrt_two_arg_return(x):
    res = None if x < 0 else x ** 0.5  # умножение на 0.5 это и есть квадратный корень
    return x, int(res) #будет возвращаться кортеж данных


a, b = get_sqrt_two_arg_return(49)
print(a, b)  # 49 7

# ------------------------------------------------------------------------------------------------------

def get_max_value_from_two(a, b):
    return a if a > b else b


c = get_max_value_from_two(5, 2)

print(c) #5

# ------------------------------------------------------------------------------------------------------
x, y, z = 5, 10, 7

def get_max_value_from_three(a, b, c):
    m = 0
    if a > b:
        if a > c:
            m = a
    elif b > c:
        m = b
    else:
        m = c
    return m

print(get_max_value_from_three(x ,y , z)) #10

#тожe самое (определить максимально из трех чисел), только по-другому

print(get_max_value_from_two(x, get_max_value_from_two(y, z))) #10

#или

def get_max_three(a, b, c):
    return get_max_value_from_two(a, get_max_value_from_two(b, c))


print(get_max_three(x, y, z)) #10

# ------------------------------------------------------------------------------------------------------

#PERIMETR = True
#if PERIMETR:
    #get_rect = 1
#else:
    #get_rect = 2

#print(get_rect) #1

#если PERIMETR = True, то возвращаем периметр, если False, то площадь

PERIMETR = False
if PERIMETR:
    def get_rect (a, b):
        return 2 * (a + b)
else:
    def get_rect(a, b):
        return a * b


print(get_rect(2, 4)) #12 - если True; 8 - если False

# ------------------------------------------------------------------------------------------------------
#четное число или нечетное
def even(x):
    return x % 2 == 0 #если четное - вернет True, а есть нечетное - вернет False


for i in range(1, 10):
    if even(i): #if even(i) == True
        print(i)
# 2
# 4
# 6
# 8

# ------------------------------------------------------------------------------------------------------



