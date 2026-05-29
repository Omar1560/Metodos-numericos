def secante_clasica(f, x0, x1, tol=1e-5, iters=15):
    print("-" * 55)
    print(f"{'Iter':<6}{'x0':<10}{'x1':<10}{'x_nuevo':<12}{'f(x_nuevo)':<12}")
    print("-" * 55)
    
    for i in range(iters):
        f0, f1 = f(x0), f(x1)
        
        if abs(f1 - f0) < 1e-12:
            print("-" * 55)
            print(f"Error en Iter {i+1}: Denominador nula o muy pequeño (f(x1) - f(x0) = {f1-f0}).")
            print("El método se detuvo para evitar una división por cero.")
            return None
            
        x_new = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        fx_new = f(x_new)
        
        print(f"{i+1:<6}{x0:<10.4f}{x1:<10.4f}{x_new:<12.5f}{fx_new:<12.5e}")
        
        if abs(fx_new) < tol:
            print("-" * 55)
            print(f"¡Convergencia alcanzada en la iteración {i+1}!")
            return x_new
            
        x0, x1 = x1, x_new
        
    print("-" * 55)
    print(f"Advertencia: Se completaron las {iters} iteraciones sin alcanzar la tolerancia.")
    return x1

f_prueba = lambda x: x**2 - 4

punto_x0 = 4.0
punto_x1 = 3.5

print("\nEJECUTANDO MÉTODO DE LA SECANTE:")
raiz = secante_clasica(f_prueba, punto_x0, punto_x1, tol=1e-6)

if raiz is not None:
    print(f"La raíz calculada es: {raiz:.5f}")
    print("-" * 55)
