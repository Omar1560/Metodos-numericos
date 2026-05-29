
def gauss_seidel_2x2(A, b):
    x = [0.0, 0.0]
    for _ in range(5):
        x[0] = (b[0] - A[0][1]*x[1]) / A[0][0]
        x[1] = (b[1] - A[1][0]*x[0]) / A[1][1] 
    return x

A_chem = [[8.0, 2.0], [2.0, 7.0]]
b_chem = [30.0, 24.0]
print(f"Concentraciones calculadas: {gauss_seidel_2x2(A_chem, b_chem)}")

