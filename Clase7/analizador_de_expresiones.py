from Clase6.pila import Pila as P

parentesis_apertura = '([{'
parentesis_cierre = ')]}'
operadores = '+-*/%'

def es_parentesis(token):
    return len(token) == 1 and \
           (token in parentesis_apertura
            or token in parentesis_cierre)

def es_parentesis_apertura(token):
    return len(token) == 1 and \
           token in parentesis_apertura

def es_parentesis_cierre(token):
    return len(token) == 1 and \
            token in parentesis_cierre

def corresponden(p1, p2):
    return parentesis_apertura.index(p1) == parentesis_cierre.index(p2)

def es_operador(token):
    return len(token) == 1 and token in operadores


def es_valida(expresion):
    """
    Analiza si una expresión matematica es valida

    >>> es_valida('( a + b )')
    True
    >>> es_valida(' x x + )')
    False

    :param expresion: Una expresión donde operadores y operandos están
    separados por espacios en blanco ' '
    :return: True si la expresión es valida False de lo contrario
    """
    tokens = expresion.split()
    pila_parentesis = P()
    ultimo_operador = None
    variables = None

    for token in tokens:
        if es_parentesis_apertura(token):
            pila_parentesis.apilar(token)
        elif es_parentesis_cierre(token):
            if pila_parentesis.es_vacia()\
                    or not corresponden(pila_parentesis.desapilar(), token):
                return False
        elif es_operador(token):
            if ultimo_operador == None :
                ultimo_operador = token
                variables = None
            else:
                return False
        else:
            if variables == None:
                ultimo_operador = None
                variables = token
            else:
                return False

    return pila_parentesis.es_vacia()
