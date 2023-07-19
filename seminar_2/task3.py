# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

n = int(input("Введите число N: "))

count = 0
res = 2 ** count

while res <= n:
    print(res, end=" ")
    count += 1
    res = 2 ** count
