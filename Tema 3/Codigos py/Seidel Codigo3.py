def gs_con_log(A, b, it=10):
    n = len(b)
    x = [0.0] * n 
    
 
    with open("resultado_gs.txt", "w") as f:
        f.write("==================================================\n")
        f.write("         LOG DE ITERACIONES GAUSS-SEIDEL          \n")
        f.write("==================================================\n\n")
        
        for k in range(it):
            for i in range(n):
              
                s = 0.0
                for j in range(n):
                    if i != j:
                        s += A[i][j] * x[j]
         
                x[i] = (b[i] - s) / A[i][i]
            
            x_str = "[" + ", ".join(f"{val:.6f}" for val in x) + "]"
            f.write(f"Iteracion {k+1}: {x_str}\n")
            
        f.write("\n==================================================\n")
        f.write("Proceso finalizado con éxito.\n")
        
    print("--------------------------------------------------")
    print("¡Historial guardado exitosamente en 'resultado_gs.txt'!")
    print("--------------------------------------------------")
    return x

A = [
    [4.0, 1.0, 2.0], 
    [3.0, 5.0, 1.0], 
    [1.0, 1.0, 3.0]
]

b = [9.0, 14.0, 11.0]

solucion_final = gs_con_log(A, b, it=10)

print(f"Solución final en terminal: {solucion_final}")
