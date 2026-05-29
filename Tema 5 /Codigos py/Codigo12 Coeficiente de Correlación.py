import numpy as np

x = np.array([1, 5], dtype=float)
y = np.array([95, 75], dtype=float)
n = len(x)

num_r = n * np.sum(x*y) - np.sum(x) * np.sum(y)
den_r = np.sqrt(((n * np.sum(x**2)) - (np.sum(x)**2)) * ((n * np.sum(y**2)) - (np.sum(y)**2)))
r = num_r / den_r

print("=" * 45)
print(f"Coeficiente de Correlación r: {r:.4f}")
print("=" * 45)
