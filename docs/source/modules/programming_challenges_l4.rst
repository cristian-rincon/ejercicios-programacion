Ejercicios de Programación - Nivel 4 \| Matemáticas
===================================================

Reto #1 - Multiplicar decimales
-------------------------------

Pide a tu usuario que ingrese 2 números con decimales (cuantos más
mejor) y muestra el resultado de multiplicarlos ¿fácil, no?

.. code:: ipython3

    def multiply_decimals(a:float,b:float):
        return float(a * b)
    
    a = float(input("Ingresa el primer número con decimales a multiplicar\n"))
    b = float(input("Ingresa el segundo número con decimales a multiplicar\n"))
    
    print(multiply_decimals(a,b))


.. parsed-literal::

    Ingresa el primer número con decimales a multiplicar
    5.5
    Ingresa el segundo número con decimales a multiplicar
    6.5
    35.75


Reto #2 - Reducir los decimales
-------------------------------

Toma como base el reto anterior, pero ajústalo para que el resultado
muestre solamente 1, 2, 3 o 4 decimales.

.. code:: ipython3

    a = float(input("Ingresa el primer número con decimales a multiplicar\n"))
    b = float(input("Ingresa el segundo número con decimales a multiplicar\n"))
    
    print(round(multiply_decimals(a,b),3))


.. parsed-literal::

    Ingresa el primer número con decimales a multiplicar
    45.5555555
    Ingresa el segundo número con decimales a multiplicar
    53.44444444
    2434.691


Reto #3 - Raíces cuadradas redondeadas
--------------------------------------

Pide a tu usuario que ingrese un número, cuyo valor debe ser mayor a 20,
luego calcula su raíz cuadrada y reduce a 2 o 3 decimales el resultado
final.

.. code:: ipython3

    import math
    
    a = int(input("Ingresa un número mayor a 20:\n"))
    round(math.sqrt(a),3)


.. parsed-literal::

    Ingresa un número mayor a 20:
    50




.. parsed-literal::

    7.071



Reto #4 - Calcular área de un círculo
-------------------------------------

Solicita a tu usuario que ingrese un número el cual será el radio de un
círculo y con este dato calcula el área de un círculo.

Si tu lenguaje cuenta con librerías específicas para este propósito haz
uso de las mismas.

.. code:: ipython3

    pi = math.pi
    
    radius = int(input("Ingresa el radio del círculo a calcular:\n"))
    circle_area = (radius ** 2) * pi
    
    print(f"El área del circulo es: {circle_area}")


.. parsed-literal::

    Ingresa el radio del círculo a calcular:
    5
    El área del circulo es: 78.53981633974483


Reto #5 - Calcular volumen de un cilindro
-----------------------------------------

Pide a tu usuario que indique el radio y la profundidad de un cilindro.
Después aplica la fórmula correspondiente para calcular el volumen del
cilindro y reduce el resultado a un solo decimal.

.. code:: ipython3

    pi = math.pi
    
    radius = int(input("Ingresa el radio del cilindro a calcular:\n"))
    h = int(input("Ingresa la altura del cilindro a calcular:\n"))
    
    cylinder_area = pi * (radius ** 2) * h
    
    print(f"El volumen del cilindro es: {round(cylinder_area,3)}")


.. parsed-literal::

    Ingresa el radio del cilindro a calcular:
    5
    Ingresa la altura del cilindro a calcular:
    9
    El volumen del cilindro es: 706.858


Reto #6 - Mostrar enteros y residuos
------------------------------------

Pide al usuario que ingrese 2 números, divídelos, muestra un resultado
como enteros y además el residuo por separado de una forma que seal
fácil de entender al usuario.

Por ejemplo: “9 dividido entre 2 es 4 y sobra 1”.

.. code:: ipython3

    num1 = int(input("Ingresa el divisor:\n"))
    num2 = int(input("Ingresa el dividendo:\n"))
    
    residue = num1 % num2
    div_result = math.floor(num1 / num2)
    
    print(f">>> {num1} dividido entre {num2} es {div_result} y sobra {residue}")


.. parsed-literal::

    Ingresa el divisor:
    10
    Ingresa el dividendo:
    3
    >>> 10 dividido entre 3 es 3 y sobra 1


Reto #7 - Calcular perímetros y áreas
-------------------------------------

Muestra un menú con distintas figuras geométricas, por lo menos 3
diferentes (triángulo, cuadrado, pentágono, etc.)

Tu usuario debe poder elegir alguna de estas figuras, indicar la
distancia de sus lados y mostrar como resultado tanto el perímetro como
el área de dicha figura.

.. code:: ipython3

    options = ['🔺','🟩','🔵']
    
    print("Selecciona la figura a la cual quieres calcularle el perímetro y el área")
    print("""
    [1] 🔺
    [2] 🟩 
    [3] 🔵
    """)
    
    num_options = int(input())
    
    if num_options == 1:
      print(f"Seleccionaste el {options[0]}")
      side = float(input("Ingresa la distancia del lado:"))
      floor = side
      perimeter = (side * 2) + floor
      area = floor * (side/2) ** 2
      print(f"El perímetro de tu triángulo es {perimeter} y su área es de {area}")
    elif num_options == 2:
      print(f"Seleccionaste el {options[1]}")
      side = int(input("Ingresa la distancia del lado:"))
      perimeter = side ** 2 
      area = side * side
      print(f"El perímetro de tu cuadrado es {perimeter} y su área es de {area}")
    elif num_options == 3:
      print(f"Seleccionaste el {options[2]}") 
      radius = float(input("Ingresa el radio del circulo a calcular:\n"))
      perimeter = (2 * math.pi) * radius
      area = math.pi * (radius ** 2)
      print(f"El perímetro de tu circulo es {round(perimeter,3)} y su área es de {round(area,3)}")
    
    
    



.. parsed-literal::

    Selecciona la figura a la cual quieres calcularle el perímetro y el área
    
    [1] 🔺
    [2] 🟩 
    [3] 🔵
    
    3
    Seleccionaste el 🔵
    Ingresa el radio del circulo a calcular:
    5
    El perímetro de tu circulo es 31.416 y su área es de 78.54

