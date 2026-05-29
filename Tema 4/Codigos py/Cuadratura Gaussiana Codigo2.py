import math
 
def f_sgn(x):
    return -1 if x < 0 else 1
 
def gauss_ideal_n3(f, a, b):
   
    nodos = [-math.sqrt(3/5), 0.0, math.sqrt(3/5)]
    pesos = [5/9, 8/9, 5/9]
  
    integral = 0.0
    c1 = (b - a) / 2.0
    c2 = (b + a) / 2.0
    
    for idx in range(3):
        x_transformado = c1 * nodos[idx] + c2
        integral += pesos[idx] * f(x_transformado)
        
    integral *= c1
    return integral
 

limite_a = -1.0
limite_b = 1.0

print("-" * 65)
print("INTEGRACIÓN NUMÉRICA DE GAUSS (CASO DISCONTINUIDAD):")
print("-" * 65)

res = gauss_ideal_n3(f_sgn, limite_a, limite_b)

print(f"Resultado real analítico esperado: 0.0")
print(f"Resultado Gauss calculado: {res}")
print("-" * 65)
print("-" * 65)
  
