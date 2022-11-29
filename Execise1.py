# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка
# с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

size = int(input('Введите размер списка: '))
my_list = []
for i in range(size):
    my_list.append(random.randint(0, 10))
print(f'Имеется список: {my_list}')

sumElWithOddIndexes = 0
for i in range(1, size, 2):
    sumElWithOddIndexes += my_list[i]
print(f'Сумма элементов списка с нечетными индексами равна {sumElWithOddIndexes}')

