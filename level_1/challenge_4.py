"""
Reto #4 "Suma de enteros"
=============================

.. note::

    Instrucciones: otro clásico conocido, donde pedirás
    al usuario que ingrese 2 números y muestre en pantalla
    el resultado. Si quieres añadir más dificultad puedes
    utilizar números con punto decimal y especificar el
    número de decimales después del punto.

    Ejemplo: 2.5633 + 5.6883 = 8.25

"""


def sum_int():
    """Solicita dos números alusuario, posteriormente suma los números e
    imprime el resultado en pantalla."""
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    print(f"El resultado de sumar {num1} + {num2} es:")
    sum_int = print(num1 + num2)
    return sum_int


if __name__ == "__main__":
    sum_int()
