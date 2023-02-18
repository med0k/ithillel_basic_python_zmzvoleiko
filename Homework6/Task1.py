"""
Написати функцію, що визначає чи введене число є парним:
"""


def is_even(number):  # returns boolean value
    return number % 2 == 0


def test():
    assert is_even(3) is False
    assert is_even(4) is True


def main():
    entered_value = int(input("Введіть ваше число: "))

    result = is_even(entered_value)

    if result is True:
        print("Your number is PARNE")

    else:
        print("Result is NE PARNE")


if __name__ == '__main__':
    main()
    # test()
