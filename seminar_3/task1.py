# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

list_1 = [randint(0, 99) for _ in range(n)]
list_2 = [randint(0, 99) for _ in range(m)]

list_res = []

for i in list_1:
    if i in list_2 and i not in list_res:
        list_res.append(i)

list_res = sorted(list_res)
print(list_1)
print(list_2)
if len(list_res) == 0:
    print("В наборах нет повторяющихся чисел.")
else:
    print(*list_res)
    