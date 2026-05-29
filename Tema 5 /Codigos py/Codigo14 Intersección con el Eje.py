import numpy as np

x = np.array([0, 1, 2], dtype=float)
y = np.array([1, 3, 4], dtype=float)
n = len(x)

# Calculamos primero a1 de forma interna
a1 = (n * np.sum(x*y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x)**2))

# Fórmula para la ordenada al origen
a0 = np.mean(y) - a1 * np.mean(x)

print("=" * 45)
print(f"Ordenada al origen (a0): {a0:.4f}")
print(f"Ecuación de la recta : Y = {a0:.4f} + {a1:.4f} * X")
print("=" * 45)
