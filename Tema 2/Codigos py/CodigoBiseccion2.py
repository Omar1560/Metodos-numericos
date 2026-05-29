import math

def biseccion_recursiva(f, a, b, tol, iteracion=1):
    c = (a + b) / 2
    
    print(f"Iter {iteracion}: c = {c:.6f}")
    
  
    if abs(f(c)) < tol or (b - a) / 2 < tol:
        return c
        
    if f(a) * f(c) < 0:
        return biseccion_recursiva(f, a, c, tol, iteracion + 1)
    else:
        return biseccion_recursiva(f, c, b, tol, iteracion + 1)

f_canal = lambda x: (x**3) + (x**2) - 2.715

a_inicial = 1.0
b_inicial = 2.0
tolerancia = 0.0005

print("-" * 55)
print("INICIANDO CÁLCULO DE BISECCIÓN RECURSIVA:")
print("-" * 55)

profundidad_critica = biseccion_recursiva(f_canal, a_inicial, b_inicial, tolerancia)

print("-" * 55)
print("¡Convergencia alcanzada exitosamente!")
print(f"La profundidad crítica calculada es: {profundidad_critica:.5f} metros.")
print("-" * 55)

