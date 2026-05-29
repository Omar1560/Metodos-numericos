import numpy as np

def eliminacion_gaussiana(A, b):
    n = len(b)
  
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)

    for i in range(n):
        for j in range(i + 1, n):
            factor = Ab[j][i] / Ab[i][i]
            Ab[j] = Ab[j] - factor * Ab[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i][-1] - np.dot(Ab[i][i+1:n], x[i+1:n])) / Ab[i][i]
    
    return x

A = np.array([[3.0, 2.0, -1.0], [2.0, -2.0, 4.0], [-1.0, 0.5, -1.0]])
b = np.array([1.0, -2.0, 0.0])

solucion = eliminacion_gaussiana(A, b)
print("--- ELIMINACIÓN GAUSSIANA ---")
print(f"Solución: {solucion}")
