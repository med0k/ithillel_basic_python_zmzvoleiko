"""
Написати функцію, що визначає чи введене число є парним:
"""


def is_even(number):  # returns boolean value
    if (number % 2) == 0:
        print("Your digit is parne")
        return True
    else:
        print("Your digit is Neparne")
        return False

def test():
    result1 = is_even(3)
    result2 = is_even(4)
    assert result1 is False
    assert result2 is True


def main():
    entered_value = int(input("Введіть ваше число і дізнаємося чи є ваше число парним: "))
    is_even(entered_value)


if __name__ == '__main__':
    main()
    # test()
