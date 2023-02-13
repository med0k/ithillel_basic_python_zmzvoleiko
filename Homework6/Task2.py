"""
Написати функцію для рішення квадратних рівнянь.
"""

import math


def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        # a = 1, b = −8, c = 12;
        # D = 16
        x1 = round((-b + math.sqrt(discriminant)) / 2 * a)
        x2 = round((-b - math.sqrt(discriminant)) / 2 * a)
        return x1, x2

    elif discriminant == 0:
        # a = 1; b = −6; c = 9 D = 0
        x3 = (-b + math.sqrt(discriminant)) / 2 * a
        return x3

    else:
        # a = 5; b = 3; c = 7; D = -131
        print("When discriminant = 0, do not have roots, and it's ")


def main():
    enter_first = int(input("Please enter a: "))
    enter_second = int(input("Please enter b: "))
    enter_third = int(input("Please enter c: "))

    result = solve_quadratic_equation(enter_first, enter_second, enter_third)

    print(result)


if __name__ == '__main__':
    main()
