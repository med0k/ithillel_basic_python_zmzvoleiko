# Поміняти місцями значення змінних a та b для наступних випадків:!
# c) Типи значень в змінних a та b можуть бути лише цілими числами. Поміняйте значення змінних використовуючи лише арифметичні операції '+' та '-'

a = 18
b = 10

print("Old values equals:", "a = ", a,", b = ", b)

a = a + b  # 28
b = a - b  # 28 - 10 = 18
a = a - b  # 28 - 18 = 10

print("New values equals:", "a = ", a, ", b = ", b)