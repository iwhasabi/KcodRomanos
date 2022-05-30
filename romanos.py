def convertir_en_romano(numero):
    """
    Restricciones:
        - Es un número natural
        - El número está entre 0 y 3999
            - no es negativo
            - no es mayor que 3999
    Resultado es una cadena que contiene (I, v, X, L, C, D, M)

    ideas para comprobar un entero
        -isdigit()
    """
    if not isinstance(numero, int):
       return"no has introducido un número"
    if numero < 0 or numero > 3999:
        return "El número introducido no es válido (debe ser un número positivo y menos de 4000)"
    return "OK"

print(convertir_en_romano(-3))