"""
Написати функцію, яка обчислює площу та об'єм конуса за його радіусом та висотою. Функція має повертати два значення.
"""

import math


def cone_square_and_volume(radius, height):  # returns 2 floats
    plosha = (math.pi*(radius**2)) + (math.pi*radius*(math.sqrt((radius**2) + (height**2))))
    volume = (math.pi*(radius**2)*height)/3
    return plosha, volume


enter_redius = int(input("Please enter radius: "))
enter_height = int(input("Please enter height: "))

result = cone_square_and_volume(enter_redius, enter_height)

print("Plosha is: ", round(result[0]), "\nVolume is: ", round(result[1]))

