import numpy as np
import math

def cholesky_detallado(A, b):
    n = len(A)
    L = np.zeros((n, n))

    print("--- MÉTODO DE CHOLESKY ---")
    try:
        for i in range(n):
            for j in range(i + 1):
                suma = sum(L[i][k] * L[j][k] for k in range(j))
                
                if i == j:
                    L[i][j] = math.sqrt(A[i][i] - suma)
                else:
                    L[i][j] = (1.0 / L[j][j]) * (A[i][j] - suma)
        
        print("Matriz L (Triangular inferior):\n", L)
    
        y = np.linalg.solve(L, b)
        
        x = np.linalg.solve(L.T, y)
        
        return x
    except ValueError:
        return "Error: La matriz debe ser definida positiva."

A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]], dtype=float)
b = np.array([1, 2, 3], dtype=float)
print("Solución Cholesky:", cholesky_detallado(A, b))
