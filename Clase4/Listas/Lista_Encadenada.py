from Listas.ListaAbstracta import ListaAbstracta


class Nodo:
    """
    Representa un nodo para la lista encadenada
    """

    elemento = None
    siguiente = None

    def __init__(self, elemento, siguiente):
        self.elemento = elemento
        self.siguiente = siguiente

class Lista_Encadenada(ListaAbstracta):

    Primero = None
    tamano = 0

    def agregar(self, Elemento):
        """
        O(n)
        :param Elemento:
        :return:
        """
        nuevo = Nodo(Elemento, None)
        ultimo_nodo = self.Primero
        if self.tamano == 0:
            self.Primero = nuevo
        else:
            while ultimo_nodo.siguiente != None:
                ultimo_nodo = ultimo_nodo.siguiente
            ultimo_nodo.siguiente = nuevo
        self.tamano += 1


    def quitar(self, Elemento):
        anterior = None
        auxiliar = self.Primero
        while auxiliar != None:
            siguiente = auxiliar.siguiente
            if auxiliar.elemento == Elemento:
                anterior.siguiente = siguiente
                self.tamano -=1
                return auxiliar.elemento
            anterior = auxiliar
            auxiliar = siguiente


    def editar(self, index, Elemento):
        if index >= self.tamano:
            raise IndexError(f'{index} esta fuera del rango de la lista')
        aux = self.Primero
        for i in range (index):
            aux = aux.siguiente
        aux.elemento = Elemento

    def index_of(self, Elemento):
        index_var = -1

        nodo_index = self.Primero
        for i in range (self.tamano):
            if nodo_index.elemento == Elemento:
                index_var = i
                return index_var
            else:
                nodo_index = nodo_index.siguiente
        return index_var

    def elemento_en(self, index):
        if index >= self.tamano:
            raise IndexError(f'{index} esta fuera del rango de la lista')
        nodo_buscado = self.Primero
        for i in range(index):
            nodo_buscado = nodo_buscado.siguiente
        return nodo_buscado.elemento


    def __init__(self, elemento = None):
        if elemento != None:
            self.Primero = Nodo(elemento, None)
            self.tamano += 1

    def __repr__(self):
        lista_rep = []
        aux = self.Primero
        while aux != None:
            lista_rep.append(aux.elemento)
            aux = aux.siguiente
        return lista_rep