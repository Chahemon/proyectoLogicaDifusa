import Funciones

# Clase para crear objetos temperatura, con su respectivas membresias.
class Temperatura:
    def __init__(self, temperatura):
        self.tem_muy_baja = 0
        self.tem_fria = 0
        self.templado = 0
        self.tem_caliente = 0
        self.tem_muy_caliente = 0
        if -10 <= temperatura <= 45:
            self.tem_muy_baja = Funciones.trapezoidal(temperatura, -10, -10, 0, 5)
            self.tem_fria = Funciones.triangular(temperatura, 0, 7.5, 15)
            self.templado = Funciones.triangular(temperatura, 10, 17.5, 25)
            self.tem_caliente = Funciones.triangular(temperatura, 20, 27.5, 35)
            self.tem_muy_caliente = Funciones.trapezoidal(temperatura, 30, 35, 45, 45)



