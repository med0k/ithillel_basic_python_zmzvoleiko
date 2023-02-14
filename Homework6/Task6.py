"""
У математиці функцію `sign(x)` (знак числа) визначено так:
sign(x) = 1, якщо x > 0,
sign(x) = -1, якщо x < 0,
sign(x) = 0 якщо x = 0.
"""

def sign(x):
    if x > 0:
        fin = 1
        print(fin)
    elif x < 0:
        fin = -1
        print(fin)
    else:
        fin = 0
        print(fin)


def test():
    assert sign(50) is None


def main():
    entered_value = int(input("Please enter your digit: "))

    print(sign(entered_value))


if __name__ == '__main__':
    main()
    # test()
