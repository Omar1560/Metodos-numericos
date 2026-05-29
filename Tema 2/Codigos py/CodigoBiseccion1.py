def metodo_biseccion(f, xl, xu, tol, max_iter=100):
    """
    Implementación del método de bisección para encontrar raíces de ecuaciones.
    
    Parámetros:
    f        : Función matemática a evaluar.
    xl       : Límite inferior del intervalo.
    xu       : Límite superior del intervalo.
    tol      : Tolerancia del error aproximado porcentual (%).
    max_iter : Número máximo de iteraciones permitidas.
    """
    if f(xl) * f(xu) >= 0:
        print("El método de bisección no puede garantizar la convergencia.")
        print("Asegúrate de que haya un cambio de signo en el intervalo elegido.")
        return None


    print(f"{'Iter':<6}{'xl':<10}{'xu':<10}{'xr (Raíz)':<12}{'f(xr)':<12}{'Ea (%)':<10}")
    print("-" * 62)

    xr_anterior = xl
    
    for i in range(max_iter):
     
        xr = (xl + xu) / 2.0
        fxr = f(xr)
        
        if i > 0:
            ea = abs((xr - xr_anterior) / xr) * 100
        else:
            ea = 100.0  
        print(f"{i+1:<6}{xl:<10.4f}{xu:<10.4f}{xr:<12.5f}{fxr:<12.5f}{ea:<10.4f}")

        if fxr == 0.0 or ea < tol:
            print("-" * 62)
            print(f"¡Convergencia alcanzada! Raíz aproximada encontrada en {i+1} iteraciones.")
            return xr

        if f(xl) * fxr < 0:
            xu = xr  
        else:
            xl = xr  
            
        xr_anterior = xr

    print("-" * 62)
    print("Se alcanzó el número máximo de iteraciones sin lograr la tolerancia deseada.")
    return xr

f_canal = lambda y: y**3 + 2*(y**2) - 4

lim_inferior = 1.0
lim_superior = 2.0
tolerancia_objetivo = 0.01 

profundidad_critica = metodo_biseccion(f_canal, lim_inferior, lim_superior, tolerancia_objetivo)

if profundidad_critica is not None:
    print(f"La profundidad crítica calculada del canal es: {profundidad_critica:.5f} metros.")
