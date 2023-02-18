# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите количество элементов 1-го множества: "))
m = int(input("Введите количество элементов 2-го множества: "))

first_set = set()
for i in range(n):
    x = int(input("Введите элемент 1-го множества: "))
    first_set.add(x)

second_set = set()
for i in range(m):
    x = int(input("Введите элемент 2-го множества: "))
    second_set.add(x)

result = first_set.intersection(second_set)
result = sorted(list(result))

print(first_set, ' ', second_set, '--->>>', result)