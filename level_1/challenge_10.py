"""
Reto #10 “Conversor de millas”
===============================

.. note::

    Instrucciones: hay 1.609344 km en una milla (mi). 
    Escribe un programa en el que el usuario indique 
    una cantidad de millas y muestre en pantalla el 
    resultado convertido a kilómetros.

"""


def miles_converter(miles):
    """Calcula la equivalencia de millas en kilómetros.

    :type miles: float
    :param miles: Número de millas a convertir.

    :rtype: float
    """

    km = 1.609344

    result = km * miles

    return result


if __name__ == "__main__":

    print("Convertidor de millas a kilómetros")
    print("==================================")
    miles = float(input(">>> Ingresa la cantidad de millas a convertir: "))

    result = miles_converter(miles)

    print(f">>> {miles} millas equivalen a {result} kilómetros.")
