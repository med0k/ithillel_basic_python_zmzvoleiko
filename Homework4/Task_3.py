"""Завдання 3.
Напишіть програму, яка зчитує ціле число та виводить текст, аналогічний наведеному у прикладі (пробіли та переведення
 на новий рядок важливі!). Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:"""


def check_user_input(input):
    try:
        val = int(input)
        print('Next number for number ', val, ' is ', val + 1, '.\n', 'Previous number for number ', val, ' is ', val - 1, '.',
              sep='')
    except ValueError:
        try:
            val = float(input)
            print("Input is a float  number. Try enter an Integer value")
        except ValueError:
            print("No.. input is not a number. It's a string")

input1 = input("Please enter an integer number: ")
check_user_input(input1)