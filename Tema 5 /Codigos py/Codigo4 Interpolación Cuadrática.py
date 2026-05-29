def interp_cuadratica_newton(x_pts, y_pts, x):
    b0 = y_pts[0]
    b1 = (y_pts[1] - y_pts[0]) / (x_pts[1] - x_pts[0])
    
    val1 = (y_pts[2] - y_pts[1]) / (x_pts[2] - x_pts[1])
    b2 = (val1 - b1) / (x_pts[2] - x_pts[0])
    
    return b0 + b1 * (x - x_pts[0]) + b2 * (x - x_pts[0]) * (x - x_pts[1])

# Datos del problema
profundidades = [0, 1, 2]
caudales = [0, 2.5, 8.0]
prof_objetivo = 1.5

caudal_estimado = interp_cuadratica_newton(profundidades, caudales, prof_objetivo)

print("=" * 45)
print(f"Caudal estimado a {prof_objetivo}m: {caudal_estimado:.4f} m³/s")
print("=" * 45)
