from Clase6.pila import Pila

mi_pila = Pila()
mi_pila.apilar('hola')
mi_pila.apilar(73)
mi_pila.apilar(True)

print(mi_pila.invertir())
print(mi_pila)