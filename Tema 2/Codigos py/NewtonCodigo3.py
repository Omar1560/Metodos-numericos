def newton_simple(f, df, x0, tol=0.001, max_it=50):
    x = x0
    
    print("-" * 50)
    print(f"{'Iter':<6}{'x actual':<12}{'f(x)':<12}{'f\'(x)':<12}")
    print("-" * 50)
    
    for i in range(1, max_it + 1):
        fx = f(x)
        dfx = df(x)
        print(f"{i:<6}{x:<12.5f}{fx:<12.5f}{dfx:<12.5f}")
        
        if abs(dfx) < 1e-12:
            print("-" * 50)
            print("Error: La derivada es prácticamente cero. El método se detuvo.")
            return None
        if abs(fx) < tol:
            print("-" * 50)
            print(f"¡Convergencia alcanzada en la iteración {i}!")
            return x

        x = x - fx / dfx
        
    print("-" * 50)
    print(f"Advertencia: Se alcanzaron las {max_it} iteraciones máximas sin converger.")
    return x


f_prueba = lambda x: x**2 - 9

df_prueba = lambda x: 2 * x

x_inicial = 5.0

print("\nEJECUTANDO MÉTODO DE NEWTON-RAPHSON:")
raiz = newton_simple(f_prueba, df_prueba, x_inicial, tol=0.0001)

if raiz is not None:
    print(f"La raíz calculada es: {raiz:.5f}")
    print("-" * 50)

