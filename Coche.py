from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super(). __init__(color,ruedas)
        self.velocidad= velocidad

    def __str__(self):
        return super().__str__() + " Velocidad km/h" + str(self.velocidad)


coche=Coche("Verde",4,90)
print(coche)