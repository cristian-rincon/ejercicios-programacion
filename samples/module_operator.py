

def operador_modulo(numero_1,numero_2):
    """Este ejemplo explica cómo usar el operador módulo % .
    """

    return numero_1 % numero_2


if __name__ == "__main__":
    numero_1 = int(input("Ingresa el divisor: "))
    numero_2 = int(input("Ingresa el dividendo: "))
    resultado = operador_modulo(numero_1, numero_2)
    print(f"El sobrante de dividir {numero_1} sobre {numero_2} es: {resultado}")