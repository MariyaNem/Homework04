# Задача 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

input_list_one = []
list_len = int(input("Количество элементов первого набора: "))
for _ in range(list_len):
    input_list_one.append(int(input("Введите число: ")))

input_list_two = []
list_len = int(input("Количество элементов второго набора: "))
for _ in range(list_len):
    input_list_two.append(int(input("Введите число: ")))

list_one = set(input_list_one)
list_two = set(input_list_two)
print(list_one)
print(list_two)

new_sorted_list = list_one.intersection(list_two)
print(new_sorted_list)