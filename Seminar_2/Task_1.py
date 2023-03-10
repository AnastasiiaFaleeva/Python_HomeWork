# Задача №1:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество
# монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
from itertools import count

n = int(input('Введите количество монеток '))
count_orel_1 = 0
count_reshka_0 = 0
for i in range(n):
    coin = int(input('Введите цифру 1 - решка или 0 - герб '))
    if coin == 1:
        count_orel_1 += 1
    else:
        count_reshka_0 += 1
if count_orel_1 <= count_reshka_0:
    print(f'Минимальное количество монет, которые нужно перевернуть - {count_orel_1}')
else:
    print(f'Минимальное количество монет, которые нужно перевернуть - {count_reshka_0}')