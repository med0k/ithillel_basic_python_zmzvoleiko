"""
При виконанні завданнь уважно вичитуйте умови та вимоги задачі. Також за замовчуванням введення та виведення
(тобто input/print) не мають використовуватися в тілі функцій, що треба створити в рамках завдань.
Тобто, послідовність програми така:
1. Оголошення фукнції для рішення задачі
2. Ввід даних від користувача
3. Виклик оголошеної функції з введеними данним
4. Вивід результату функції. Не забувайте за оформлення коду, а також гарне оформлення вводу та виводу для користувача.

Завдання 1.
Написати функцію, яка буде переводити градуси в радіани (без використання math.radians).
 Використовуючи цю функцію, вивести на екран значення косинусів кутів 60, 45 та 40 градусів.
"""

from math import cos, pi


def degrees2radians(degrees):
    radians = (degrees*pi) / 180
    return radians


valu = int(input('Please enter degrees: \n'))

cosi = cos(degrees2radians(valu))

print("Value of cosinuses by entered your degrees: ", round(cosi, 2))



