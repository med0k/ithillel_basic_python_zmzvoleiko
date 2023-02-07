# Написати програму, що перетворює значення рядкової змінної з формату snake_case в формат CapitalizedWords
# (a.k.a. Capitalized camelCase). Значення змінної отримуйте з input(). Для простоти вважаємо, що значення змінної
# завжди складається з 3-х слів, але, можна оброблювати і "загальний випадок", тобто, коли будь-яка кількість слів.
# Наприклад: 'employee_first_name' -> 'EmployeeFirstName'.

entered_words = input('Enter three snake_case words: \n')
entered_words = entered_words.title()

merger = entered_words.split('_')
new_words = "".join(merger)

print('camelCase looks like:\n', new_words)