"""
Reto #4 - I like turtles
============================

.. note::

    Escribe un programa que pida al usuario ingrese su animal favorito, 
    si coloca ‘Tortuga’, ‘tortuga’, ‘TORTUGA’ o cualquier otra variante 
    de la palabra entonces mostrar en pantalla “También me gustan las tortugas”. 
    En caso contrario mostrar el mensaje “Ese animal es genial, pero prefiero las tortugas”.
"""
import re


def like_turtles(text: str):
    """Recibe un nombre de un animal, convierte la cadena de texto a minúsculas
    y a través de la librería re valida si coincide con el texto dado. De acuerdo
    con la coincidencia envía un mensaje personalizado.

    :type text: str
    :param text: Cadena de texto solicitada al usuario
    """

    text_lower = text.lower()
    x = re.search("tortuga", text_lower)

    if x:
        print("También me gustan las tortugas.")
    else:
        print("Ese animal es genial, pero prefiero las tortugas.")


if __name__ == "__main__":

    ask_animal = input("¿Cual es tu animal favorito? ")

    like_turtles(ask_animal)
