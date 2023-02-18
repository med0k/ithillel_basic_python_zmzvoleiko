"""
Програма випадковим чином обирає число від 1 до 10 і пропонує користувачу його вгадати. Користувач вводить число,
а програма перевіряє його і, якщо користувач не вгадав, то програма повідомляє, що введене число більше
або менше від згенерованого. Після цього знову просить вгадати. І так, поки користувач не вгадає.
Щоб згенерувати випрадкове число, скористайтеся функцією randint з модулю random.
"""


from random import randint

random_value = randint(1, 10)

tire = "-------------------------------------------------------------------------"
print(f"{tire}\nLet's play this hellish game! You have to guess the number I came up with\n{tire}")

while True:
    entered_value = int(input("Please enter any your digit from 1 to 10: "))

    if entered_value == random_value:
        print("Congratulations, You're winner. Your entered value is equal to random.", "Random value was: ",
              random_value)

    elif entered_value > random_value:
        print("What are hell is going on buddy? Your number is too big.", "Random value was: ", random_value)

    else:
        print("Holy cow, this number is too small than what I thought.", "Random value was: ", random_value)

    break
