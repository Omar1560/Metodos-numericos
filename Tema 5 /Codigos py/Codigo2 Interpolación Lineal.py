def interp_lineal(x0, y0, x1, y1, x):
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

# Datos del problema
t0, pos0 = 2, 15
t1, pos1 = 6, 47
t_objetivo = 5

posicion_calculada = interp_lineal(t0, pos0, t1, pos1, t_objetivo)

print("=" * 45)
print(f"Posición estimada a los {t_objetivo}s: {posicion_calculada:.2f} metros")
print("=" * 45)
