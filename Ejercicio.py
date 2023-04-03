#Ejercicio Completo
class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def __str__(self):
        return "Color: " + str(self.color) + " Ruedas: "+ str(self.ruedas)
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super(). __init__(color,ruedas)
        self.velocidad= velocidad

    def __str__(self):
        return super().__str__() + " Velocidad km/h" + str(self.velocidad)
class Bicicleta(Vehiculo):
        def __init__(self, color, ruedas, tipo):
            super().__init__(color, ruedas)
            self.tipo = tipo

        def __str__(self):
            return super().__str__() + "Tipo: " + str(self.tipo)

vehiculo=Vehiculo("Azul",5)
coche=Coche("Blanco",6,100)
bicicleta=Bicicleta("Rojo",2,"Urbana")
print(vehiculo)
print(coche)
print(bicicleta)
