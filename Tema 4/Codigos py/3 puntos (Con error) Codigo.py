import math
x0, h = (math.pi / 2) - 0.01, 0.5
try:
    aprox = (math.tan(x0 + h) - math.tan(x0 - h)) / (2 * h)
    print(f"Resultado incorrecto: {aprox:.4f}")
except: print("Error en evaluación")
