def f2(t, N):
    r = 0.2
    K = 1000
    return r * N * (1 - N / K)
 
t0 = 0
N0 = 100
h = 0.5   
pasos = 6  

t = t0
N = N0

print(f"Año 0.0: Población = {N:.2f}")

for i in range(1, pasos + 1):
    N = N + h * f2(t, N)
    t = t + h
    print(f"Año {t:.1f}: Población = {N:.2f}")
 
