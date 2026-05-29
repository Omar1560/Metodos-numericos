 
def biseccion_p1(f, xl, xu, tol, max_iter=100):
    if f(xl) * f(xu) >= 0:
        print("El método de bisección falla: No hay cambio de signo en el intervalo.")
        return None
    
    iteracion = 0
    xr_anterior = xl
    
    print(f"{'Iter':<5}{'xl':<10}{'xu':<10}{'xr':<10}{'f(xr)':<12}{'Ea (%)':<10}")
    print("-" * 60)
    
    while iteracion < max_iter:
        xr = (xl + xu) / 2
        fxr = f(xr)
        
        ea = abs((xr - xr_anterior) / xr) * 100 if iteracion > 0 else 100
        
        print(f"{iteracion+1:<5}{xl:<10.4f}{xu:<10.4f}{xr:<10.4f}{fxr:<12.4f}{ea:<10.4f}")
        
        if fxr == 0 or ea < tol:
            return xr
            
        if f(xl) * fxr < 0:
            xu = xr
        else:
            xl = xr
            
        xr_anterior = xr
        iteracion += 1
        
    return xr
 
f1 = lambda x: x**3 - x - 2
raiz = biseccion_p1(f1, 1.0, 2.0, 0.01)
print(f"\nRaíz aproximada: {raiz:.4f}")
 
