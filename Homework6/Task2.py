"""
Написати функцію для рішення квадратних рівнянь.
"""

import math


def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    my_sqrt = math.sqrt(abs(discriminant))
    if discriminant > 0:
        x1 = (-b + my_sqrt) / (2 * a)
        x2 = (-b - my_sqrt3) / (2 * a)
        return x1, x2

    elif discriminant == 0:
        x3 = -b / (2 * a)
        return x3, None

    else:
        return None, None


def main():
    enter_first = int(input("Please enter a: "))
    enter_second = int(input("Please enter b: "))
    enter_third = int(input("Please enter c: "))

    result = solve_quadratic_equation(enter_first, enter_second, enter_third)

    print(result)


if __name__ == '__main__':
    main()
