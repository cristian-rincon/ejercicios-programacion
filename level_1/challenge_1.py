"""
Reto #1 “Hola Mundo”
====================

.. note::  
    
    Instrucciones: este es un clásico de clásicos, 
    pero haremos un pequeño cambio. En lugar de 
    solo imprimir un mensaje en pantalla, pedirás 
    al usuario que digite un nombre y mostrarás 
    en pantalla lo siguiente: "Hola, [nombre]"
"""


def hello1():
    """Solicita el nombre del usuario y posteriormente imprime un saludo
    personalizado.

    :rtype: str
    """
    name = input("Ingresa tu nombre: ")

    while name != "":
        greeting = print(f"Hola, {name}")
        return greeting

    print("El nombre no debe estar vacío")


def hello2():
    """Solicita el nombre y apellido del usuario, posteriormente imprime un
    saludo personalizado."""
    name = input("Ingresa tu nombre: ")
    lastname = input("Ingresa tu apellido: ")

    while name or lastname != "":
        greeting = print(f"Hola, {name} {lastname}")
        return greeting

    print("El nombre no debe estar vacío")


if __name__ == "__main__":
    hello1()
