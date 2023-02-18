# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > 0 and b > 0:
        return sum(a-1, b+1)
    else:
        return sum(a+1, b-1)

a = int(input('A = '))
b = int(input('B = '))
print(f"{a} + {b} = {sum(a,b)}")