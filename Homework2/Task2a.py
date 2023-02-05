# З допомогою Python порахувати наступні вирази для a=1, b=5, c=4 (використати функцію sqrt з модулю math):!

import math

a = 1
b = 5
c = 4

x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

print('Result for x1: ' , x1)
print('Result for x2: ' , x2)