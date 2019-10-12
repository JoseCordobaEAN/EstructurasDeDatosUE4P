from ArbolAbstracto import ArbolAbstracto


class ArbolBinario(ArbolAbstracto):
    class Nodo:
        """
        Representa un nodo en el arbol binario
        """
        elemento = None
        izquierda = None
        derecha = None
        padre = None

        def __init__(self, elemento, padre=None, iz=None, der=None ):
            self.elemento = elemento
            self.izquierda = iz
            self.derecha = der
            self.padre = padre

        def es_hoja(self):
            return self.izquierda is None and self.derecha is None

        def es_rama(self):
            return not self.es_hoja()

        def es_raiz(self):
            return self.padre is None

        def tiene_izquierda(self):
            return self.izquierda is not None

        def tiene_derecha(self):
            return self.derecha is not None

        @property
        def altura(self):
            if self.es_raiz():
                return 0
            return 1 + self.padre.altura()

        @property
        def profundidad(self):
            if self.es_hoja():
                return 0
            p_iz = self.izquierda.profundidad if self.izquierda is not None else 0
            p_d = self.derecha.profundidad if self.derecha is not None else 0
            return 1 + p_iz if p_iz > p_d else p_d

    raiz = None
    tamano = 0

    def __init__(self, elemento=None):
        if elemento is not None:
            self.raiz = self.Nodo(elemento)
            self.tamano += 1

    def profundidad(self):
        return self.raiz.profundidad()

    def es_vacio(self):
        return self.raiz is None

    def raiz(self):
        return self.raiz

    def insertar(self, elemento, nodo=None):
        self.tamano += 1
        if self.es_vacio():
            self.raiz = self.Nodo(elemento)
        if nodo is None:
            raiz = self.raiz
            if not self.raiz.tiene_izquierda():
                raiz.izquierda = self.Nodo(elemento, raiz)
            elif not self.raiz.tiene_derecha():
                raiz.derecha = self.Nodo(elemento, raiz)



    def __repr__(self):
        return f'Arbol binario de tamaño {self.tamano}'
