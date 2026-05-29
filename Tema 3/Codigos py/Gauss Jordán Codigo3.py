import numpy as np

A = np.array([[3.0, 2.0], 
              [2.0, 3.0]])
b = np.array([11.0, 9.0])

print("--- EJERCICIO 3: MÉTODO NUMPY.SOLVE ---")
try:
    solucion = np.linalg.solve(A, b)
    print(f"Resultado optimizado: x = {solucion[0]}, y = {solucion[1]}")
except np.linalg.LinAlgError:
    print("El sistema no tiene una solución única.")
