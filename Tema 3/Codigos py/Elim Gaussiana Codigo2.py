import numpy as np
A = np.array([[0.0, 2.0, 1.0], [1.0, -2.0, -3.0], [5.0, -1.0, -2.0]])
b = np.array([4.0, 0.0, -3.0])
print("Eliminación 2 (Pivoteo):", np.linalg.solve(A, b))
