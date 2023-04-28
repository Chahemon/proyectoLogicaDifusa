# En cambas funciones el valor "x" es la entrada.

# Función trapezoidal

def trapezoidal(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return 1
    else:
        return (d - x) / (d - c)


# Función triangular

def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

