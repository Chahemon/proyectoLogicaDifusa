# Base logica para determinar la salida

def determinar_regla(humedad, temperatura):
    tiempo = []
    hora = []
    regla = []

    # Regla 1
    if temperatura == "muy_fria" and humedad == "seco":
        tiempo.append("_")
        hora.append("temprano")
        regla.append(1)

    # Regla 2
    if temperatura == "muy_fria" and humedad == "seco":
        tiempo.append("_")
        hora.append("noche")
        regla.append(2)

    # Regla 3
    if temperatura == "fria" and humedad == "seco":
        tiempo.append("moderado")
        hora.append("temprano")
        regla.append(3)

    # Regla 4
    if temperatura == "fria" and humedad == "seco":
        tiempo.append("_")
        hora.append("temprano")
        regla.append(4)

    # Regla 5
    if temperatura == "templado" and humedad == "seco":
        tiempo.append("moderado")
        hora.append("temprano")
        regla.append(5)

    # Regla 6
    if temperatura == "templado" and humedad == "seco":
        tiempo.append("moderado")
        hora.append("noche")
        regla.append(6)

    # Regla 7
    if temperatura == "caliente" and humedad == "seco":
        tiempo.append("mucho")
        hora.append("temprano")
        regla.append(7)

    # Regla 8
    if temperatura == "caliente" and humedad == "seco":
        tiempo.append("mucho")
        hora.append("noche")
        regla.append(8)

    # Regla 9
    if temperatura == "muy_caliente" and humedad == "seco":
        tiempo.append("mucho")
        hora.append("temprano")
        regla.append(9)

    # Regla 10
    if temperatura == "muy_caliente" and humedad == "seco":
        tiempo.append("mucho")
        hora.append("noche")
        regla.append(10)

    # Regla 11
    if temperatura == "fria" and humedad == "humedo":
        tiempo.append("_")
        hora.append("temprano")
        regla.append(11)

    # Regla 12
    if temperatura == "fria" and humedad == "humedo":
        tiempo.append("_")
        hora.append("noche")
        regla.append(12)

    # Regla 13
    if temperatura == "muy_fria" and humedad == "humedo":
        tiempo.append("_")
        hora.append("temprano")
        regla.append(13)

    # Regla 14
    if temperatura == "muy_fria" and humedad == "humedo":
        tiempo.append("_")
        hora.append("temprano")
        regla.append(14)

    # Regla 15
    if temperatura == "templado" and humedad == "humedo":
        tiempo.append("moderado")
        hora.append("temprano")
        regla.append(15)

    # Regla 16
    if temperatura == "templado" and humedad == "humedo":
        tiempo.append("_")
        hora.append("noche")
        regla.append(16)

    # Regla 17
    if temperatura == "caliente" and humedad == "humedo":
        tiempo.append("moderado")
        hora.append("temprano")
        regla.append(17)

    # Regla 18
    if temperatura == "caliente" and humedad == "humedo":
        tiempo.append("moderado")
        hora.append("noche")
        regla.append(18)

    # Regla 19
    if temperatura == "muy_caliente" and humedad == "humedo":
        tiempo.append("moderado")
        hora.append("temprano")
        regla.append(19)

    # Regla 20
    if temperatura == "muy_caliente" and humedad == "humedo":
        tiempo.append("moderado")
        hora.append("noche")
        regla.append(20)

    # Regla 21
    if temperatura == "muy_fria" and humedad == "muy_humedo":
        tiempo.append("_")
        hora.append("temprano")
        regla.append(21)

    # Regla 22
    if temperatura == "muy_fria" and humedad == "muy_humedo":
        tiempo.append("_")
        hora.append("noche")
        regla.append(22)

    # Regla 23
    if temperatura == "fria" and humedad == "muy_humedo":
        tiempo.append("_")
        hora.append("temprano")
        regla.append(23)

    # Regla 24
    if temperatura == "fria" and humedad == "muy_humedo":
        tiempo.append("_")
        hora.append("noche")
        regla.append(24)

    # Regla 25
    if temperatura == "templado" and humedad == "muy_humedo":
        tiempo.append("_")
        hora.append("temprano")
        regla.append(25)

    # Regla 26
    if temperatura == "templado" and humedad == "muy_humedo":
        tiempo.append("_")
        hora.append("noche")
        regla.append(26)

    # Regla 27
    if temperatura == "caliente" and humedad == "muy_humedo":
        tiempo.append("moderado")
        hora.append("temprano")
        regla.append(27)

    # Regla 28
    if temperatura == "caliente" and humedad == "muy_humedo":
        tiempo.append("_")
        hora.append("noche")
        regla.append(28)

    # Regla 29
    if temperatura == "muy_caliente" and humedad == "muy_humedo":
        tiempo.append("moderado")
        hora.append("temprano")
        regla.append(29)

    # Regla 30
    if temperatura == "muy_caliente" and humedad == "muy_humedo":
        tiempo.append("_")
        hora.append("noche")
        regla.append(30)

    return [tiempo, hora, regla]


def temperatura_num_string(tem_muy_baja, tem_fria, templado, tem_caliente, tem_muy_caliente):

    if tem_muy_baja == max(tem_muy_baja, tem_fria, templado, tem_caliente, tem_muy_caliente):
        return "muy_baja"

    if tem_fria == max(tem_muy_baja, tem_fria, templado, tem_caliente, tem_muy_caliente):
        return "fria"

    if templado == max(tem_muy_baja, tem_fria, templado, tem_caliente, tem_muy_caliente):
        return "templado"

    if tem_caliente == max(tem_muy_baja, tem_fria, templado, tem_caliente, tem_muy_caliente):
        return "caliente"

    if tem_muy_caliente == max(tem_muy_baja, tem_fria, templado, tem_caliente, tem_muy_caliente):
        return "muy_caliente"


def humedad_num_string(seco, humedo, muy_humedo):
    if seco == max(seco, humedo, muy_humedo):
        return "seco"

    if humedo == max(seco, humedo, muy_humedo):
        return "humedo"

    if muy_humedo == max(seco, humedo, muy_humedo):
        return "muy_humedo"


