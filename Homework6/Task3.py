"""
Завдання 3.
Виконати попереднє завдання, але функція має враховувати рішення квадратного рівняння в комплексній площині.
Тобто з використанням комплексних чисел, квадратне рівняння завжди матиме рішення.
"""
import math


def solve_quadratic_complex(a, b, c):
    dd = b ** 2 - 4 * a * c
    square_D = (dd * -1) ** 0.5
    x1 = (-b + square_D) / (2 * a)
    x2 = (-b - square_D) / (2 * a)

    return x1, x2


def main():
    enter_first = int(input("Please enter a: "))
    enter_second = int(input("Please enter b: "))
    enter_third = int(input("Please enter c: "))

    result = solve_quadratic_complex(enter_first, enter_second, enter_third)

    print(result)


if __name__ == '__main__':
    main()
