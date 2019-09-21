from unittest import TestCase
from Clase6.pila import Pila


class TestPila(TestCase):

    def test_apilar_tamano(self):
        tamano_esperado = 13
        pila_pruebas = Pila()
        for i in range(13):
            pila_pruebas.apilar(f'elemento {i}')
        tamano_real = pila_pruebas.tamano
        self.assertEqual(tamano_esperado, tamano_real)

    def test_apilar(self):
        elemento_esperado = f'elemento {12}'
        pila_pruebas = Pila()
        for i in range(13):
            pila_pruebas.apilar(f'elemento {i}')
        elemento_real = pila_pruebas.mirar()
        self.assertEqual(elemento_esperado, elemento_real)

    def test_desapilar_tamano(self):
        tamano_esperado = 10
        pila_pruebas = Pila()
        for i in range(13):
            pila_pruebas.apilar(f'elemento {i}')
        for i in range(3):
            pila_pruebas.desapilar()
        tamano_real = pila_pruebas.tamano
        self.assertEqual(tamano_esperado, tamano_real)

    def test_desapilar_vacia(self):
        pila_pruebas = Pila()
        self.assertRaises(IndexError, pila_pruebas.desapilar)

    def test_desapilar(self):
        elemento_esperado = f'elemento {10}'
        pila_pruebas = Pila()
        for i in range(13):
            pila_pruebas.apilar(f'elemento {i}')
        for i in range(3):
            elemento_real = pila_pruebas.desapilar()
        self.assertEqual(elemento_esperado, elemento_real)

    def test_mirar(self):
        elemento_esperado = False
        pila_pruebas = Pila()
        pila_pruebas.apilar(73)
        pila_pruebas.apilar('Hola')
        pila_pruebas.apilar(False)
        elemento_real = pila_pruebas.mirar()
        self.assertEqual(elemento_esperado, elemento_real)

    def test_es_vacia(self):
        pila_pruebas = Pila()
        self.assertTrue(pila_pruebas.es_vacia())
        pila_pruebas.apilar('hola')
        self.assertFalse(pila_pruebas.es_vacia())

    def test_invertir(self):
        mi_pila = Pila()
        mi_pila.apilar('hola')
        mi_pila.apilar(73)
        mi_pila.apilar(True)

        invertida = mi_pila.invertir()
        representacion_esperada = ['hola', 73, True]
        self.assertEqual(representacion_esperada, invertida.__repr__())


    def test_copiar(self):
        self.fail()
