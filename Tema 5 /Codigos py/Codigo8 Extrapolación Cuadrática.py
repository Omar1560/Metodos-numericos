def extrap_cuadratica_newton(x_pts, y_pts, x):
    b0 = y_pts[0]
    b1 = (y_pts[1] - y_pts[0]) / (x_pts[1] - x_pts[0])
    
    val1 = (y_pts[2] - y_pts[1]) / (x_pts[2] - x_pts[1])
    b2 = (val1 - b1) / (x_pts[2] - x_pts[0])
    
    return b0 + b1 * (x - x_pts[0]) + b2 * (x - x_pts[0]) * (x - x_pts[1])
 
tiempos = [1, 2, 3]
posiciones = [5, 20, 45]
tiempo_objetivo = 4

pos_proyectada = extrap_cuadratica_newton(tiempos, posiciones, tiempo_objetivo)

print("=" * 45)
print(f"Posición proyectada a los {tiempo_objetivo}s: {pos_proyectada:.2f} metros")
print("=" * 45)
