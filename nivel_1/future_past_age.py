"""
Reto #7 "Edad futura y pasada"
==========================

.. note::

    Instrucciones: pide al usuario que indique su nombre y su edad. 
    Como mensaje de salida le indicarás que edad tuvo el año pasado 
    y cuantos años tendrá el siguiente año.

    Ejemplo: [nombre] el año pasado tenías X años y el próximo año cumplirás Y años.

.. code-block:: python

    from .substraction import substraction
    from .sum_multiplication import sum


    if __name__ == "__main__":

        helper_text_1 = print(""
        ¡Edad futura y pasada!
        Este programa te ayudará a saber cuantos años
        tenías el año pasado y cuantos tendrás el siguiente

        Debes indicar tu nombre y tu edad actual.
        "")
        name = input('¿Cómo te llamas? ')
        actual_age = int(input("¿Cuantos años tienes? "))
        num2 = 1
        last_year_age = substraction(actual_age, num2)
        next_year_age = sum(actual_age, num2)

        if name != "":
            print(f'Hola {name}, el año pasado tenías {last_year_age} años ')
            print(f'y el próximo año cumplirás {next_year_age} años.')
        else:
            print('El nombre no debe estar vacío')

"""

from .substraction import substraction # En pruebas locales es necesario quitar el punto, para documentación se debe dejar
from .sum_multiplication import sum # En pruebas locales es necesario quitar el punto, para documentación se debe dejar


if __name__ == "__main__":

    helper_text_1 = print("""
    ¡Edad futura y pasada!
    Este programa te ayudará a saber cuantos años
    tenías el año pasado y cuantos tendrás el siguiente

    Debes indicar tu nombre y tu edad actual.
    
    """)
    name = input('¿Cómo te llamas? ')
    actual_age = int(input("¿Cuantos años tienes? "))
    num2 = 1
    last_year_age = substraction(actual_age, num2)
    next_year_age = sum(actual_age, num2)

    if name != "":
        print(f'Hola {name}, el año pasado tenías {last_year_age} años ')
        print(f'y el próximo año cumplirás {next_year_age} años.')
    else:
        print('El nombre no debe estar vacío')
