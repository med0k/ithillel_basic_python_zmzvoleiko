"""
У математиці функцію `sign(x)` (знак числа) визначено так:
sign(x) = 1, якщо x > 0,
sign(x) = -1, якщо x < 0,
sign(x) = 0 якщо x = 0.
"""

def sign(x):
    if x > 0:
        print("Result is 1")
        return 1
    elif x < 0:
        print("Result is -1")
        return -1
    else:
        print("Result is 0")
        return 0


def test():
    assert sign(50) > 0


def main():
    entered_value = int(input("Please enter your digit: "))

    print(sign(entered_value))


if __name__ == '__main__':
    main()
    # test()
