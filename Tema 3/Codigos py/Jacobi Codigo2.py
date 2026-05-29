import numpy as np
import matplotlib.pyplot as plt

def jacobi_graficado(A, b, it=20, tol=1e-5):
    n = len(b)
    x = np.zeros(n)
    errores = []

    d = np.diag(A)
    
    R = A - np.diag(d)
    
    print("-" * 50)
    print(f"{'Iter':<6}{'x aproximado':<30}{'Error (Norma)':<12}")
    print("-" * 50)
    
    for k in range(1, it + 1):
      
        x_new = (b - np.dot(R, x)) / d
     
        error = np.linalg.norm(x_new - x)
        errores.append(error)
        
        x_str = "[" + ", ".join(f"{val:.4f}" for val in x_new) + "]"
        print(f"{k:<6}{x_str:<30}{error:<12.5e}")
   
        x = x_new
        if error < tol:
            print("-" * 50)
            print(f"¡Convergencia alcanzada en la iteración {k}!")
            break


A = np.array([[5.0, -1.0, 1.0], 
              [2.0, 4.0, 0.0], 
              [1.0, 1.0, 5.0]])

b = np.array([10.0, 12.0, -1.0])

solucion = jacobi_graficado(A, b, it=15)
