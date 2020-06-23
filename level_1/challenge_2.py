"""
Reto #2 "Hola... nombre y apellido"
====================================

.. note::  
    
    Instrucciones: Ahora que sabemos incluir nombres, 
    podemos agregar más datos. Intentemos con un apellido 
    para tener algo así: ``Hola, [nombre] [apellido]``
"""


def helloworld_2():
    """Solicita el nombre y apellido del usuario, posteriormente imprime un
    saludo personalizado."""
    name = input("Ingresa tu nombre: ")
    lastname = input("Ingresa tu apellido: ")

    if name == "":
        print("El nombre no debe estar vacío")
    elif lastname == "":
        print("El apellido no debe estar vacío")
    else:
        greeting = print(f"Hola, {name} {lastname}")
        return greeting


if __name__ == "__main__":
    helloworld_2()
