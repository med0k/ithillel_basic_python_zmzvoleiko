# Написати програму, що за допомогою функції input() запитує кількість гривень і потім виводить еквіваленте число доларів США (курс довільний -- можна підгледіти на будь-яку дату у вашому банку або у НБУ). Наприклад:
#
# >>> Введіть кількість гривень:
# ... 74.63
# >>> Станом на 25 серпня 2022 року це становить 2.0 Долари США :(

import datetime
from decimal import Decimal

now = datetime.datetime.now()

amount_UA = Decimal(input('Enter your amount UA: '))

print(type(amount_UA))

current_curs = Decimal('36.9')
calc= amount_UA / current_curs

print('For current time ', now.strftime('%d-%m-%Y-%H:%M'),"it's equal to", round(calc,2) , 'USA')