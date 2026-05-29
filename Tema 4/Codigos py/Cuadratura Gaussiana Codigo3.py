import numpy as np

def f_z(z):
    return (1/np.sqrt(2*np.pi)) * np.exp(-0.5*z**2)

def gauss_stats(a, b, n=5):
    nodos, pesos = np.polynomial.legendre.leggauss(n)
    puntos = 0.5 * (b - a) * nodos + 0.5 * (a + b)
    return 0.5 * (b - a) * sum(w * f_z(p) for w, p in zip(pesos, puntos))

print(f"Probabilidad P(0 < Z < 1.5): {gauss_stats(0, 1.5):.8f}")

 
