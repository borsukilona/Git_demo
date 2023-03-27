from functools import reduce


def sum_args(*args):
    result = reduce(lambda x, y: x + y, args)
    return result


def multiple_args(*args):
    result = reduce(lambda x, y: x * y, args)
    return result


def minus_args(*args):
    result = reduce(lambda x, y: x - y, args)
    return result


def divide_args(*args):
    result = reduce(lambda x, y: x / y, args)
    return result

