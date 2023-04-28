import Funciones


class Humedad:
    def __init__(self, humedad):
        self.seco = 0
        self.humedo = 0
        self.muy_humedo = 0
        if 0 <= humedad <= 100:
            self.seco = Funciones.triangular(humedad, 0, 0, 5)
            self.humedo = Funciones.trapezoidal(humedad, 0.4, 20, 55, 70)
            self.muy_humedo = Funciones.trapezoidal(humedad, 60, 75, 100, 100)

