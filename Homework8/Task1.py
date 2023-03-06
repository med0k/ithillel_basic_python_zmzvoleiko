"""
Завдання 1.
Дано довільний список. Створити функцію index(lst, elem), що повертатиме індекс elem в списку lst, або,
 якщо елемент відсутній, то None. Не можна використовувати метод list().index().

def index(lst, elem):  # returns integer or None
    pass
"""


def index(lst, elem):
    for num in range(len(lst)):
        if lst[num] == elem:
            return num
    return None


def main():
    my_list = ['Max', 6, 'Petya', '40', 'kek', 60, 56, 11, 23]
    print(index(my_list, 'kek'))
    print(index(my_list, 'Vasya'))


if __name__ == '__main__':
    main()
