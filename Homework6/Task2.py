"""
Написати функцію для рішення квадратних рівнянь.
"""

import math


def solve_quadratic_equation(a, b, c):
    # always returns 2(!) values: either 2 roots, 1 root and None or 2 Nones
    x1 = - b + math.sqrt(b ** 2 - 4 * a * c) / 2 * a
    x2 = - b - math.sqrt(b ** 2 - 4 * a * c) / 2 * a
    return x1, x2


enter_first = int(input("Please enter a: "))
enter_second = int(input("Please enter b: "))
enter_third = int(input("Please enter c: "))

result = solve_quadratic_equation(enter_first, enter_second, enter_third)

print(result)

