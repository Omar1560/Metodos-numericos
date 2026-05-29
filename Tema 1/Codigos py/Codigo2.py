
import math

def biseccion_p2(f, xl, xu, tol):
    
    if f(xl) * f(xu) >= 0: 
        return None
        
    for _ in range(50):
        xr = (xl + xu) / 2
        
        
        if abs((xu - xl) / xr) * 100 < tol:
            return xr
       
        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
            
    return xr

f2 = lambda m: ((9.8 * m) / 12.5) * (1 - math.exp(-125 / m)) - 35

resultado = biseccion_p2(f2, 50.0, 100.0, 0.1)

if resultado is not None:
    print(f"Masa requerida: {resultado:.3f} kg")
else:
    print("Error: El intervalo [xl, xu] no contiene una raíz (no hay cambio de signo).")
