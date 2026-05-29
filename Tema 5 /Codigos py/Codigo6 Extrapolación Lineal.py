def extrap_lineal(x0, y0, x1, y1, x):
    return y1 + ((y1 - y0) / (x1 - x0)) * (x - x1)
 
año_base1, pob_base1 = 2020, 50000
año_base2, pob_base2 = 2024, 58000
año_proyeccion = 2026

pob_proyectada = extrap_lineal(año_base1, pob_base1, año_base2, pob_base2, año_proyeccion)

print("=" * 45)
print(f"Población proyectada para {año_proyeccion}: {pob_proyectada:.0f} hab.")
print("=" * 45)
