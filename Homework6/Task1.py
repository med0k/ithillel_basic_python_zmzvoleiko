"""
Написати функцію, що визначає чи введене число є парним:
"""


def is_even(number):  # returns boolean value
    if number % 2 == 0:
        return number % 2
    else:
        return None


def test():
    result1 = is_even(3)
    result2 = is_even(4)
    assert result1 is False
    assert result2 is True


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
