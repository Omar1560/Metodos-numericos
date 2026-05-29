

def gauss_seidel_3x3(A, b, x0, tol, max_iter=50):
    n = len(b)
    x = x0.copy()
    
    print(f"{'Iter':<5}{'x1':<12}{'x2':<12}{'x3':<12}{'Error':<12}")
    print("-" * 55)
    
    for k in range(max_iter):
        x_anterior = x.copy()
        
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - suma) / A[i][i]
            
        error = sum((x[i] - x_anterior[i])**2 for i in range(n))**0.5
        
        print(f"{k+1:<5}{x[0]:<12.4f}{x[1]:<12.4f}{x[2]:<12.4f}{error:<12.4f}")
        
        if error < tol:
            break
            
    return x

A = [
    [10.0, 2.0, -1.0],
    [-3.0, -6.0, 1.0],
    [1.0, 1.0, 5.0]
]

b = [27.0, -61.5, -21.5]

x_inicial = [0.0, 0.0, 0.0]

tolerancia = 0.001

print("\nEjecución de Gauss-Seidel:")
sol_gs = gauss_seidel_3x3(A, b, x_inicial, tolerancia)

print("-" * 55)
print(f"Solución final encontrada: x1={sol_gs[0]:.4f}, x2={sol_gs[1]:.4f}, x3={sol_gs[2]:.4f}")
