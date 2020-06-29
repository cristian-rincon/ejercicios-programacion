"""
Reto #6 - Edad permitida
========================

.. note::

    Pide al usuario que ingrese su edad y mostrarás un mensaje correspondiente 
    si esta coincide con las siguientes condiciones:
    
    * Menos de 18 años: ¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.
    * Entre 18 y 29 años: Es un momento excelente para impulsar tu carrera.
    * Más de 30 años: Nunca es tarde para aprender ¿Qué curso tomaremos?

"""


def allowed_age(age: int) -> str:
    """Solicita la edad y dependiendo de la misma emite un mensaje personalizado.

    :type age: int
    :param age: Edad del usuario.

    :rtype: str
    """

    if age < 18:
        print("¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.")
    elif age > 18 and age < 30:
        print("Es un momento excelente para impulsar tu carrera.")
    else:
        print("Nunca es tarde para aprender ¿Qué curso tomaremos?")


if __name__ == "__main__":
    print("¡Hola!")
    ask_age = int(input("¿Cuantos años tienes? "))

    allowed_age(ask_age)
