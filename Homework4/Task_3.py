"""Завдання 3.
Напишіть програму, яка зчитує ціле число та виводить текст, аналогічний наведеному у прикладі (пробіли та переведення
 на новий рядок важливі!). Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:"""

x = int(input("Please enter an integer number: "))

if isinstance(x, int):
    print('Next number for number ', x, ' is ', x+1, '.\n', 'Previous number for number ', x, ' is ', x-1, '.', sep='')
else:
    print("Please enter a full digit")