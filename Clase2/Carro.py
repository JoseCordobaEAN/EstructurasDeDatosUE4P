from Vehiculo import Vehiculo

class Carro(Vehiculo):

    ruedas = 4
    repuesto = True

    def __init__(self, nombre, color, energia):
        super(Carro, self).__init__(nombre, 4, energia, color)

    def reversa(self, cantidad):
        if cantidad <= self.energia:
            print(f'Retrocedemos {cantidad} unidades')
            self.energia -= cantidad
        else:
            raise Exception(f'El carro {self.nombre} no tiene energía para '
                            f'retroceder {cantidad}')
