import base_logica
from humedad import *
from temperatura import *
from base_logica import *

print("\nLOGICA DIFUSA - PROYECTO")
# Ingresamos los valores de entrada
humedad_valor = float(input("Ingrese la humedad: "))
temperatura_valor = float(input("Ingrese la Temperatura: "))

# Creamos el objeto que calculara internamente los grados de membresía de cada uno de ellos.
humedad_obj = Humedad(humedad_valor)
temperatura_obj = Temperatura(temperatura_valor)

print("\n---------------------------------------------------------------------------------------")

# Mostramos los valores obtenidos de membresía
print("MEMBRESIA DE HUMEDAD : (Seco - " + str(humedad_obj.seco) + ") (Humedo - " + str(humedad_obj.humedo) + ") (Muy Humedo - " +
      str(humedad_obj.muy_humedo) + ").")
print("MEMBRESIA DE TEMPERATURA : (Muy Fria - " + str(temperatura_obj.tem_muy_baja) + ") (Fria - " + str(temperatura_obj.tem_fria) + ") (Templada - " +
      str(temperatura_obj.templado) + ") (Caliente - " + str(temperatura_obj.tem_caliente) + ") (Muy Caliente - " + str(temperatura_obj.tem_muy_caliente) + ").")

# Creamos una lista con los valores para poder usarlos en el calculo de las reglas
humedad_lista = [humedad_obj.seco, humedad_obj.humedo, humedad_obj.muy_humedo]
temperatura_lista = [temperatura_obj.tem_muy_baja, temperatura_obj.tem_fria, temperatura_obj.templado, temperatura_obj.tem_caliente, temperatura_obj.tem_muy_caliente]

# Verificamos cuáles reglas aplican y cuáles no, y las guardamos en una variable.
resultado_parcial = (base_logica.determinar_regla(humedad_lista, temperatura_lista))

print("---------------------------------------------------------------------------------------")

max_nada = 0
max_moderado = 0
max_mucho = 0

# Recorremos los resultados para calcular la pertenencia más alta y usarla para calcular la defuzzificacion.
for actual in resultado_parcial:
    if actual[1][0] == "nada":
        max_nada = max(max_nada, actual[1][1])

    if actual[1][0] == "moderado":
        max_moderado = max(max_moderado, actual[1][1])

    if actual[1][0] == "mucho":
        max_mucho = max(max_mucho, actual[1][1])

# Hacemos la lista con las membresía y los valores.

# Puntos claves de la función de tiempo, que usaremos para calcular la defuzzificación
lista_membresias = [0, max_moderado, max_moderado, 0, 0, max_mucho, max_mucho, 0]
lista_valores = [0.1, 0.1, 5.0, 5.0, 5.01, 5.01, 10, 10]

# Usamos el metodo para calcular el tiempo
defuzzificacion_tiempo = base_logica.defuzzificacion_centroide(lista_membresias, lista_valores)

print("\n==============================================")
print("| Regla  | Tiempo de Riego   | Hora          |")
print("==============================================")

# Imprimimos los resultados obtenidos con el respectivo tiempo.
for actual in resultado_parcial:
    print("|\t" + str(actual[0]) + "\t | \t" + str("Nada  \t\t\t | " if actual[1][0] == "nada"
            else (str(defuzzificacion_tiempo) + " Minutos\t | ")) + str(actual[2]) + "\t\t |")

print("==============================================")

