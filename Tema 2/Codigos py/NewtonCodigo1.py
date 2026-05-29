def newton_auto_derivar(f, x0, tol=1e-5, h=1e-5, max_it=20):
    x = x0
    
    print("-" * 50)
    print(f"{'Iter':<6}{'x actual':<15}{'f(x)':<15}")
    print("-" * 50)
    
    for i in range(1, max_it + 1):
        fx = f(x)
        
        print(f"{i:<6}{x:<15.6f}{fx:<15.5e}")
        
        if abs(fx) < tol:
            print("-" * 50)
            print(f"¡Convergencia alcanzada en la iteración {i}!")
            return x
            
        df_num = (f(x + h) - f(x - h)) / (2 * h)
        
        if abs(df_num) < 1e-12:
            print("-" * 50)
            print("Error: La derivada numérica dio cero. El método no puede continuar.")
            return None
            
        x = x - fx / df_num
        
    print("-" * 50)
    print(f"Se completaron las {max_it} iteraciones.")
    return x

f_prueba = lambda x: x**3 - x - 2

x_inicial = 1.0

print("\nEJECUTANDO NEWTON-RAPHSON CON AUTO-DERIVACIÓN:")
raiz = newton_auto_derivar(f_prueba, x_inicial, tol=1e-6)

if raiz is not None:
    print(f"La raíz calculada es: {raiz:.6f}")
    print("-" * 50)

