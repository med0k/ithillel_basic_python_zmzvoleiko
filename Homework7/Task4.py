"""
Написати функцію, що розраховує суму Unicode кодів усіх символів, що знаходяться між двома заданими символами включно.
Наприклад, в функцію передаються символи 'a' та 'd', отже треба порахувати суму кодів символів 'a', 'b', 'c' та 'd',
а це 97+98+99+100=394.
"""


def sum_symbol_codes(first, last):  # returns int
    sumik = 0
    for i in range(ord(first), ord(last)+1):
        sumik += i
    return sumik


def main():
    tik = 'a'
    tok = 'd'

    print(sum_symbol_codes(tik, tok))


if __name__ == '__main__':
    main()
