from unittest import TestCase
from Listas.Lista_Encadenada import Lista_Encadenada


class TestLista_Encadenada(TestCase):

    def test_agregar(self):
        elemento = "Hola mundo"
        tamano_esperado = 11

        lista = Lista_Encadenada(elemento)
        for i in range(10):
            lista.agregar(elemento)
        self.assertEquals(lista.tamano, tamano_esperado)

        elemento_recibido = lista.elemento_en(10)
        self.assertEquals(elemento, elemento_recibido)

        self.assertRaises(IndexError, lista.elemento_en, 11)

    def test_quitar(self):
        self.fail()

    def test_editar(self):
        self.fail()

    def test_index_of(self):
        self.fail()

    def test_elemento_en(self):
        self.fail()
