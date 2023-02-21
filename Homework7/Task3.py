"""
Завдання 3.
Згідно з древньою індійською легендою творець гри в шахи за свій винахід попросив у раджі незначну на перший погляд
 винагороду: стільки пшеничних зерен, скільки опиниться на шаховій дошці, якщо на першу клітинку покласти одне зерно,
 на другу -- два зерна, на третю -- чотири, і т.д.. Виявилося, що такої кількості зерна немає на усій планеті
 (2**64-1 зерен). Напишіть програму, що вираховує починаючи з якої клітинки дошки раджі треба було віддати Nкг зерна,
 де N -- вводить користувач. Прийняти вагу однієї зернинки за 35мг.
 Номер клітинки виводити в букво-циферних традиційних шахових координатах.
"""


def main():
    n = float(input("Enter weight that you have to return to Redgi in kg: "))
    total_grains = int(n * 1000000 // 0.035)
    grains_on_current_square = 1
    grains_on_board = 0
    current_square = 1

    while grains_on_board < total_grains:
        grains_on_board += grains_on_current_square
        if grains_on_board >= total_grains:
            break
        grains_on_current_square *= 2
        current_square += 1

    stroka = (current_square - 1) // 8 + 1
    column = chr((current_square - 1) % 8 + ord('a'))

    print(f"Redgi have to return {grains_on_board / 1000000:.2f} kg seeds on square {column}{stroka}")


if __name__ == '__main__':
    main()
