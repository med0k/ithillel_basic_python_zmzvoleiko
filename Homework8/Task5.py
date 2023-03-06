"""
Написати функцію, що повертає найбільшу цифру випадкового 12-ти-значного натурального числа а) з використанням рядків
б) без використання рядків.
Число для тестування можна отримати або від користувача, або згенерувати за допомогою функції randint з модулю random.
def get_max_digit(number): # returns int
    pass
"""

import random


def max_digit_with_strings(my_number):
    str_number = str(my_number)
    max_digit = max(str_number)
    return int(max_digit)


def max_digit_without_strings(my_number):
    max_digit = 0
    while my_number > 0:
        digit = my_number % 10
        if digit > max_digit:
            max_digit = digit
        my_number //= 10
    return max_digit


def main():
    my_number = random.randint(10**11, 10**12 - 1)
    print(f'Random value is: {my_number}')
    print(f"Biggest number with string uses: {max_digit_with_strings(my_number)}")
    print(f"Biggest number withOUT string uses: {max_digit_without_strings(my_number)}")


if __name__ == "__main__":
    main()
