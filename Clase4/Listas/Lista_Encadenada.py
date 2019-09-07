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

    def agregar(self, Elemento):
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
        super().quitar(Elemento)

    def editar(self, index, Elemento):
        super().editar(index, Elemento)

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

    def __init__(self):
        self.Primero = None
        self.tamano = 0

    def __init__(self, elemento) -> None:
        super().__init__()
        self.Primero = Nodo(elemento, None)
        self.tamano += 1

    def __repr__(self) -> str:
        return super().__repr__()