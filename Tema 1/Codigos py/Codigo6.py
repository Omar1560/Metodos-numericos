

def jacobi_3x3(A, b, x0, tol, max_iter=50):
    n = len(b)
    x = x0.copy()
    x_nuevo = x.copy()
    
    print(f"{'Iter':<5}{'x1':<10}{'x2':<10}{'x3':<10}")
    
    for k in range(max_iter):
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - suma) / A[i][i]
            
        error = sum((x_nuevo[i] - x[i])**2 for i in range(n))**0.5
        x = x_nuevo.copy()
        
        print(f"{k+1:<5}{x[0]:<10.4f}{x[1]:<10.4f}{x[2]:<10.4f}")
        if error < tol: break
    return x


A = [[10.0, -1.0, 2.0],
     [-1.0, 11.0, -1.0],
     [2.0, -1.0, 10.0]]
b = [6.0, 25.0, -11.0]
x0 = [0.0, 0.0, 0.0]

print("\nEjecución de Jacobi:")
sol = jacobi_3x3(A, b, x0, 0.001) 
