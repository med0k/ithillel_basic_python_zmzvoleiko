"""
Завдання 2.
Створити функцію copydeep(obj), що створює і повертає глибоку копію переданого об'єкту obj. Умови:

Не можна використовувати deepcopy з модулю copy
Вважати, що можливі лише ці типи об'єктів та іхніх можливих вкладених елементів, які можуть бути передані у функцію:
 str, int, float, bool, list, tuple
Для спрощення завдання вважати, що вхідні колекції (tuple, list) не матимуть рекурсивних елементів,
тобто не міститимуть самі себе на будь-якій глибині.
Якщо редагується будь-яка частина чи вкладений на довільній глибині елемент оригінального списку,
то в копії не має нічого змінюватися. Наприклад:
lst1 = ['a', 1, 2.0, ['b']]
lst2 = copydeep(lst1)
lst1[3].append(0)
print(lst1[3], lst2[3])  # ['b', 0] ['b']
"""


def copydeep(obj):
    if isinstance(obj, (str, int, float, bool)):
        return obj
    elif isinstance(obj, list):
        new_list = []
        for elem in obj:
            new_list.append(copydeep(elem))
        return new_list
    elif isinstance(obj, tuple):
        new_tuple = ()
        for elem in obj:
            new_tuple += (copydeep(elem))
        return new_tuple
    else:
        return None


def main():
    lst1 = ['a', 1, 2.0, ['b']]
    lst2 = copydeep(lst1)
    lst1[3].append(0)
    print(lst1[3], lst2[3])


if __name__ == "__main__":
    main()
