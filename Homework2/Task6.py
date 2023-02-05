# Напишіть програму, що запитує довільне число у користувача і виводить його тангенс.
# Розрахувати тангенс за допомогою тільки math.cos
# (не можна використовувати вбудовані функції для розрахунку сінусу чи тангенсу -- потрібно втілити відповідні формули).

import math

new_value = input('Enter your value: ')

if new_value.isdigit() == True:
    new_value = int(new_value)
    cos = math.cos(new_value)

    tg = ((1 - (cos ** 2)) ** 0.5) / cos

    print("The tangens of your entered number is: ", tg)
else:
    print("You have entered a string. Please enter a digit")