import random


def get_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Неправильне введення. Спробуйте ще раз.")


def get_str(prompt):
    while True:
        string = input(prompt)
        if string.lower() in ['yes', 'y']:
            return True
        elif string.lower() in ['no', 'n']:
            return False
        else:
            print("Неправильне введення. Спробуйте ще раз.")


def guess_user():
    print("Вгадайте число від 1 до 100.")
    secret_number = random.randint(1, 100)
    while True:
        guess = get_integer("Введіть свій варіант: ")
        if guess == secret_number:
            print("Вітаємо! Ви вгадали число!")
            break
        elif guess < secret_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")
    print()


def guess_computer():
    print("Загадайте число від 1 до 100, а я спробую його вгадати.")
    min_num = 1
    max_num = 100
    while True:
        guess = (min_num + max_num) // 2
        response = get_str(f"Чи правильне це число: {guess}? (y/n): ")
        if response:
            print("Ура! Я вгадав число!")
            break
        else:
            response = get_str(f"Чи число більше {guess}? (y/n): ")
            if response:
                min_num = guess + 1
            else:
                max_num = guess - 1
    print()


def main():
    print("Вітаю! Це програма для гри в відгадування числа.")
    while True:
        print("Виберіть гру:\n1. Я відгадаю число, яке ви загадаєте.\n2. Ви відгадуєте число, яке я загадаю.")
        game_choice = get_integer("Ваш вибір: ")
        if game_choice == 1:
            guess_computer()
        elif game_choice == 2:
            guess_user()
        else:
            print("Неправильне введення. Спробуйте ще раз.")
        play_again = get_str("Хочете зіграти ще раз? (y/n): ")
        if not play_again:
            break


if __name__ == '__main__':
    main()
