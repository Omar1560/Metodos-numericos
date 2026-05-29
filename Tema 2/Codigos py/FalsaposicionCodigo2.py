def falsa_pos_limite(f, a, b, max_it=15):
 
    if f(a) * f(b) >= 0:
        print("Error: Los límites iniciales no encierran una raíz (signos iguales).")
        return None

    res = []
  
    fa = f(a)
    fb = f(b)
    
    for _ in range(max_it):
     
        x = b - (fb * (a - b)) / (fa - fb)
        res.append(x)
        
        fx = f(x)
        
        if abs(fx) == 0:
            break
            
        if fa * fx < 0: 
            b = x
            fb = fx
        else: 
            a = x
            fa = fx
            
    print("Flujo de aproximaciones:", [round(r, 4) for r in res])
    return res

f_prueba = lambda x: x**2 - 2

intervalo_a = 1.0
intervalo_b = 2.0

print("\nEJECUTANDO FALSA POSICIÓN (FLUJO DE RAÍCES):")
flujo = falsa_pos_limite(f_prueba, intervalo_a, intervalo_b, max_it=10)
