"""
Завдання 4.
Написати функцію, що відповідає на питання, чи перетинають два заданих кола на площині.
Кожне коло задається координатами центра та радіусом.
"""

import math


def circles_intersect(x1, y1, r1, x2, y2, r2):  # returns boolean value
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if d < r1 - r2:
        return d < r1 - r2
    elif d < r2 - r1:
        return d < r2 - r1
    elif d > r1 + r2:
        return d > r1 + r2
    else:
        return None


def main():
    r1 = int(input("Enter radius1: "))
    x1 = int(input("Please enter coordinate x1: "))
    y1 = int(input("Please enter coordinate y1: "))
    r2 = int(input("Enter radius2: "))
    x2 = int(input("Please enter coordinate x2: "))
    y2 = int(input("Please enter coordinate y2: "))

    result = circles_intersect(x1, y1, r1, x2, y2, r2)
    print(result)


if __name__ == '__main__':
    main()
