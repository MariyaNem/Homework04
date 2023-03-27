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


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

berries = []
bush = int(input("Введите количество кустов: "))
for i in range(bush):
    berries.append(int(input('Количество ягод на кусте: ')))

max_berries = 0
for i in range(bush):
    berries = bush[i] + bush[i-1] + bush[i+1]
    if max_berries < berries:
        max_berries = berries
print(max_berries)