def extrap_lineal(x0, y0, x1, y1, x):
    return y1 + ((y1 - y0) / (x1 - x0)) * (x - x1)
 
ciclo1, cap1 = 100, 92
ciclo2, cap2 = 200, 86
ciclo_extrapolar = 250

cap_proyectada = extrap_lineal(ciclo1, cap1, ciclo2, cap2, ciclo_extrapolar)

print("=" * 45)
print(f"Capacidad en ciclo {ciclo_extrapolar}: {cap_proyectada:.2f}%")
print("=" * 45)
