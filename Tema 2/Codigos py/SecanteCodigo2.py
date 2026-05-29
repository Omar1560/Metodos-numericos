def secante_tol(f, x0, x1, tol=1e-7, max_it=30):
    print("-" * 65)
    print(f"{'Iter':<6}{'x0':<12}{'x1':<12}{'x_nuevo':<12}{'f(x1)':<12}")
    print("-" * 65)
    
    for i in range(1, max_it + 1):
        f0 = f(x0)
        f1 = f(x1)
        if abs(f1) <= tol:
            print("-" * 65)
            print(f"¡Convergencia alcanzada en la iteración {i-1}!")
            return x1
            
        if abs(f1 - f0) < 1e-12:
            print("-" * 65)
            print(f"Error en iteración {i}: División por cero detectada (f(x1) == f(x0)).")
            print("El método se detuvo para proteger la terminal.")
            return None
            
        temp = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        
        print(f"{i:<6}{x0:<12.5f}{x1:<12.5f}{temp:<12.5f}{f1:<12.5e}")
        
        x0, x1 = x1, temp
        
    print("-" * 65)
    print(f"Advertencia: Se agotaron las {max_it} iteraciones máximas sin alcanzar el criterio.")
    return x1


f_prueba = lambda x: x**3 - x - 1

punto_a = 1.0
punto_b = 2.0

print("\nEJECUTANDO SECANTE CON TOLERANCIA INTELIGENTE:")
raiz = secante_tol(f_prueba, punto_a, punto_b, tol=1e-7)

if raiz is not None:
    print(f"La raíz calculada con precisión es: {raiz:.6f}")
    print("-" * 65)
