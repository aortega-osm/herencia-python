class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas

    def __str__(self):
        return "Color: " + str(self.color) + " Ruedas: "+ str(self.ruedas)

vehiculo= Vehiculo ("Azul" , 4)
print(vehiculo)










