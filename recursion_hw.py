def print_stars(n):
    print('*', end='')
    if n == 1:
        return
    print_stars(n - 1)


def count_char(c, word):
    if not len(word):
        return 0
    return (1 if word[0] == c else 0) + count_char(c, word[1:])


def print_digits_forward(num):
    if num < 10:
        print(num, end=' ')
    else:
        print_digits_forward(num // 10)
        print(num % 10, end=' ')


def count_odd_digits(n):
    if n == 0:
        return 0
    return ((n % 10) % 2) + count_odd_digits(n // 10)


def reverse_print(word):
    if not word:
        return
    reverse_print(word[1:])
    print(word[0],end='')


print_stars(5)
print()
print(count_char("a", "banana"))
print_digits_forward(567)
print()
reverse_print('hello')
print()
