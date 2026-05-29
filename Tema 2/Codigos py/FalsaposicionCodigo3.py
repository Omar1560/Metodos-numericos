def falsa_pos_error(f, a, b, tol):

    if f(a) * f(b) >= 0:
        print("Error: El método de la falsa posición requiere que f(a) y f(b) tengan signos opuestos.")
        return None

    x_ant = 0.0  
    
    print("-" * 60)
    print(f"{'Iter':<6}{'a':<10}{'b':<10}{'x (Raíz)':<12}{'Error Relativo':<15}")
    print("-" * 60)
    
    for i in range(1, 50): 
        x = b - (f(b) * (b - a)) / (f(b) - f(a))
        
        if i == 1:
        else:
            error = abs((x - x_ant) / x) * 100 if x != 0 else 0
            
        print(f"{i:<6}{a:<10.4f}{b:<10.4f}{x:<12.5f}{error:<14.2f}%")
        
        if abs(f(x)) < tol or (i > 1 and error < tol): 
            print("-" * 60)
            print(f"¡Convergencia alcanzada en la iteración {i}!")
            break
            
        x_ant = x
        
        if f(a) * f(x) < 0: 
            b = x
        else: 
            a = x
            
    return x

f_ejemplo = lambda x: x**3 - 2*x - 5

intervalo_a = 2.0
intervalo_b = 3.0
tolerancia_error = 0.01  

print("\nEJECUTANDO MÉTODO DE FALSA POSICIÓN:")
raiz_encontrada = falsa_pos_error(f_ejemplo, intervalo_a, intervalo_b, tolerancia_error)

if raiz_encontrada is not None:
    print(f"La raíz aproximada es: {raiz_encontrada:.5f}")
    print("-" * 60)



#Convergencia alcanzada en la iteración 5!
#La raíz aproximada es: 2.09388
