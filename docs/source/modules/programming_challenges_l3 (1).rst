Ejercicios de Programación - Nivel 3
====================================

Reto #1 - Longitud del string
-----------------------------

Pide a tu usuario que ingrese el nombre de su curso favorito, obtén la
longitud de ese string y muéstralo en pantalla.

.. code:: ipython3

    def favourite_course(fav_course: str) -> int:
        """Recibe el nombre del curso favorito del usuario
        y retorna el tamaño de ese string.
    
        :type fav_course: str
        :param fav_course: Nombre del curso favorito del usuario.
        """
    
        len_fav_course = len(fav_course)
        return len_fav_course
    
    
    fav_course = input("Nombra tu curso favorito de platzi:\n")
    print(f"Genial, Tu curso favorito es {fav_course.capitalize()}.")
    result = favourite_course(fav_course)
    print(f"El nombre del curso tiene una longiud de {result} caracteres.")


.. parsed-literal::

    Nombra tu curso favorito de platzi:
    devops
    Genial, Tu curso favorito es Devops.
    El nombre del curso tiene una longiud de 6 caracteres.


Reto #2 “Suma” de strings
-------------------------

Crea un programa en el que le pidas en 3 variables distintas: nombre,
apellido y comida favorita. Como salida mostrarás el mensaje Hola, mi
nombres es {nombre} {apellido} y mi comida favorita es {comida} en un
solo string.

.. code:: ipython3

    def sum_of_strings(name: str, lastname: str, fav_food: str):
        """Recibe nombre, apellido y comida favorita, combina las 
        cadenas de texto, aplica capitalize() a nombre y apellido 
        y retorna un mensaje predeterminado.
    
        Returns:
            [type]: [description]
        """
    
        message = print(
            f"Hola, mi nombre es {name.capitalize()} {lastname.capitalize()} y mi comida favorita es {fav_food.capitalize()}"
        )
    
        return message
    
    
    name = input("¿Cual es tu nombre?\n")
    lastname = input("¿Cual es tu apellido?\n")
    fav_food = input("¿Cual es tu comida favorita?\n")
    sum_of_strings(name, lastname, fav_food)


.. parsed-literal::

    ¿Cual es tu nombre?
    cristian
    ¿Cual es tu apellido?
    rincon
    ¿Cual es tu comida favorita?
    lasagna
    Hola, mi nombre es Cristian Rincon y mi comida favorita es Lasagna


Reto #3 Ajusta las iniciales
----------------------------

Ahora, pedirás a tu usuario que ingrese su nombre, apellido y país de
origen en minúsculas. Después mostrarás los datos de salida con
mayúscula inicial al tratarse de nombres propios.

.. code:: ipython3

    def capitalize_sample(name, lastname, country):
        message = print(f"Hola {name.capitalize()} {lastname.capitalize()}, veo que eres de {country.capitalize()}. Yo soy de Colombia.")
        return message
    
    name = input("¿Cual es tu nombre? ")
    lastname = input("¿Cual es tu apellido? ")
    country = input("¿De qué país eres? ")
    
    capitalize_sample(name,lastname,country)


.. parsed-literal::

    ¿Cual es tu nombre? cristian
    ¿Cual es tu apellido? rincón
    ¿De qué país eres? colombia
    Hola Cristian Rincón, veo que eres de Colombia. Yo soy de Colombia.


Reto #4 String fragmentado
--------------------------

-  Pongámonos más exigentes 💥

Solicita a tu usuario que indique una oración de 10 o más caracteres, la
línea de un poema o canción funciona excelente. Calcula la longitud del
string, pide un número de rango inicial y final que esté entre la
longitud del string para al final mostrar el fragmento que incluya los
caracteres en ese intervalo.

.. code:: ipython3

    def fragmented_string(sentence, min_range, max_range):
    
        if min_range == '':
          min_range = 0
        if max_range == '':
          max_range = len(sentence)
        
        response_sentence = print(sentence[min_range:max_range])
    
        return response_sentence
    
    
    
    sentence = input("Indica una frase u oración de mínimo 10 caracteres: ")
    # Test sentence
    # Mi nombre es Cristian, soy programador y mi lenguaje favorito es Python
    if len(sentence) >= 10:
        print(f"La frase que envías tiene {len(sentence)} caracteres")
        min_range = input("Indica desde donde quieres ver la cadena de caracteres: ")
        max_range = input("Indica hasta donde quieres ver la cadena de caracteres: ")
    
        fragmented_string(sentence,min_range,max_range)
    else:
        print(f"La frase que envías no tiene la cantidad mínima de caracteres solicitada. Intenta nuevamente")



.. parsed-literal::

    Indica una frase u oración de mínimo 10 caracteres: Mi nombre es Cristian, soy programador y mi lenguaje favorito es Python
    La frase que envías tiene 71 caracteres
    Indica desde donde quieres ver la cadena de caracteres: 
    Indica hasta donde quieres ver la cadena de caracteres: 
    Mi nombre es Cristian, soy programador y mi lenguaje favorito es Python


Reto #5 Mayúsculas y minúsculas
-------------------------------

Solicita a tu usuario que indique 2 palabras, donde al mostrarlas en
pantalla una estará totalmente en mayúsculas y otra en minúsculas.

¿fácil, no?

.. code:: ipython3

    def transform_words(word1,word2):
        word1 = word1.upper()
        word2 = word2.lower()
        message = word1,word2
        return message
    
    word1 = input("Indica la primera palabra: ")
    word2 = input("Indica la segunda palabra: ")
    
    print(transform_words(word1,word2))


.. parsed-literal::

    Indica la primera palabra: hola
    Indica la segunda palabra: mundo
    ('HOLA', 'mundo')


Reto #6 Nombres cortos y largos
-------------------------------

-  Ya sabemos trabajar con nombres ¿pero qué pasa si cumple ciertas
   cualidades?

Tu usuario ingresará su nombre, si tiene una longitud mayor a 5
caracteres mostrarás un saludo con su nombre en pantalla. Si tiene menos
de 5 caracteres, pedirás su apellido, mostrarás el saludo con nombre y
apellido. En ambos casos deberás mostrarlos con mayúscula inicial.

.. code:: ipython3

    name = input("¿Cual es tu nombre?\n")
    
    if len(name) >= 5:
      print(f"Hola, {name.capitalize()}")
    else:
      lastname = input("¿Cual es tu apellido?\n")
      print(f"Hola, {name.capitalize()}, {lastname.capitalize()}")



.. parsed-literal::

    ¿Cual es tu nombre?
    Cristian
    Hola, Cristian


Reto #7 ¡Hablemos Pig Latin! (Puerco Latino) 🐷
----------------------------------------------

-  Solo una cosa, pide a tu usuario que ingrese una palabra y tradúcela
   a Pig Latin.

-  PuercoLatino es como el idioma de la “efe”, donde cambiamos las
   palabras bajo ciertas condiciones. En este caso será así:

-  La primer consonante de una palabra se pasa al final y se agrega la
   sílaba “ay”.

-  Si una palabra inicia con vocal, se agrega “way” al final.

Ejemplos:

::

   Platzi 👉 Latzipay
   Abeja 👉 Abejaway

.. code:: ipython3

    import re
    
    def pig_latin(word):
        if_vowel = "way"
        if_consonant = "ay"
        word_to_translate = word
        vowel = re.search("^[aeiouAEIOU]", word_to_translate)
    
        if vowel:
            final_word = word_to_translate + if_vowel
            print(final_word.capitalize())
        else:
            first_letter = word_to_translate[0]
            final_word = word_to_translate[1:] + first_letter + if_consonant
            print(final_word.capitalize())
    
    
    word = input("Dime una palabra y la convertiré en Pig Latin:\n")
    
    pig_latin(word)



.. parsed-literal::

    Dime una palabra y la convertiré en Pig Latin:
    gato
    Atogay

