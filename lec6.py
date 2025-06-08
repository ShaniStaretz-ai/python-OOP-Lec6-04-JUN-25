# implement for loop with Recursion:
from operator import truediv


def loop(n):
    if n == 0:
        return
    loop(n - 1)
    print(n, end=' ')


def loop_2(n):
    print(n, end=' ')
    if n == 10:
        return
    loop_2(n + 1)


def loop_desc(n):
    print(n, end=" ")
    if n == 1:
        return
    loop_desc(n - 1)


def add_recursion(x, y) -> int:
    # return x+y:
    if y == 0:
        return x
    return add_recursion(x + 1, y - 1)


def add_recursion2(x, y) -> int:
    # return x+y:
    if y == 0:
        return x
    return 1 + add_recursion2(x, y - 1)


def sum_digits(x):
    if x < 10:
        return x
    return x % 10 + sum_digits(x // 10)

def contain_char(char,line):
    if not len(line):
        return False
    if line[0]==char:#always check the first char in the string
        return True
    return contain_char(char,line[1:])

loop(10)
print()
loop_2(1)
print()
loop_desc(10)
print()
print(add_recursion(4, 3))
print(add_recursion2(4, 3))
print(sum_digits(1111))
print(sum_digits(9987))
print(contain_char("a","shani"))
