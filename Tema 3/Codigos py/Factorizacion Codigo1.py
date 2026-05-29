import numpy as np

def factorizacion_lu(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    print("--- INICIANDO DESCOMPOSICIÓN LU ---")
    for i in range(n):
        
        for k in range(i, n):
            suma = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - suma

        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                suma = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - suma) / U[i][i]

    print("Matriz L:\n", L)
    print("Matriz U:\n", U)

    y = np.zeros(n)
    for i in range(n):
        suma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - suma

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U[i][i]

    return x

A = np.array([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]], dtype=float)
b = np.array([-1, 13, -6], dtype=float)
solucion = factorizacion_lu(A, b)
print("\nSolución Final x:", solucion)

