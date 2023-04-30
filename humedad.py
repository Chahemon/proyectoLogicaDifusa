import Funciones

# Clase para crear objetos humedad, con su respectivas membresia.
class Humedad:
    def __init__(self, humedad):
        self.seco = 0
        self.humedo = 0
        self.muy_humedo = 0
        if 0 <= humedad <= 100:
            self.seco = Funciones.triangular(humedad, 0, 0, 5)
            self.humedo = Funciones.trapezoidal(humedad, 3, 20, 54, 70)
            self.muy_humedo = Funciones.trapezoidal(humedad, 60, 77, 100, 100)

