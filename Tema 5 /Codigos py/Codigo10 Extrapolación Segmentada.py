def extrap_segmentada_borde_final(x0, y0, x1, y1, x):
    
    return y1 + ((y1 - y0) / (x1 - x0)) * (x - x1)
 
t_penultimo, pres_penultima = 5, 80
t_ultimo, pres_ultima = 10, 50
t_proyeccion = 12

presion_proyectada = extrap_segmentada_borde_final(t_penultimo, pres_penultima, t_ultimo, pres_ultima, t_proyeccion)

print("=" * 45)
print(f"Presión de vacío estimada a los {t_proyeccion}s: {presion_proyectada:.2f} kPa")
print("=" * 45)
