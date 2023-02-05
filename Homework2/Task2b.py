# Порахувати ту ж формулу, але для значень a=2, b=5, c=2 (для обчислення кореню використати оператор **)!

a = 2
b = 5
c = 2
square_root = (b ** 2) - (4*a*c)

x1 = (-b + (square_root ** 0.5)) / (2*a)
x2 = (-b - (square_root ** 0.5)) / (2*a)

print('Result for x1: ' , x1)
print('Result for x2: ' , x2)