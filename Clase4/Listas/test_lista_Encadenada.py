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

    def test_quitar_longitud(self):
        lista = Lista_Encadenada()
        for i in range(5):
            lista.agregar(i)
        lista.quitar(3)

        longitud_esperada = 4
        longitud_real = lista.tamano
        self.assertEquals(longitud_esperada, longitud_real)


    def test_quitar_indice(self):
        lista = Lista_Encadenada()
        for i in range(5):
            lista.agregar(i)
        lista.quitar(3)

        indice_esperado = -1
        indice_real = lista.index_of(3)
        self.assertEquals(indice_esperado, indice_real)

    def test_quitar_elemento(self):
        lista = Lista_Encadenada()
        for i in range(5):
            lista.agregar(i)

        elemento_esperado = 3
        elemento_real = lista.quitar(3)
        self.assertEquals(elemento_esperado, elemento_real)

    def test_quitar_enlace(self):
        lista = Lista_Encadenada()
        for i in range(5):
            lista.agregar(i)
        lista.quitar(3)

        indice_esperado = 3
        indice_real = lista.index_of(4)
        self.assertEquals(indice_esperado, indice_real)

    def test_quitar_vacia(self):
        lista = Lista_Encadenada()
        lista.quitar(3)

        indice_esperado = -1
        indice_real = lista.index_of(4)
        self.assertEquals(indice_esperado, indice_real)

    def test_rep(self):
        lista = Lista_Encadenada()
        for i in range(5):
            lista.agregar(i)

        lista_esperada = [0, 1, 2, 3, 4]
        lista_real = lista.__repr__()
        self.assertEquals(lista_esperada, lista_real)

    def test_editar(self):
        lista = Lista_Encadenada()
        for i in range(5):
            lista.agregar(i)

        nuevo_elemento = 10
        indice = 3
        lista.editar(indice, nuevo_elemento)
        elemento_real = lista.elemento_en(indice)
        self.assertEquals(elemento_real, nuevo_elemento)

    def test_editar_error(self):
        lista = Lista_Encadenada()
        for i in range(5):
            lista.agregar(i)

        nuevo_elemento = 10
        indice = 30
        self.assertRaises(IndexError,lista.editar, indice, nuevo_elemento)



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
        lista = Lista_Encadenada()
        for i in range(1000):
            lista.agregar(i)

        elemento_esperado = 200
        elemento_real = lista.elemento_en(200)
        self.assertEquals(elemento_esperado, elemento_real)

    def test_elemento_en_error(self):
        lista = Lista_Encadenada()
        for i in range(10):
            lista.agregar(i)

        indice_prueba =100
        self.assertRaises(IndexError,lista.elemento_en, indice_prueba)
