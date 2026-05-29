# Ejercicio 1: Sistema 2x2 simple
import numpy as np

# Matriz aumentada [A|b]
# 2x + y = 5
# x - 3y = -1
matriz = np.array([[2.0, 1.0, 5.0],
                   [1.0, -3.0, -1.0]])

print("Matriz Original:")
print(matriz)

# Paso 1: Hacer el primer pivote 1
matriz[0] = matriz[0] / matriz[0][0]

# Paso 2: Hacer cero abajo del pivote
factor = matriz[1][0]
matriz[1] = matriz[1] - factor * matriz[0]

# Paso 3: Hacer el segundo pivote 1
matriz[1] = matriz[1] / matriz[1][1]

# Paso 4: Hacer cero arriba del pivote
factor = matriz[0][1]
matriz[0] = matriz[0] - factor * matriz[1]

print("\nMatriz tras Gauss-Jordan (Identidad):")
print(matriz)
print(f"\nSolución: x = {matriz[0][2]}, y = {matriz[1][2]}")

#Salida
#Matriz Original:
#[[ 2.  1.  5.]
# [ 1. -3. -1.]]

#Matriz tras Gauss-Jordan (Identidad):
#[[ 1.  0.  2.]
# [-0.  1.  1.]]

#Solución: x = 2.0, y = 1.0
