def extrap_cuadratica_newton(x_pts, y_pts, x):
    b0 = y_pts[0]
    b1 = (y_pts[1] - y_pts[0]) / (x_pts[1] - x_pts[0])
    
    val1 = (y_pts[2] - y_pts[1]) / (x_pts[2] - x_pts[1])
    b2 = (val1 - b1) / (x_pts[2] - x_pts[0])
    
    return b0 + b1 * (x - x_pts[0]) + b2 * (x - x_pts[0]) * (x - x_pts[1])

# Datos del problema
unidades = [10, 20, 30]
costos = [150, 240, 350]
unidades_objetivo = 40

costo_proyectado = extrap_cuadratica_newton(unidades, costos, unidades_objetivo)

print("=" * 45)
print(f"Costo proyectado para {unidades_objetivo} unidades: ${costo_proyectado:.2f}")
print("=" * 45)
