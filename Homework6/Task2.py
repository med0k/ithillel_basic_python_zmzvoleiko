"""
Написати функцію для рішення квадратних рівнянь.
"""

import math


def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = round((-b + math.sqrt(discriminant)) / 2 * a)
        x2 = round((-b - math.sqrt(discriminant)) / 2 * a)
        return x1, x2

    elif discriminant == 0:
        x3 = (-b + math.sqrt(discriminant)) / 2 * a
        return x3

    else:
        print("When discriminant = 0, do not have roots")


def main():
    enter_first = int(input("Please enter a: "))
    enter_second = int(input("Please enter b: "))
    enter_third = int(input("Please enter c: "))

    result = solve_quadratic_equation(enter_first, enter_second, enter_third)

    print(result)


if __name__ == '__main__':
    main()
