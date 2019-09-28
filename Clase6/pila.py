class Nodo:

    elemento = None
    Siguiente = None

    def __init__(self, elemento, siguiente):
        self.elemento = elemento
        self.Siguiente = siguiente

class Pila:

    tamano = 0
    top = None

    def apilar(self, elemento):
        """
        Agrega un elemento al tope de la pila

        :param elemento: Cualquier elemento
        :return: None
        """
        nuevo_nodo = Nodo(elemento, self.top)
        self.top = nuevo_nodo
        self.tamano += 1

    def desapilar(self):
        """
        Retorna el elemento del Tope de la pila y lo elimina
        :return: El elemento del tope de la pila
        """
        if self.tamano > 0:
            elemento_auxiliar = self.top.elemento
            self.top = self.top.Siguiente
            self.tamano -= 1
            return elemento_auxiliar
        raise IndexError('La pila esta vacía')


    def mirar(self):
        """
        Ve el elemento del tope de la pila sin eliminarlo
        :return: El elemento del tope de la pila
        """
        return self.top.elemento

    def es_vacia(self):
        return self.tamano == 0

    def invertir(self):
        auxiliar = Pila()
        nodo_auxiliar = self.top
        for i in range(self.tamano):
            auxiliar.apilar(nodo_auxiliar.elemento)
            nodo_auxiliar = nodo_auxiliar.Siguiente
        return auxiliar

    def copiar(self):
        return self.invertir().invertir()

    def __repr__(self):
        resultado = []
        auxiliar = self
        while not auxiliar.es_vacia():
            resultado.append(auxiliar.desapilar())
        resultado.reverse()
        return str(resultado)
