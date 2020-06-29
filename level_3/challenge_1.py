"""
Reto #1 - Longitud del string
===============================

.. note::

    Pide a tu usuario que ingrese el nombre de su curso favorito, 
    obtén la longitud de ese string y muéstralo en pantalla.
"""

def favourite_course(fav_course: str) -> int:
    """Recibe el nombre del curso favorito del usuario
    y retorna el tamaño de ese string.

    :type fav_course: str
    :param fav_course: Nombre del curso favorito del usuario.
    """

    len_fav_course = len(fav_course)
    return len_fav_course


if __name__ == "__main__":
    fav_course = input("Nombra tu curso favorito de platzi: ")
    print(f"Genial, Tu curso favorito es {fav_course}.")
    result = favourite_course(fav_course)
    print(f"El nombre del curso tiene una longiud de {result} caracteres.")
