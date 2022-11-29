# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

import random

size = int(input('Введите размер списка: '))
my_list = []
for i in range(size):
    my_list.append(random.randint(0, 10))
print(f'Имеется список: {my_list}')

my_listOftwoNumProduct = []

if size % 2 == 0:
    my_listOftwoNumProductLength = size // 2
    for i in range(my_listOftwoNumProductLength):
        my_listOftwoNumProduct.append(my_list[i] * my_list[size - 1 - i])
    print(f'Произведение пар чисел списка равно {my_listOftwoNumProduct}')

else:
    my_listOftwoNumProductPreLength = (size // 2)
    centreElemInMy_listOftwoNumProductLength = my_list[my_listOftwoNumProductPreLength]
    lastElemInMy_listOftwoNumProductLength = (centreElemInMy_listOftwoNumProductLength *
                                              centreElemInMy_listOftwoNumProductLength)
    my_listOftwoNumProductLength = (size // 2)
    for i in range(my_listOftwoNumProductLength):
        my_listOftwoNumProduct.append(my_list[i] * my_list[size - 1 - i])
    my_listOftwoNumProduct.append(lastElemInMy_listOftwoNumProductLength)
    print(f'Произведение пар чисел списка равно {my_listOftwoNumProduct}')