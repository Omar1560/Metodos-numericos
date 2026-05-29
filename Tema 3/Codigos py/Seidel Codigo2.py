import numpy as np

def sistema_aleatorio_gs(size=5):
 
    A = np.random.rand(size, size)
    A = A + np.diag(np.sum(np.abs(A), axis=1))
    b = np.random.rand(size)
    
    x = np.zeros(size)
    for _ in range(50):
        for i in range(size):
            s = sum(A[i][j] * x[j] for j in range(size) if i != j)
            x[i] = (b[i] - s) / A[i][i]
    print(f"Sistema {size}x{size} resuelto.")
    print("X:", x)

sistema_aleatorio_gs(10)
