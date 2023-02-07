"""Даний рядок вигляду 'Taras Shevchenko*1814-03-09*1861-03-10', тобто вказане ім'я, прізвище та дати народження та смерті.
Написати програму, що отримуючи такий рядок через input() виводить на екран окремими рядками ім'я та прізвище людини
та її вік в роках. Для простоти при розрахунку віку можете ігнорувати число місяця та місяць.
 Тобто для рядку 'Taras Shevchenko*1814-03-09*1861-03-10' програма має вивести:
Name: Taras Schevchenko
Age: 47 years"""

# Taras Shevchenko*1814-03-09*1861-03-10

entered_value = input("Enter your test value:\n")
merger = entered_value.split('*')
print(merger)

print("Name: ", merger[0])
print("Age: ", int(merger[2][:4]) - int(merger[1][:4]), "years")
