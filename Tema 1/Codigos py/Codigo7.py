

def jacobi_2x2(A, b, tol=0.01):
    x = [0.0, 0.0]
    xn = [0.0, 0.0]
    for _ in range(10):
        xn[0] = (b[0] - A[0][1]*x[1]) / A[0][0]
        xn[1] = (b[1] - A[1][0]*x[0]) / A[1][1]
        x = xn.copy()
    return x

A2 = [[5.0, -2.0], [-1.0, 4.0]]
b2 = [9.0, 9.0]
print(f"Corrientes de malla (Jacobi): {jacobi_2x2(A2, b2)}")
