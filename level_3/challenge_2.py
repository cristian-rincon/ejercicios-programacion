"""
Reto #2 "Suma" de strings
===============================

.. note::

    Crea un programa en el que le pidas en 3 variables distintas: 
    nombre, apellido y comida favorita. Como salida mostrarás el 
    mensaje Hola, mi nombres es {nombre} {apellido} y mi comida 
    favorita es {comida} en un solo string.
"""


def sum_of_strings(name: str, lastname: str, fav_food: str):
    """Recibe nombre, apellido y comida favorita, combina las 
    cadenas de texto, aplica capitalize() a nombre y apellido 
    y retorna un mensaje predeterminado.

    Returns:
        [type]: [description]
    """

    message = print(
        f"Hola, mi nombre es {name.capitalize()} {lastname.capitalize()} y mi comida favorita es {fav_food}"
    )

    return message


if __name__ == "__main__":
    name = input("¿Cual es tu nombre? ")
    lastname = input("¿Cual es tu apellido? ")
    fav_food = input("¿Cual es tu comida favorita? ")

    sum_of_strings(name, lastname, fav_food)
