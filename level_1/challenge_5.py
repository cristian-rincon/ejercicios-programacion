"""
Reto #5 "Suma y multiplicación"
================================

.. note::

    Instrucciones: añadiendo un extra al reto anterior 
    ahora el usuario ingresará 3 números, sumarás los 2 
    primeros y el resultado será multiplicado por el tercero. 
    Añade las consideraciones del punto decimal del reto anterior.

    Ejemplo:

.. code-block:: python

    Datos de entrada:2, 3, 4
    Resultado:20

"""


def sum(a: int, b: int) -> int:
    """Solicita dos números al usuario y los suma.

    :type a: int
    :param a: Primer número para sumar

    :type b: int
    :param b: Segundo número para sumar

    :rtype: int
    """

    return a + b


def multiplication(a: int, b: int) -> int:
    """Solicita dos números al usuario y los multiplica.

    :type a: int
    :param a: Primer número para multiplicar

    :type b: int
    :param b: Segundo número para multiplicar

    :rtype: int
    """

    return a * b


if __name__ == "__main__":

    helper_text_1 = print(
        """
    Ingresa 3 números, los primeros dos se sumarán, 
    el resultado se multiplicará por el tercero y 
    el valor final se escribirá en pantalla.
    """
    )
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    helper_text = print(f"El resultado es:")
    print(multiplication(sum(num1, num2), num3))
