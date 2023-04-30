# Base logica para determinar la salida

def determinar_regla(humedad, temperatura):
    resultado = []

    # Regla 1
    # if temperatura == "muy_fria" and humedad == "seco":
    if temperatura[0] > 0 and humedad[0] > 0:
        resultado.append([1, ["nada", 1], "temprano"])

    # Regla 2
    # if temperatura == "muy_fria" and humedad == "seco":
    if temperatura[0] > 0 and humedad[0] > 0:
        resultado.append([2, ["nada", 1], "noche"])

    # Regla 3
    # if temperatura == "fria" and humedad == "seco":
    if temperatura[1] > 0 and humedad[0] > 0:
        resultado.append([3, ["moderado", min(humedad[0], temperatura[1])], "temprano"])

    # Regla 4
    # if temperatura == "fria" and humedad == "seco":
    if temperatura[1] > 0 and humedad[0] > 0:
        resultado.append([4, ["nada", 1], "noche"])

    # Regla 5
    # if temperatura == "templado" and humedad == "seco":
    if temperatura[2] > 0 and humedad[0] > 0:
        resultado.append([5, ["moderado", min(humedad[0], temperatura[2])], "temprano"])

    # Regla 6
    # if temperatura == "templado" and humedad == "seco":
    if temperatura[2] > 0 and humedad[0] > 0:
        resultado.append([6, ["moderado", min(humedad[0], temperatura[2])], "noche"])

    # Regla 7
    # if temperatura == "caliente" and humedad == "seco":
    if temperatura[3] > 0 and humedad[0] > 0:
        resultado.append([7, ["mucho", min(humedad[0], temperatura[3])], "temprano"])

    # Regla 8
    # if temperatura == "caliente" and humedad == "seco":
    if temperatura[3] > 0 and humedad[0] > 0:
        resultado.append([8, ["mucho", min(humedad[0], temperatura[3])], "noche"])

    # Regla 9
    # if temperatura == "muy_caliente" and humedad == "seco":
    if temperatura[4] > 0 and humedad[0] > 0:
        resultado.append([9, ["mucho", min(humedad[0], temperatura[4])], "temprano"])

    # Regla 10
    # if temperatura == "muy_caliente" and humedad == "seco":
    if temperatura[4] > 0 and humedad[0] > 0:
        resultado.append([10, ["mucho", min(humedad[0], temperatura[4])], "noche"])

    # Regla 11
    # if temperatura == "fria" and humedad == "humedo":
    if temperatura[1] > 0 and humedad[1] > 0:
        resultado.append([11, ["nada", 1], "temprano"])

    # Regla 12
    # if temperatura == "fria" and humedad == "humedo":
    if temperatura[1] > 0 and humedad[1] > 0:
        resultado.append([12, ["nada", 1], "noche"])

    # Regla 13
    # if temperatura == "muy_fria" and humedad == "humedo":
    if temperatura[0] > 0 and humedad[1] > 0:
        resultado.append([13, ["nada", 1], "temprano"])

    # Regla 14
    # if temperatura == "muy_fria" and humedad == "humedo":
    if temperatura[0] > 0 and humedad[1] > 0:
        resultado.append([14, ["nada", 1], "temprano"])

    # Regla 15
    # if temperatura == "templado" and humedad == "humedo":
    if temperatura[2] > 0 and humedad[1] > 0:
        resultado.append([15, ["moderado", min(humedad[1], temperatura[2])], "temprano"])

    # Regla 16
    # if temperatura == "templado" and humedad == "humedo":
    if temperatura[2] > 0 and humedad[1] > 0:
        resultado.append([16, ["nada", 1], "noche"])

    # Regla 17
    # if temperatura == "caliente" and humedad == "humedo":
    if temperatura[3] > 0 and humedad[1] > 0:
        resultado.append([17, ["moderado", min(humedad[1], temperatura[3])], "temprano"])

    # Regla 18
    # if temperatura == "caliente" and humedad == "humedo":
    if temperatura[3] > 0 and humedad[1] > 0:
        resultado.append([18, ["moderado", min(humedad[1], temperatura[3])], "noche"])

    # Regla 19
    # if temperatura == "muy_caliente" and humedad == "humedo":
    if temperatura[4] > 0 and humedad[1] > 0:
        resultado.append([19, ["moderado", min(humedad[1], temperatura[4])], "temprano"])

    # Regla 20
    # if temperatura == "muy_caliente" and humedad == "humedo":
    if temperatura[4] > 0 and humedad[1] > 0:
        resultado.append([20, ["moderado", min(humedad[1], temperatura[4])], "noche"])

    # Regla 21
    # if temperatura == "muy_fria" and humedad == "muy_humedo":
    if temperatura[0] > 0 and humedad[2] > 0:
        resultado.append([21, ["nada", 1], "temprano"])

    # Regla 22
    # if temperatura == "muy_fria" and humedad == "muy_humedo":
    if temperatura[0] > 0 and humedad[2] > 0:
        resultado.append([22, ["nada", 1], "noche"])

    # Regla 23
    # if temperatura == "fria" and humedad == "muy_humedo":
    if temperatura[1] > 0 and humedad[2] > 0:
        resultado.append([23, ["nada", 1], "temprano"])

    # Regla 24
    # if temperatura == "fria" and humedad == "muy_humedo":
    if temperatura[1] > 0 and humedad[2] > 0:
        resultado.append([24, ["nada", 1], "noche"])

    # Regla 25
    # if temperatura == "templado" and humedad == "muy_humedo":
    if temperatura[2] > 0 and humedad[2] > 0:
        resultado.append([25, ["nada", 1], "temprano"])

    # Regla 26
    # if temperatura == "templado" and humedad == "muy_humedo":
    if temperatura[2] > 0 and humedad[2] > 0:
        resultado.append([26, ["nada", 1], "noche"])

    # Regla 27
    # if temperatura == "caliente" and humedad == "muy_humedo":
    if temperatura[3] > 0 and humedad[2] > 0:
        resultado.append([27, ["moderado", min(humedad[2], temperatura[3])], "temprano"])

    # Regla 28
    # if temperatura == "caliente" and humedad == "muy_humedo":
    if temperatura[3] > 0 and humedad[2] > 0:
        resultado.append([28, ["nada", 1], "noche"])

    # Regla 29
    # if temperatura == "muy_caliente" and humedad == "muy_humedo":
    if temperatura[4] > 0 and humedad[2] > 0:
        resultado.append([29, ["moderado", min(humedad[2], temperatura[4])], "temprano"])

    # Regla 30
    # if temperatura == "muy_caliente" and humedad == "muy_humedo":
    if temperatura[4] > 0 and humedad[2] > 0:
        resultado.append([30, ["nada", 1], "noche"])

    return resultado


# Función de defuzzificación
def defuzzificacion_centroide(membresias, valores):
    # Calcula el centro de masa ponderado
    numerador = sum(membresias[i] * valores[i] for i in range(len(membresias)))
    denominador = sum(membresias)
    if denominador > 0:
        centroide = numerador / denominador
    else:
        centroide = 0

    return centroide
