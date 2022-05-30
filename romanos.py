def convertir_en_romano(numero):
    """
    Restricciones:
        - Es un número natural
        - El número está entre 0 y 3999
            - no es negativo
            - no es mayor que 3999
    Resultado es una cadena que contiene (I, v, X, L, C, D, M)

    """
    if not isinstance(numero, int):
       return"no has introducido un número"
    if numero < 0 or numero > 3999:
        return "El número introducido no es válido (debe ser un número positivo y menos de 4000)"

    # continuamos la conversión
    simbolos = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    return "OK"

    # Descomponer en unidades, decenas, centenas y unidades de millar
    # Opcion 1: división entera + modulo en cascada
    # Opción 2: convertir en cadena y en función de la longitud y la posición obtener u,d,c y um 

print(convertir_en_romano(-3))
print(convertir_en_romano(33333))
print(convertir_en_romano(253))