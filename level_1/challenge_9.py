"""

Reto #9 "Calculando días"
==========================

.. note::

    Instrucciones: escribe un programa al que le indiques una cantidad de 
    días y como resultado deberá mostrar cuantas horas, minutos y segundos 
    hay en dicha cantidad de días.

.. code-block:: python

    if __name__ == "__main__":
        
        helper_text = print(""
        Calculando días
        ===============================================
        Este programa te permitirá saber cuantas horas,
        minutos y segundos hay en una cantidad de días 
        dados.
        "")

        days = int(input(">>> Indica la cantidad de días a calcular: "))

        minutes = (60 * 24) * days

        seconds = 60 * minutes

        print(f">>> En {days} días hay:")
        print(f">>> {minutes} minutos.")
        print(f">>> {seconds} segundos.")

"""


if __name__ == "__main__":

    helper_text = print(
        """
    Calculando días
    ===============================================
    Este programa te permitirá saber cuantas horas,
    minutos y segundos hay en una cantidad de días 
    dados.
    """
    )

    days = int(input(">>> Indica la cantidad de días a calcular: "))

    minutes = (60 * 24) * days

    seconds = 60 * minutes

    print(f">>> En {days} días hay:")
    print(f">>> {minutes} minutos.")
    print(f">>> {seconds} segundos.")
