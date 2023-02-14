"""
Користувач вводить натуральне число. Потрібно визначити, чи є рік із цим числом високосним.
Якщо рік є високосним, то виведіть `YES`, інакше виведіть `NO`.
Примітка: відповідно до григоріанського календаря, рік є високосним, якщо його номер кратний 4,
 але не кратний 100, а також якщо він кратний 400.
"""


def count_year(your_year):
    if your_year % 4 ==0 and your_year % 100 != 0 or your_year % 400 == 0:
        print("YES")
    else:
        print("NO")


def test():
    assert count_year(1996) is None


def main():
    enter_year = int(input("Enter your year: "))

    result = count_year(enter_year)

    print(result)


if __name__ == '__main__':
    main()
    test()
