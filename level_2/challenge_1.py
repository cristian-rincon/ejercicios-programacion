"""
Reto #1 - Número mayor y menor
===============================

.. note::

    Escribe un programa que pida al usuario 2 números, mostrando como 
    salida cuál es el número mayor y la diferencia de uno respecto al 
    otro. En caso de que los números sean iguales, mostrarlo también 
    en pantalla.
"""


def min_maj_number(num1: int, num2: int) -> int:
    """Recibe dos números, informa cual es el número mayor y la diferencia
    entre ambos. Si ambos números son iguales también se lo indicará al
    usuario.

    :type num1: int
    :param num1: Primer número para sumar

    :type num2: int
    :param num2: Segundo número para sumar

    :rtype: int
    """

    if num1 > num2:
        difference_between = num1 - num2
        print(f"El número mayor es: {num1}")
        print(f"La diferencia entre {num1} y {num2} es: {difference_between}")
    elif num1 < num2:
        difference_between = num2 - num1
        print(f"El número mayor es: {num2}")
        print(f"La diferencia entre {num2} y {num1} es: {difference_between}")
    else:
        print("Ambos números son iguales.")


if __name__ == "__main__":

    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    min_maj_number(num1, num2)
