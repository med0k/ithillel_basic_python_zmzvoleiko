"""
Написати функцію, що визначає чи введене число є парним:
"""


def is_even(number):  # returns boolean value
    if (number % 2) == 0:
        print(bool(True))
    else:
        print(bool(False))


def test():
    result = is_even(2)
    print("Result", result)
    assert result == (result % 2)


def main():
    entered_value = int(input("Введіть ваше число і дізнаємося чи є ваше число парним: "))
    is_even(entered_value)


if __name__ == '__main__':
    # main()
    test()
