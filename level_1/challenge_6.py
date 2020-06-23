"""
Reto #6 "Resta de pizzas"
==========================

.. note::

    Instrucciones: llegaste a una fiesta con X cantidad 
    de rebanadas de pizza (indicadas por el usuario), 
    después de un rato se consumió Y cantidad de rebanadas 
    y quedan Z. Fácil ¿cierto?

    El reto está en que expreses lo que sucede es una forma 
    comprensible para cualquier persona, imprescindible pensar en tus usuarios 😉.

"""


def substraction(a: int, b: int) -> int:
    """Solicita dos números al usuario y los resta.

    :type a: int
    :param a: Primer número para sumar

    :type b: int
    :param b: Segundo número para sumar

    :rtype: int
    """

    return a - b


if __name__ == "__main__":

    helper_text_1 = print(
        """
    ¡Resta de pizzas!
    Este programa te ayudará a saber cuántas 
    porciones de pizzas te quedan luego de comerte algunas.

    Debes indicar el número de porciones inicial y
    cuántas te comiste.
    
    """
    )
    num1 = int(input("Ingresa el número de porciones inicial: "))
    num2 = int(input("Ingresa el número de porciones que te comiste: "))

    pizzas_final_number = substraction(num1, num2)

    if pizzas_final_number < 0:
        print("No puede existir un número negativo de pizzas")
    else:
        if pizzas_final_number == 1:
            helper_text = print(f"Te queda {pizzas_final_number} porción de pizza.")
        else:
            helper_text = print(f"Te quedan {pizzas_final_number} porciones de pizza.")
