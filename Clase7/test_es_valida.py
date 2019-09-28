from unittest import TestCase
from Clase7.analizador_de_expresiones import es_valida

class TestEs_valida(TestCase):

    def test_es_valida_caso_regular(self):
        expresion_de_prueba = '( a * b )'
        self.assertTrue(es_valida(expresion_de_prueba))
        expresion_de_prueba = '( ( ax % yb ) )'
        self.assertTrue(es_valida(expresion_de_prueba))
        expresion_de_prueba = '[ ( aaz + zbb ) ]'
        self.assertTrue(es_valida(expresion_de_prueba))
        expresion_de_prueba = '{ [ aafp / pwbb ] }'
        self.assertTrue(es_valida(expresion_de_prueba))
        expresion_de_prueba = 'a + b + c'
        self.assertTrue(es_valida(expresion_de_prueba))
        expresion_de_prueba = 'a '
        self.assertTrue(es_valida(expresion_de_prueba))


    def test_es_valida_caso_dos_variables(self):
        expresion_de_prueba = 'a b'
        self.assertFalse(es_valida(expresion_de_prueba))
        expresion_de_prueba = 'xx yy'
        self.assertFalse(es_valida(expresion_de_prueba))

    def test_es_valida_caso_dos_operadores(self):
        expresion_de_prueba = '* +'
        print(f'probando {expresion_de_prueba}')
        self.assertFalse(es_valida(expresion_de_prueba))
        expresion_de_prueba = '% /'
        print(f'probando {expresion_de_prueba}')
        self.assertFalse(es_valida(expresion_de_prueba))

    def test_es_valida_caso_parentesis_no_balanceados(self):
        expresion_de_prueba = '( ( ( ) } )'
        self.assertFalse(es_valida(expresion_de_prueba))
        expresion_de_prueba = '( ( ( ] ] )'
        self.assertFalse(es_valida(expresion_de_prueba))

    def test_es_valida_caso_parentesis_sobrante(self):
        expresion_de_prueba = ')'
        self.assertFalse(es_valida(expresion_de_prueba))
        expresion_de_prueba = '('
        self.assertFalse(es_valida(expresion_de_prueba))