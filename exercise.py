def get_age():
    age = int(input("enter your age"))
    if age < 0:
        raise BaseException("oh no, age can not be negative")


def get_number():
    result = int(input("enter number: "))
    return result


def addition(first, second):
    result = first - second
    return result


def d():
    c()


def c():
    b()


def b():
    a()


def a():
    first = get_number()
    second = get_number()
    addition(first, second)
    return addition(first, second)