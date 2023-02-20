"""
Користувач вводить натуральне число. Потрібно визначити, чи є рік із цим числом високосним.
Якщо рік є високосним, то виведіть `YES`, інакше виведіть `NO`.
Примітка: відповідно до григоріанського календаря, рік є високосним, якщо його номер кратний 4,
 але не кратний 100, а також якщо він кратний 400.
"""


def count_year(your_year):
    return your_year % 4 == 0 and your_year % 100 != 0 or your_year % 400 == 0


def test():
    assert count_year(2017) is False
    assert count_year(1996) is True

def main():
    enter_year = int(input("Enter your year: "))

    result = count_year(enter_year)

    if result is True:
        print("yes")

    else:
        print("False")


if __name__ == '__main__':
    main()
    # test()
