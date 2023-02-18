"""
У математиці функцію `sign(x)` (знак числа) визначено так:
sign(x) = 1, якщо x > 0,
sign(x) = -1, якщо x < 0,
sign(x) = 0 якщо x = 0.
"""

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def test():
    assert sign(50) > 0


def main():
    entered_value = int(input("Please enter your digit: "))

    result = sign(entered_value)

    if result == 1:
        print("This value equal -> 1")

    elif result == -1:
        print("This value equal -> -1")

    else:
        print("This value equal -> 0")


if __name__ == '__main__':
    main()
    # test()
