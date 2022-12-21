# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from os import system
import random as rnd

def console_clear():
    system('cls')


def random_list(list_length: int, begin_num: int, end_num: int):
    return [rnd.randint(begin_num, end_num) for _ in range(list_length)]


def sum_pairs1(elements: list):  # первый способ (через границы)
    left_i = 0
    right_i = len(my_list) - 1
    result = list()
    while left_i <= right_i:
        result.append(my_list[left_i] * my_list[right_i])
        left_i += 1
        right_i -= 1
    return (result)


def sum_pairs2(elements: list):  # второй способ (через метод pop())
    my_list = list.copy(elements)
    result = list()
    while len(my_list) > 1:
        result.append(my_list.pop() * my_list.pop(0))
    if len(my_list) > 0:
        result.append(my_list.pop()**2)
    return result

console_clear()
print('Программа находит произведение пар чисел списка.')
print('Парой считаем первый и последний элемент, второй и предпоследний')
n = int(input('Введите длину списка: '))
my_list = random_list(n, 1, 10)
print('Метод 1:')
print(f'{my_list} => {sum_pairs1(my_list)}')
print('Метод 2:')
print(f'{my_list} => {sum_pairs2(my_list)}')
