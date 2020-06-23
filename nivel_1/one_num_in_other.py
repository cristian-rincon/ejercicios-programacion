"""
Reto #11 "Cuantas veces un número en otro"
===========================================

Instrucciones: pide al usuario ingresar un número mayor 
a 1000 y otro menor a 100. Indica de una forma sencilla 
de entender al usuario cuantas veces cabe el número menor 
a 100 en el número mayor a 1000.

"""


if __name__ == "__main__":

    num1 = 0

    while num1 < 1000:
        num1 = int(input(">>> Ingresa un número mayor a 1000: "))

    num2 = int(input(">>> Ingresa un número menor a 100: "))

    result = num1 // num2
    print(f"El número {num2} cabe {result} veces en {num1}")
