"""
Reto #3 "Mensaje multilínea"
=============================

.. note::  
    
    Instrucciones: seguro has visto que en Platzi 
    hay más de 600 cursos ¿puedes mostrar a que 
    categorías corresponden en una sola línea de código?
    Debe mostrarse así:

.. code-block:: python

    Platzi cuenta con cursos de:
    [categoría1]
    [categoría2]
    [categoría3]
    [categoría4]
    [categoría5]
    [categoría6]

"""


def multiline_message():
    """Toma las categorías desde una lista y las imprime en pantalla al usuario
    final."""

    categories = [
        "Desarrollo e Ingeniería",
        "Diseño y Ux",
        "Marketing",
        "Negocios y Emprendimiento",
        "Producción Audiovisual",
        "Crecimiento Profesional",
    ]

    print("Platzi cuenta con cursos de:\n")
    for category in categories:
        print(f"- {category}")


if __name__ == "__main__":
    multiline_message()
