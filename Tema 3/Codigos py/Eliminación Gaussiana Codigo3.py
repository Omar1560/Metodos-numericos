import numpy as np
A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
b = np.array([8.0, -11.0, -3.0])

def gauss(A, b):
    n = len(b)
    Ab = np.column_stack((A, b))
    for i in range(n):
        for j in range(i+1, n):
            factor = Ab[j][i] / Ab[i][i]
            Ab[j] = Ab[j] - factor * Ab[i]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i][-1] - np.dot(Ab[i][i+1:n], x[i+1:n])) / Ab[i][i]
    return x

print("Eliminación 1:", gauss(A, b))
