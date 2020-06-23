"""
Reto #7 "Edad futura y pasada"
==========================

.. note::

    Instrucciones: pide al usuario que indique su nombre y su edad. 
    Como mensaje de salida le indicarás que edad tuvo el año pasado 
    y cuantos años tendrá el siguiente año.

    Ejemplo: [nombre] el año pasado tenías X años y el próximo año cumplirás Y años.

"""

from substraction import substraction
from sum_multiplication import sum


if __name__ == "__main__":

    helper_text_1 = print("""
    ¡Edad futura y pasada!
    Este programa te ayudará a saber cuantos años
    tenías el año pasado y cuantos tendrás el siguiente

    Debes indicar tu nombre y tu edad actual.
    
    """)
    name = input('¿Cómo te llamas? ')
    num1 = int(input("¿Cuantos años tienes? "))
    num2 = 1
    last_year_age = substraction(num1, num2)
    next_year_age = sum(num1, num2)

    if name != "":
        print(f'Hola {name}, el año pasado tenías {last_year_age} años ')
        print(f'y el próximo año cumplirás {next_year_age} años.')
    else:
        print('El nombre no debe estar vacío')