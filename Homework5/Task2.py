"""Завдання 2.
Користувач вводить довжини катетів прямокутного трикутника. Написати функцію, яка обчислить площу
та периметр цього трикутника. Функція має повертати пару значень.
"""

import math


def triangle_square_and_perimeter(a, b):
    plosha = 0.5*(a*b)
    perim = (math.sqrt((a**2) + (b**2))) + a + b
    return plosha, perim


x = int(input("Enter katet 1(a): "))
y = int(input("Enter katet 2(b): "))

final = triangle_square_and_perimeter(x, y)

print("Plosha: ", int(final[0]), "\nPerimeter: ", int(final[1]))

