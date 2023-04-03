from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo=tipo

    def __str__(self):
        return super().__str__() + "Tipo: " + str(self.tipo)

bicicleta=Bicicleta("Blanca",2,"BMX")
print(bicicleta)