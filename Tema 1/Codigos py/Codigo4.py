
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
f3 = lambda x: math.exp(x) - 3 * x

resultado = biseccion_p2(f3, 0.0, 1.0, 0.001)

if resultado is not None:
    print(f"Raíz termodinámica: {resultado:.4f}")
else:
    print("Error: No hay cambio de signo en el intervalo [0, 1].")
