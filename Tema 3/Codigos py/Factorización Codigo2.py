import numpy as np

def factorizacion_qr(A):
    n, m = A.shape
    Q = np.zeros((n, m))
    R = np.zeros((m, m))

    print("--- PROCESO DE ORTOGONALIZACIÓN QR ---")
    for j in range(m):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    print("Matriz Q (Ortogonal):\n", Q)
    print("Matriz R (Triangular):\n", R)
  
    print("\nVerificación (Q * R):\n", np.dot(Q, R))
    return Q, R

A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=float)
factorizacion_qr(A)
