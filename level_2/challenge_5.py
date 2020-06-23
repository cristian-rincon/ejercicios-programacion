"""
Reto #5 - ¿Cómo está el clima?
==============================

.. note::

    Crea un programa que pregunte al usuario si está lloviendo, en caso de responder 
    “sí” pregunta si está haciendo mucho viento y si responde “sí” nuevamente muestra 
    un mensaje indicando que hace mucho viento para salir con una sombrilla. En caso 
    contrario, anima al usuario a que lleve una sombrilla. Para el caso de responder 
    “no” en la primer pregunta, entonces solo desea un bonito día.

    Considera que las respuestas pueden pasarse a minúsculas para evitar posibles errores.

.. code-block::

    if __name__ == "__main__":

    print("¿Está lloviendo?")

    options()
    command = input()
    command = command.upper()

    if command == "S":
        print("¿Hay mucho viento?")
        options()
        command = input()
        command = command.upper()
        if command == "S":
            print("Es mejor que te quedes en casa.")
        else:
            print("Recuerda llevar tu sombrilla.")
    else:
        print("Que tengas un buen día.")

"""


def options():
    """Imprime dos opciones en pantalla. Si o No
    """

    print("[S] - Si")
    print("[N] - No")


if __name__ == "__main__":

    print("¿Está lloviendo?")

    options()
    command = input()
    command = command.upper()

    if command == "S":
        print("¿Hay mucho viento?")
        options()
        command = input()
        command = command.upper()
        if command == "S":
            print("Es mejor que te quedes en casa.")
        else:
            print("Recuerda llevar tu sombrilla.")
    else:
        print("Que tengas un buen día.")
