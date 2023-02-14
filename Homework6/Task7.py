"""
Створити рекурсивну функцію, що приймає натуральне число і повертає число з послідовності Фібоначі,
 позиція якого відповідає введеному числу.
Кожне наступне число послідовности Фібоначі -- це сума двох попередніх чисел. Тобто:
0 1 1 2 3 5 8 13 21 34 55 89 і т.д.
Отже, якщо в функцію передадуть число 5, то вона має повернути 5те число з послідовности, тобто 3.
 Якщо введуть 10, то має повернути 10те число, тобто 34.
Розрахувати за допомогою цієї функції та вивести на екран 20те число з послідовності Фібоначі.
Примітка: на ваш вибір прийняти, з яких чисел починається послідовність: або з 0 та 1, або з 1 та 1.
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def test():
    assert fibonacci(5) == 5


def main():
    prev_fibonacci = fibonacci(5 - 1)

    print(prev_fibonacci)


if __name__ == '__main__':
    main()
    # test()
