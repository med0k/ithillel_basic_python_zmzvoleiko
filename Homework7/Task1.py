"""
При створенні програм до усіх завдань я враховуватиму аккуратність виконання, правильна форматування,
зрозумілість виводу для користувача програми, а також слідування кращим практикам,
про які говорилося на цій та попередніх лекціях, там, де це доречно.
Завдання 1.
Шаховий кінь ходить буквою "Г" - на дві клітинки по вертикалі в будь-якому напрямку і на одну клітинку по горизонталі,
чи навпаки. Дані дві різні клітини шахівниці, визначте, чи може кінь потрапити з першої клітини на другу одним ходом.
Клітина шахівниці задається одним рядком, що складається з символу a-h та цифри 1-8: a2, e2, e4, h7, d1, і т.і.
"""


def chess(letters_start, digit_start, letters_finish, digit_finish):
    move_letters = abs(letters_start - letters_finish)
    move_digit = abs(digit_start - digit_finish)
    return move_letters == 1 and move_digit == 2 or move_letters == 1 and move_digit == 1


def main():
    letters_start = ord(input('Enter point from a-h, where you will start: '))
    digit_start = int(input('Enter letter from 1-8, where you will start: '))
    letters_finish = ord(input('Enter point from a-h: where yo wanna go: '))
    digit_finish = int(input('Enter point from 1-8: where yo wanna go: '))

    result = chess(letters_start, digit_start, letters_finish, digit_finish)

    if result is True:
        print("You can move here")
    else:
        print("You can't move here, read the rules and try again")


if __name__ == '__main__':
    main()
