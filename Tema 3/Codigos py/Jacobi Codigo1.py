import numpy as np

def jacobi_tolerancia(A, b, tol=1e-5, max_iter=100):
    n = len(b)
    x = np.zeros(n)
    x_prev = np.zeros(n)
    
    print(f"{'Iter':<5} | {'Error':<12} | {'Solución'}")
    
    for k in range(max_iter):
        for i in range(n):
            suma = sum(A[i][j] * x_prev[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i][i]
        
        error = np.linalg.norm(x - x_prev, np.inf)
        print(f"{k+1:<5} | {error:<12.6f} | {x}")
        
        if error < tol:
            print(f"Convergencia alcanzada en {k+1} iteraciones.")
            return x
        x_prev = x.copy()
    return x

A = np.array([[4, -1, 1], [4, -8, 1], [-2, 1, 5]], dtype=float)
b = np.array([7, -21, 15], dtype=float)
jacobi_tolerancia(A, b)
