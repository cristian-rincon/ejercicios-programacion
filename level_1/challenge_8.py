"""

Reto #8 "Divide la cuenta"
==========================

.. note::

    Instrucciones: vas con tus amigos a tu restaurante favorito 
    y acuerdan dividir la cuenta. Para facilitar las cosa pedirás 
    al usuario que indique el total a pagar, entre cuantas personas 
    se dividirá la cuenta, porcentaje de propina a incluir, 
    un porcentaje de impuestos, total a pagar incluyendo propina 
    más impuestos y el total a pagar por cada persona.

"""


def divide(a: float, b: float) -> float:
    """Solicita dos números al usuario y los divide.

    :type a: float
    :param a: Dividendo

    :type b: float
    :param b: Divisor

    :rtype: float
    """
    return a / b


tip = 10
tax = 19

if __name__ == "__main__":

    helper_text = print(
        """
    Divide la cuenta
    ============================================
    Este programa te permitirá saber cuanto debe
    pagar cada persona sobre la cuenta total del
    restaurante.
    """
    )

    total = float(input("Indica el valor total de la cuenta: "))
    num_of_persons = float(input("¿Entre cuantas personas se dividirá la cuenta? "))

    calculate_cost_per_person = divide(total, num_of_persons)
    calculate_tip = (total * tip) / 100
    calculate_tax = (total * tax) / 100

    print(f"Cada persona debe pagar: $ {calculate_cost_per_person} COP")
    print(
        f"En esta cuenta pagaste el {tip}% en propinas, lo cual equivale a: $ {calculate_tip} COP"
    )
    print(
        f"En esta cuenta pagaste el {tax}% en impuestos, lo cual equivale a: $ {calculate_tax} COP"
    )
