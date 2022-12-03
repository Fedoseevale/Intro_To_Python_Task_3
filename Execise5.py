# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
# (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите целое число: '))
my_list = [0, 1]
for i in range(0, number-1):
    my_list.append(my_list[i] + my_list[i+1])

my_list2 = [0, 1]
for i in range(0, number-1):
    my_list2.append(my_list2[i] - my_list2[i+1])

my_list2.remove(my_list2[0])

my_list2.reverse()

my_list3 = (my_list2 + my_list)
print(f'Список чисел Фибоначчи (в т.ч. Негафибоначчи) выглядит следующим образом: {my_list3}')
