def trapecio_tabulado(datos, h):
  
    n = len(datos)
    suma = (datos[0] + datos[-1]) / 2
    for i in range(1, n - 1):
        suma += datos[i]
    return suma * h

caudales = [0, 1.5, 3.2, 4.5, 3.0, 0.8]
print(f"Volumen total: {trapecio_tabulado(caudales, 2):.4f} m3")

 
