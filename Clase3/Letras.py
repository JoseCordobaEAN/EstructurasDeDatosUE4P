def es_vocal(letra):
    """
    Decide si una letra es vocal

    >>> es_vocal('A')
    True
    >>> es_vocal('ae')
    False
    >>> es_vocal('Z')
    False
    >>> es_vocal('o')
    True

    :param letra:
    :return:
    """
    return len(letra) == 1 and letra in 'aeiouAEIOU'

def contar_vocales(texto):
    """
    Cuenta cuantas vocales hay en un texto


    >>> contar_vocales('')
    0
    >>> contar_vocales('hola')
    2
    >>> contar_vocales('qwrtp')
    0
    >>> contar_vocales('aeiou')
    5

    :param texto:
    :return:
    """
    contador = 0
    for letra in texto:
        if es_vocal(letra):
            contador += 1
    return contador