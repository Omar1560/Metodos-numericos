# Unidad 4: Diferenciación e Integración Numérica

Esta sección del repositorio aborda las técnicas numéricas utilizadas para aproximar los dos conceptos fundamentales del cálculo: la derivada (tasa de cambio instantánea) y la integral definida (área bajo la curva), herramientas esenciales cuando las funciones no poseen una primitiva analítica directa o están definidas únicamente por un conjunto de puntos discretos.

---

## 4.1 Diferenciación numérica

La diferenciación numérica aproxima el valor de la derivada de una función en un punto específico utilizando los valores de la función en puntos cercanos espaciados uniformemente por una distancia $h$ (tamaño de paso).

### 1. Fórmulas de Diferencias Finitas de Primer Orden
Derivadas a partir de la expansión de la Serie de Taylor, truncando los términos de orden superior:

* **Diferencia Hacia Adelante (Forward):** Emplea el punto actual y el punto siguiente.
  $$f'(x_i) \approx \frac{f(x_{i+1}) - f(x_i)}{h} + \mathcal{O}(h)$$

* **Diferencia Hacia Atrás (Backward):** Emplea el punto actual y el punto anterior.
  $$f'(x_i) \approx \frac{f(x_i) - f(x_{i-1})}{h} + \mathcal{O}(h)$$

* **Diferencia Central (Centered):** Emplea el punto siguiente y el anterior. Es significativamente más exacta porque el error de truncamiento se reduce de manera cuadrática.
  $$f'(x_i) \approx \frac{f(x_{i+1}) - f(x_{i-1})}{2h} + \mathcal{O}(h^2)$$

### 2. Fórmulas de Alta Precisión y Segundas Derivadas
Para aproximar la tasa de aceleración o la concavidad (segunda derivada), se utiliza comúnmente la fórmula de diferencia central de segundo orden:

$$f''(x_i) \approx \frac{f(x_{i+1}) - 2f(x_i) + f(x_{i-1})}{h^2} + \mathcal{O}(h^2)$$

---

## 4.2 Integración numérica (Fórmulas de Newton-Cotes)

Las fórmulas de Newton-Cotes son los esquemas más comunes de integración numérica. Se basan en aproximar una función compleja o un conjunto de puntos mediante un polinomio fácil de integrar sobre un intervalo cerrado $[a, b]$.

### 1. Regla del Trapecio
Aproxima el área bajo la curva dividiendo el intervalo en uno o más trapecios rectos.



* **Regla del Trapecio Simple (1 intervalo):**
  $$\int_{a}^{b} f(x) \,dx \approx \frac{b - a}{2} [f(a) + f(b)]$$

* **Regla del Trapecio Compuesta ($n$ subintervalos de ancho $h = \frac{b-a}{n}$):**
  $$\int_{a}^{b} f(x) \,dx \approx \frac{h}{2} \left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$

### 2. Regla de Simpson 1/3
Aproxima la función mediante polinomios de segundo grado (parábolas). Requiere obligatoriamente que el número de subintervalos $n$ sea **par**.

* **Regla de Simpson 1/3 Compuesta:**
  $$\int_{a}^{b} f(x) \,dx \approx \frac{h}{3} \left[ f(x_0) + 4\sum_{i \text{ impar}}^{n-1} f(x_i) + 2\sum_{j \text{ par}}^{n-2} f(x_j) + f(x_n) \right]$$

### 3. Regla de Simpson 3/8
Aproxima la función utilizando polinomios de tercer grado (cúbicos). Requiere que el número de subintervalos $n$ sea **múltiplo de 3**.

* **Regla de Simpson 3/8 Simple:**
  $$\int_{a}^{b} f(x) \,dx \approx \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]$$

---

## 4.3 Integración de Gauss (Cuadratura Gaussiana)

A diferencia de las reglas de Newton-Cotes, donde los puntos de evaluación están fijos y espaciados uniformemente, la **Cuadratura Gaussiana** selecciona de manera óptima los puntos (nodos) y los coeficientes (pesos) para maximizar la precisión de la integración.

Una integral en el intervalo estándar $[-1, 1]$ se aproxima mediante la suma ponderada:
$$\int_{-1}^{1} f(t) \,dt \approx \sum_{i=1}^{n} w_i \cdot f(t_i)$$

Para aplicar este método a cualquier intervalo genérico $[a, b]$, se realiza un cambio de variable lineal hacia la variable $t$:
$$x = \frac{b-a}{2}t + \frac{a+b}{2} \quad \implies \quad dx = \frac{b-a}{2}dt$$

### Valores estándar para Cuadratura Gaussiana de 2 puntos ($n=2$)
* **Nodos ($t_i$):** $t_1 = -\frac{1}{\sqrt{3}} \approx -0.57735$, \quad $t_2 = \frac{1}{\sqrt{3}} \approx 0.57735$
* **Pesos ($w_i$):** $w_1 = 1$, \quad $w_2 = 1$
* **Exactitud:** Es exacta para cualquier polinomio de grado 3 o menor utilizando solo dos evaluaciones.

---

## 4.4 Tabla Comparativa de Métodos de Integración

| Método | Grado del Polinomio | Restricción de Subintervalos ($n$) | Orden del Error global | Ideal para... |
| :--- | :---: | :---: | :---: | :--- |
| **Trapecio Compuesto** | 1 (Lineal) | $n \ge 1$ (Cualquiera) | $\mathcal{O}(h^2)$ | Funciones con comportamiento lineal o datos dispersos generales. |
| **Simpson 1/3 Compuesto** | 2 (Parabólico) | $n$ debe ser **Par** | $\mathcal{O}(h^4)$ | Funciones continuas suaves con curvaturas moderadas. |
| **Simpson 3/8 Compuesto** | 3 (Cúbico) | $n$ debe ser **Múltiplo de 3** | $\mathcal{O}(h^4)$ | Ajustar variaciones bruscas en los extremos del intervalo. |
| **Cuadratura Gaussiana** | $2n - 1$ | No aplica (usa pesos óptimos) | Muy alto | Integrar funciones continuas conocidas con alta precisión analítica. |

---

## 4.5 Ejemplo de Implementación en Python

El siguiente script en Python contrasta las aproximaciones de la **Regla de Simpson 1/3** y la **Regla del Trapecio** para integrar la función $f(x) = \sin(x)$ en el intervalo $[0, \pi]$ (cuyo valor real exacto es $2.0$):

```python
import numpy as np

def f(x):
    return np.sin(x)

def regla_trapecio_compuesta(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    suma_interior = np.sum(y[1:-1])
    integral = (h / 2) * (y[0] + 2 * suma_interior + y[-1])
    return integral

def regla_simpson_13_compuesta(a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos 'n' debe ser par para Simpson 1/3.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    
    suma_impares = np.sum(y[1:-1:2])
    suma_pares = np.sum(y[2:-1:2])
    
    integral = (h / 3) * (y[0] + 4 * suma_impares + 2 * suma_pares + y[-1])
    return integral

# Parámetros del problema
lim_inferior = 0
lim_superior = np.pi
subintervalos = 10  # Es par, válido para ambos métodos

# Cálculos
val_trapecio = regla_trapecio_compuesta(lim_inferior, lim_superior, subintervalos)
val_simpson = regla_simpson_13_compuesta(lim_inferior, lim_superior, subintervalos)

print(f"--- Integración Numérica de sin(x) de 0 a pi (Valor Real = 2.0) ---")
print(f"Resultado Regla del Trapecio: {val_trapecio:.6f} | Error: {abs(2.0 - val_trapecio):.6f}")
print(f"Resultado Regla Simpson 1/3:  {val_simpson:.6f} | Error: {abs(2.0 - val_simpson):.6f}")
