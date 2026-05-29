def falsa_pos_mejorada(f, a, b, tol):
    fa, fb = f(a), f(b)
    
    if fa * fb >= 0:
        print("Error: El intervalo inicial no encierra una raíz (no hay cambio de signo).")
        return None
        
    x_ant = 0.0
    
    print("-" * 70)
    print(f"{'Iter':<6}{'a':<10}{'b':<10}{'x (Raíz)':<12}{'f(x)':<12}{'Error Rel.':<10}")
    print("-" * 70)
    
    for i in range(1, 51):
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)
        
        if i == 1:
            error = 100.0
        else:
            error = abs((x - x_ant) / x) * 100 if x != 0 else 0
            
        print(f"{i:<6}{a:<10.4f}{b:<10.4f}{x:<12.6f}{fx:<12.5e}{error:<10.2f}%")
        
        if abs(fx) < tol or (i > 1 and error < tol):
            print("-" * 70)
            print(f"¡Convergencia lograda en la iteración {i}!")
            break
            
        x_ant = x
        if fa * fx < 0:
            b = x
            fb = fx
            fa = fa / 2.0  
        else:
            a = x
            fa = fx
            fb = fb / 2.0  

    return x
f_prueba = lambda x: x**10 - 1

intervalo_a = 0.0
intervalo_b = 1.3
tolerancia = 0.01  

print("\nEJECUTANDO FALSA POSICIÓN MEJORADA (MÉTODO DE ILLINOIS):")
raiz = falsa_pos_mejorada(f_prueba, intervalo_a, intervalo_b, tolerancia)

if raiz is not None:
    print(f"La raíz calculada es: {raiz:.6f}")
    print("-" * 70)
