"""
Завдання 1.
Дано довільний список. Створити функцію index(lst, elem), що повертатиме індекс elem в списку lst, або,
 якщо елемент відсутній, то None. Не можна використовувати метод list().index().

def index(lst, elem):  # returns integer or None
    pass
"""


def index(lst, elem):  # returns integer or None
    for num in range(len(lst)):
        if lst[num] == elem:
            return num
    return None


def main():
    my_list = [5, 6, '30', '40', 'kek', 60, 56, 11, 23]
    print(index(my_list, 23))


if __name__ == '__main__':
    main()
