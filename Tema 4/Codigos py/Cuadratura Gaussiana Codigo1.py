import numpy as np

def f_cable(x):
    return 10 * np.cosh(x/10)

def gauss_ideal(a, b):
    # Nodos y pesos para n=3
    nodos = [-0.7745966, 0, 0.7745966]
    pesos = [0.5555556, 0.8888889, 0.5555556]
    
    # Cambio de variable a [-1, 1]
    suma = 0
    for i in range(3):
        punto = 0.5 * (b - a) * nodos[i] + 0.5 * (a + b)
        suma += pesos[i] * f_cable(punto)
    return 0.5 * (b - a) * suma

print(f"Longitud del cable: {gauss_ideal(-5, 5):.6f} m")

#Salida

#Longitud del cable: 104.219016 m
