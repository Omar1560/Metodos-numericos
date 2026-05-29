def f(t, y):
    return 0.5 * y
 
t = [0.0, 0.1]
y = [100.0, 105.12]
h = 0.1

print(f"Paso 0: t = {t[0]:.1f} -> y = {y[0]:.2f}")
print(f"Paso 1: t = {t[1]:.1f} -> y = {y[1]:.2f}")
 
for n in range(1, 3):
    
    f_actual = f(t[n], y[n])
    f_anterior = f(t[n-1], y[n-1])
     
    y_siguiente = y[n] + (h / 2.0) * (3 * f_actual - f_anterior)
    t_siguiente = t[n] + h
    
    y.append(y_siguiente)
    t.append(t_siguiente)
    print(f"Paso {n+1}: t = {t_siguiente:.1f} -> y = {y_siguiente:.2f}")
 
