# Unidad 6: Solución de Ecuaciones Diferenciales

Esta sección del repositorio se enfoca en los métodos numéricos diseñados para resolver Ecuaciones Diferenciales Ordinarias (EDO). Estos métodos son indispensables en la ingeniería, ya que la mayoría de las leyes físicas (como las leyes de Newton, las leyes de circuitos o los balances de masa y energía) se expresan naturalmente en términos de tasas de cambio (derivadas), cuyas soluciones analíticas exactas suelen ser complejas o imposibles de obtener.

---

## 6.1 Conceptos básicos de Ecuaciones Diferenciales Ordinarias (EDO)

Una Ecuación Diferencial Ordinaria es una ecuación que involucra una función de una sola variable independiente y una o más de sus derivadas. El objetivo de los métodos numéricos es aproximar los valores de la función incógnita $y(x)$ en un conjunto discreto de puntos, a partir de una condición inicial dada.

### Problema de Valor Inicial (PVI)
La estructura estándar de un PVI de primer orden se define como:
$$\frac{dy}{dx} = f(x, y), \quad \text{con la condición inicial: } y(x_0) = y_0$$

El algoritmo calcula de forma iterativa los valores aproximados en pasos uniformes de tamaño $h$:
$$x_{n+1} = x_n + h$$

---

## 6.2 Métodos de un solo paso

Los métodos de un solo paso utilizan exclusivamente la información del punto inmediatamente anterior $(x_n, y_n)$ para proyectar y calcular el valor del siguiente punto $(x_{n+1}, y_{n+1})$.

### 1. Método de Euler (Euler hacia adelante)
Es el método más simple y el punto de partida de todos los esquemas de un solo paso. Utiliza la derivada evaluada en el extremo inicial del intervalo como una aproximación de la pendiente promedio en todo el paso.

* **Fórmula de Recurrencia:**
    $$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$
* **Error:** Su error de truncamiento local es de orden $\mathcal{O}(h^2)$, lo que significa que el error global acumulado es de orden lineal $\mathcal{O}(h)$. Requiere pasos $h$ muy pequeños para ser preciso.



### 2. Método de Euler Mejorado (o Método de Heun)
Mejora la precisión del método de Euler al calcular una pendiente promedio basada en dos extrapolaciones: una pendiente al inicio del intervalo (predictores) y una pendiente estimada al final del intervalo (correctores).

* **Paso Predictor (Euler estándar):**
    $$y_{n+1}^0 = y_n + h \cdot f(x_n, y_n)$$
* **Paso Corrector (Media de pendientes):**
    $$y_{n+1} = y_n + \frac{h}{2} [f(x_n, y_n) + f(x_{n+1}, y_{n+1}^0)]$$
* **Error:** Su error global es de orden cuadrático $\mathcal{O}(h^2)$.

---

## 6.3 Métodos de Runge-Kutta (RK)

Los métodos de Runge-Kutta logran la precisión de una serie de Taylor de orden superior sin necesidad de calcular analíticamente las derivadas de la función. Esto se consigue evaluando la función $f(x, y)$ en varios puntos intermedios dentro de cada paso $h$.

La estructura matemática general para un método RK de orden $m$ es:
$$y_{n+1} = y_n + h \sum_{i=1}^{m} c_i k_i$$

### Método de Runge-Kutta de Cuarto Orden (RK4)
Es el método más popular y utilizado en la ingeniería debido a su excelente balance entre costo computacional y alta precisión. Utiliza cuatro pendientes auxiliares ($k_1, k_2, k_3, k_4$):

* **Fórmulas de las pendientes:**
    $$k_1 = f(x_n, y_n)$$
    $$k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$
    $$k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)$$
    $$k_4 = f(x_n + h, y_n + h k_3)$$

* **Fórmula de combinación final:**
    $$y_{n+1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)$$

* **Error:** Su error global es de cuarto orden, $\mathcal{O}(h^4)$. Si reduces el tamaño de paso $h$ a la mitad, el error se reduce en un factor de $2^4 = 16$.

---

## 6.4 Sistemas de Ecuaciones Diferenciales Ordinarias

Muchos problemas reales involucran múltiples variables interdependientes, lo que da lugar a un sistema de EDOs. Además, cualquier ecuación diferencial de orden superior (como una de segundo orden $y'' + py' + qy = 0$) puede transformarse en un sistema equivalente de ecuaciones de primer orden mediante un cambio de variables.

### Extensión de Métodos a Sistemas Vectoriales
Para resolver un sistema, las fórmulas de aproximación (como Euler o RK4) se aplican de manera **simultánea** en cada paso a todas las ecuaciones involucradas, tratando las variables como vectores:

$$\frac{d\mathbf{y}}{dx} = \mathbf{f}(x, \mathbf{y}) \implies \mathbf{y}_{n+1} = \mathbf{y}_n + h \cdot \mathbf{\Phi}(x_n, \mathbf{y}_n, h)$$

---

## 6.5 Tabla Comparativa de Métodos para EDOs

| Método | Tipo | Evaluaciones por paso | Error Global | Estabilidad | Ideal para... |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Euler Simple** | Un paso | 1 | $\mathcal{O}(h)$ | Baja | Fines didácticos y aproximaciones rápidas. |
| **Heun / Euler Mejorado** | Un paso | 2 | $\mathcal{O}(h^2)$ | Media | Problemas sencillos con curvas suaves. |
| **Runge-Kutta 4 (RK4)** | Un paso | 4 | $\mathcal{O}(h^4)$ | Alta | El estándar general en ciencia e ingeniería. |
| **Métodos Multipaso** | Multipaso | Variable | Alta | Condicionada | Simulación en tiempo real de trayectorias continuas. |

---

## 6.6 Ejemplo de Implementación en Python

El siguiente script en Python compara de manera práctica el desempeño numérico del **Método de Euler** y el **Método RK4** para resolver el PVI de enfriamiento o decaimiento exponencial $\frac{dy}{dx} = -2y$, con condición inicial $y(0) = 1$, cuya solución exacta analítica es $y(x) = e^{-2x}$:

```python
import numpy as np

# 1. Definición del PVI
def f(x, y):
    return -2 * y

def solucion_exacta(x):
    return np.exp(-2 * x)

# 2. Algoritmo del Método de Euler
def euler(f, x0, y0, h, pasos):
    x = np.zeros(pasos + 1)
    y = np.zeros(pasos + 1)
    x[0], y[0] = x0, y0
    
    for n in range(pasos):
        y[n+1] = y[n] + h * f(x[n], y[n])
        x[n+1] = x[n] + h
    return x, y

# 3. Algoritmo del Método Runge-Kutta 4 (RK4)
def rk4(f, x0, y0, h, pasos):
    x = np.zeros(pasos + 1)
    y = np.zeros(pasos + 1)
    x[0], y[0] = x0, y0
    
    for n in range(pasos):
        k1 = f(x[n], y[n])
        k2 = f(x[n] + h/2, y[n] + (h/2)*k1)
        k3 = f(x[n] + h/2, y[n] + (h/2)*k2)
        k4 = f(x[n] + h, y[n] + h*k3)
        
        y[n+1] = y[n] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        x[n+1] = x[n] + h
    return x, y

# Parámetros de simulación
x_inicial, y_inicial = 0, 1
tamano_paso = 0.1
num_pasos = 10

# Ejecución de métodos
x_e, y_e = euler(f, x_inicial, y_inicial, tamano_paso, num_pasos)
x_rk, y_rk = rk4(f, x_inicial, y_inicial, tamano_paso, num_pasos)

# Impresión de resultados contrastados en el punto final
x_final = x_e[-1]
y_real_final = solucion_exacta(x_final)

print(f"--- Solución de EDO en x = {x_final:.1f} ---")
print(f"Valor Real Exacto:   {y_real_final:.6f}")
print(f"Aproximación Euler:  {y_e[-1]:.6f} | Error: {abs(y_real_final - y_e[-1]):.6f}")
print(f"Aproximación RK4:    {y_rk[-1]:.6f} | Error: {abs(y_real_final - y_rk[-1]):.6f}")
