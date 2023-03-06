"""
Завдання 3.
Згідно з древньою індійською легендою творець гри в шахи за свій винахід попросив у раджі незначну на перший погляд
 винагороду: стільки пшеничних зерен, скільки опиниться на шаховій дошці, якщо на першу клітинку покласти одне зерно,
 на другу -- два зерна, на третю -- чотири, і т.д.. Виявилося, що такої кількості зерна немає на усій планеті
 (2**64-1 зерен). Напишіть програму, що вираховує починаючи з якої клітинки дошки раджі треба було віддати Nкг зерна,
 де N -- вводить користувач. Прийняти вагу однієї зернинки за 35мг.
 Номер клітинки виводити в букво-циферних традиційних шахових координатах.
"""


def calculate_position(kgs):
    seeds_input = float(input("Enter count kg that you have to return to Redgi: "))
    seeds_count = int(seeds_input / kgs * 1000000)
    current_square = 1
    grains_on_current_square = 1
    grains_on_board = 0
    while grains_on_board < seeds_count:
        grains_on_board += grains_on_current_square
        if grains_on_board >= seeds_count:
            break
        grains_on_current_square *= 2
        current_square += 1
    col = (current_square - 1) // 8 + 1
    row = chr((current_square - 1) % 8 + ord('a'))
    return col, row


def main():
    kgs = 0.03584
    print(calculate_position(kgs))


if __name__ == '__main__':
    main()
