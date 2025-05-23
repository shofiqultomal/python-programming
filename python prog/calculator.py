a = int(input('ENTER THE NUMBAR: '))
b = int(input('ENTER THE NUMBAR: '))
c = input('ENTER THE OPRETOR: ')



def add(a, b):
    print('addation of the given numbar is : ', a+b)


def sub(a, b):
    print('subtration of the given numbar is : ', a-b)


def mul(a, b):
    print('multipulation of the given numbar is : ', a*b)


def div(a, b):
    print('division of the given numbar is : ', a/b)


if (c == "+"):
    add(a, b)
if (c == "-"):
    sub(a, b)
if (c == "*"):
    mul(a, b)
if (c == "/"):
    div(a, b)
