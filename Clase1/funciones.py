def division(divendo, divisor):
    return divendo / divisor

def division_entera(divendo, divisor):
    return divendo // divisor

def es_vocal(letra):
    """
    La funcion es vocal determina si una letra es vocal

    >>> es_vocal('A')
    True
    >>> es_vocal('e')
    True
    >>> es_vocal('Z')
    False
    >>> es_vocal('io')
    False

    :param letra: string de longitud 1
    :return: True si es una vocal False de lo contrario
    """
    return len(letra) ==1 and letra in 'AEIOUaeiou'