N = 100


def my_func(lst):
    global N  # чтобы работать в глобальной переменной N = 100, нам надо сказать функции, что именно эту переменную N мы берем для работы
    N = 20
    for i in lst:
        n = i + 1 + N
        print(n)


# my_func([1, 2, 3])

# ---------------------------------------------------------------
x = 0


def outer():
    x = 1

    def inner():
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)


#outer()
#print("global: ", x)
# inner:  2
# outer:  1
# global:  0

# ---------------------------------------------------------------
x = 0


def outer():
    x = 1

    def inner():
        nonlocal x #используем x из внешей функции outer и меняем этот x на 2
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)


#outer()
#print("global: ", x)
# inner:  2
# outer:  2
# global:  0

# ---------------------------------------------------------------
x = 0


def outer():
    global x
    x = 1

    def inner():
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)

outer()
print("global: ", x)
# inner:  2
# outer:  1
# global:  1