# Напишите программу, которая на вход принимает два числа A и B,
# # и возводит число А в целую степень B с помощью рекурсии.
# # A = 3; B = 5 -> 243 (3⁵)
# # A = 2; B = 3 -> 8


def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

a = int(input('A = '))
b = int(input('B = '))
print(f"{a} в степени {b} равно {power(a,b)}")
