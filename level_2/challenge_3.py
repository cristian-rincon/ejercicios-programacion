"""
Reto #3 - Rangos cambiantes.
============================

.. note::

    Nuevamente pide a tu usuario que indique 3 números: un límite superior, 
    un límite inferior y uno de comparación. Si el número de comparación se 
    encuentra entre los 2 primeros, comunicarlo en pantalla. En caso estar 
    por debajo del límite inferior o por arriba del límite superior, también 
    mostrarlo en pantalla.
"""


def in_range_number(num1: int, num2: int, num3: int) -> int:
    """Recibe tres números, el primero será el límite superior, el segundo será el
    límite inferior y el tercero es el número a comparar.

    :type num1: int
    :param num1: Límite superior

    :type num2: int
    :param num2: Límite inferior.

    :type num3: int
    :param num3: Número a comparar.

    :rtype: int
    """

    if num1 > num3 and num2 < num3:
        print(
            f">>> El número {num3} se encuentra bajo el rango máximo y también se encuentra por encima del rango mínimo."
        )
    else:
        print(f">>> El número {num3} excede el límite permitido.")


if __name__ == "__main__":

    num1 = int(input("Ingresa el límite superior: "))
    num2 = int(input("Ingresa el límite inferior: "))
    num3 = int(input("Ingresa el número a comparar: "))

    in_range_number(num1, num2, num3)
