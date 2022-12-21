# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# Ni = N(i-1) + N(i-2)

from os import system


def console_clear():
    system('cls')


def get_fib(n: int):    # возвращает список с последовательностью Фибоначчи
    fib = list()
    for i in range(n + 1):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i - 2] + fib[i - 1])
    return fib


def get_neg_fib(fibonacci: list):   # возвращает отрицательную последовательность Фибоначчи
                                    # в виде списка
    neg_fib = list()
    m = 0
    neg_fib.append(fib[m])
    for i in range(1, len(fib)):
        n = m = fib[i]
        if i % 2 == 0:
            m = -m
        neg_fib.insert(0, m)
        neg_fib.append(n)
    return neg_fib

console_clear()
print('Программа составляет список чисел Фибоначчи, в том числе для отрицательных индексов.')
n = int(input('Введите индекс последовательности: '))
fib = get_fib(n)
print(get_neg_fib(fib))
