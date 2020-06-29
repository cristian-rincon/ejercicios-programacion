"""
Reto #7 - Mensajes opcionales
==============================

.. note::

    Crearás un un script para el que el usuario indicará un número entre 1 y 6. 
    Como respuesta se le brindará un mensaje según el número leido:

    1 - Hoy aprenderemos sobre programación
    2 - ¿Qué tal tomar un curso de marketing digital?
    3 - Hoy es un gran día para comenzar a aprender de diseño
    4 - ¿Y si aprendemos algo de negocios online?
    5 - Veamos un par de clases sobre producción audiovisual
    6 - Tal vez sea bueno desarrollar una habilidad blanda en Platzi

    En caso indicar un número distinto, pedir al usuario que ingrese uno en el rango válido.

"""


def optional_message(number: int) -> str:
    """Recibe un número entre 1 y 6, imprime en pantalla un mensaje personalizado según
    el número dado.
    """

    messages = {
        "1": "Hoy aprenderemos sobre programación",
        "2": "¿Qué tal tomar un curso de marketing digital?",
        "3": "Hoy es un gran día para comenzar a aprender de diseño",
        "4": "¿Y si aprendemos algo de negocios online?",
        "5": "Veamos un par de clases sobre producción audiovisual",
        "6": "Tal vez sea bueno desarrollar una habilidad blanda en Platzi",
    }

    if number == 1:
        return messages.get("1")
    elif number == 2:
        return messages.get("2")
    elif number == 3:
        return messages.get("3")
    elif number == 4:
        return messages.get("4")
    elif number == 5:
        return messages.get("5")
    elif number == 6:
        return messages.get("6")
    else:
        error = str("Ingresa un número válido.")
        return error


if __name__ == "__main__":
    print("Bienvenido")
    message = int(
        input("Ingresa un número entre 1 y 6 y obtendrás un mensaje personalizado: ")
    )

    print(optional_message(message))
