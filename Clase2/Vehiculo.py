class Vehiculo:

    color = ""
    ruedas = 0
    energia = 0
    nombre = ""

    def __init__(self, nombre, ruedas, energia, color):
        self.nombre = nombre
        self.ruedas = ruedas
        self.energia = energia
        self.color = color

    def __repr__(self):
        return f'Este es un vehiculo llamado {self.nombre}' \
               f' de color {self.color} ' \
               f'tiene {self.ruedas} ruedas ' \
               f'y {self.energia} energia'

    def __eq__(self, other):
        return self.nombre == other.nombre \
               and self.color == other.color \
               and self.ruedas == other.ruedas \
               and self.energia == other.energia


    def mover(self, cantidad):
        if cantidad <= self.energia:
            print(f'El vehiculo {self.nombre} se mueve {cantidad}')
            self.energia -= cantidad
        else:
            raise Exception(f'El vehiculo {self.nombre} no tiene energía para '
                            f'moverse {cantidad}')

    def tanquear(self, cantidad):
        if cantidad > 0:
            self.energia += cantidad
        else:
            raise Exception(f'No puede tanquear con {cantidad}')
