import math

def f(x):
    return math.sqrt(100 - x**2)

def trapecio_ideal(a, b, n):
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
    for i in range(1, n):
        suma += f(a + i * h)
    return suma * h

resultado = trapecio_ideal(0, 8, 100)
print(f"Área calculada: {resultado:.6f} m2")
 
