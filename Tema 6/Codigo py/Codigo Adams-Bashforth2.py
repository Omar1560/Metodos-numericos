def f(t, y):
    return t - y
 
t = [0.0, 0.1, 0.2, 0.3]
y = [1.0000, 0.9052, 0.8213, 0.7492]
h = 0.1

print("Puntos de arranque conocidos:")
for i in range(4):
    print(f"  t = {t[i]:.1f} -> y = {y[i]:.4f}")
 
n = 3

f_n  = f(t[n], y[n])
f_n1 = f(t[n-1], y[n-1])
f_n2 = f(t[n-2], y[n-2])
f_n3 = f(t[n-3], y[n-3])
 
y_siguiente = y[n] + (h / 24.0) * (55 * f_n - 59 * f_n1 + 37 * f_n2 - 9 * f_n3)
t_siguiente = t[n] + h

print(f"\nResultado predicho:")
print(f"  Paso 4: t = {t_siguiente:.1f} -> y = {y_siguiente:.4f}")
 
