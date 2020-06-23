"""
Reto #2 - En el rango, por favor
=================================

.. note::

    Pide al usuario que indique 2 números: uno que servirá como 
    límite y otro para comparar. Si el segundo número es menor 
    al primero, mostrarás un mensaje diciendo “El número ‘x’ se 
    encuentra en el rango, gracias” y en caso contrario dirá 
    “El número ‘x’ excede el límite permitido”.
"""


def in_range_number(num1: int, num2: int) -> int:
    """Recibe dos números, el primero será el límite y el segundo será el
    número a comparar.

    :type num1: int
    :param num1: Límite

    :type num2: int
    :param num2: Número a comparar.

    :rtype: int
    """

    if num1 > num2:
        print(f">>> El número {num2} se encuentra en rango, gracias.")
    else:
        print(f">>> El número {num2} excede el límite permitido.")


if __name__ == "__main__":

    num1 = int(input("Ingresa el número límite: "))
    num2 = int(input("Ingresa el número a comparar: "))

    in_range_number(num1, num2)
