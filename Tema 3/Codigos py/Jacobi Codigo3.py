import numpy as np

def es_diagonal_dominante(A):
    diag = np.abs(np.diag(A))
    suma_filas = np.sum(np.abs(A), axis=1) - diag
    if np.all(diag > suma_filas):
        return True
    return False

A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]])
if es_diagonal_dominante(A):
    print("La matriz es diagonal dominante. El método convergerá.")
else:
    print("Advertencia: El método podría no converger.")
