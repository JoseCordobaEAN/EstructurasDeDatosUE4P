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
        elemento = "prueba"

        lista = Lista_Encadenada(elemento) #Elemento queda agregado
        index_of_esperado = 0

        index_obtenido = lista.index_of(elemento)
        self.assertEquals(index_obtenido, index_of_esperado)

        for i in range (50):
            lista.agregar(f'Elemento {i}')
        index_of_esperado = 26

        index_obtenido = lista.index_of(f'Elemento {25}')
        self.assertEquals(index_obtenido, index_of_esperado)

        index_of_esperado = -1
        index_obtenido = lista.index_of('Miller')
        self.assertEquals(index_obtenido, index_of_esperado)

    def test_elemento_en(self):
        self.fail()
