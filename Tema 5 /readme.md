# Unidad 5: Interpolación y Ajuste de Funciones

Esta sección del repositorio está dedicada al estudio de técnicas avanzadas para aproximar funciones y modelar el comportamiento de conjuntos de datos. Se profundiza en métodos alternativos de interpolación polinomial, el uso de trazadores (*splines*) para evitar oscilaciones severas y el ajuste de curvas mediante regresión por mínimos cuadrados cuando los datos contienen ruido experimental.

---

## 5.1 Diferencias divididas de Newton

El método de interpolación polinomial de Newton es una alternativa al método de Lagrange. Aunque ambos generan exactamente el mismo polinomio único de grado $n$ para un conjunto de puntos, la ventaja de Newton radica en que es **computacionalmente eficiente**: permite añadir nuevos puntos de datos sin tener que recalcular todo el polinomio desde cero.

### Fórmula del Polinomio de Newton
Un polinomio de grado $n$ se expresa en forma secuencial como:
$$P_n(x) = b_0 + b_1(x - x_0) + b_2(x - x_0)(x - x_1) + \dots + b_n(x - x_0)(x - x_1)\dots(x - x_{n-1})$$

Donde los coeficientes $b_i$ corresponden a las **diferencias divididas** de la función, denotadas por corchetes:
* $b_0 = f[x_0] = y_0$
* $b_1 = f[x_1, x_0] = \frac{f(x_1) - f(x_0)}{x_1 - x_0}$
* $b_2 = f[x_2, x_1, x_0] = \frac{f[x_2, x_1] - f[x_1, x_0]}{x_2 - x_0}$

### Algoritmo de la Tabla de Diferencias Divididas
Los cálculos se organizan de forma piramidal en una tabla como la siguiente para construir los coeficientes:

| $x_i$ | $y_i$ | Primeras Diferencias | Segundas Diferencias | Terceras Diferencias |
| :---: | :---: | :---: | :---: | :---: |
| $x_0$ | **$y_0$** | | | |
| | | **$f[x_1, x_0]$** | | |
| $x_1$ | $y_1$ | | **$f[x_2, x_1, x_0]$** | |
| | | $f[x_2, x_1]$ | | **$f[x_3, x_2, x_1, x_0]$** |
| $x_2$ | $y_2$ | | $f[x_3, x_2, x_1]$ | |
| | | $f[x_3, x_2]$ | | |
| $x_3$ | $y_3$ | | | |

*Nota: Los coeficientes $b_0, b_1, \dots, b_n$ necesarios para la fórmula polinomial corresponden a los elementos de la **diagonal superior** de la tabla (resaltados en negrita).*

---

## 5.2 Interpolación mediante trazadores (Splines)

Cuando se incrementa el número de puntos a interpolar, el grado del polinomio global aumenta automáticamente. Esto suele provocar el **Fenómeno de Runge**: una serie de oscilaciones salvajes y destructivas en los extremos del intervalo que arruinan la precisión de la aproximación.

Para solucionar esto, la **interpolación por trazadores (Splines)** no utiliza un solo polinomio para todos los datos, sino que conecta cada par de puntos contiguos $(x_i, y_i)$ y $(x_{i+1}, y_{i+1})$ mediante un polinomio local de grado bajo (generalmente cúbico), garantizando un acoplamiento suave en los nodos de unión.



### Trazadores Cúbicos (Cubic Splines)
Para un conjunto de $n+1$ puntos, se definen $n$ polinomios cúbicos de la forma:
$$S_i(x) = a_i(x - x_i)^3 + b_i(x - x_i)^2 + c_i(x - x_i) + d_i \quad \text{para } x \in [x_i, x_{i+1}]$$

Para asegurar la suavidad visual y física de la curva curva, se imponen de manera rigurosa las siguientes condiciones de continuidad en los nodos internos:
1.  **Continuidad de la función:** Los polinomios adyacentes deben tocar el mismo punto común ($S_i(x_{i+1}) = S_{i+1}(x_{i+1})$).
2.  **Continuidad de la primera derivada:** La pendiente o velocidad de la curva debe ser idéntica en el punto de unión ($S_i'(x_{i+1}) = S_{i+1}'(x_{i+1})$).
3.  **Continuidad de la segunda derivada:** La concavidad o aceleración debe ser idéntica en el punto de unión ($S_i''(x_{i+1}) = S_{i+1}''(x_{i+1})$).

---

## 5.3 Ajuste de curvas por mínimos cuadrados

A diferencia de la interpolación (donde la curva debe pasar **obligatoriamente por encima** de todos los puntos), en el **ajuste de funciones** se asume que los datos provienen de experimentos o mediciones reales y contienen ruido o errores aleatorios. Por lo tanto, el objetivo es encontrar una curva de tendencia general que minimice la distancia global hacia todos los puntos.

### 1. Regresión Lineal Simple
Busca ajustar los datos a una línea recta de la forma $y = a_1 x + a_0$. Para lograrlo, el método minimiza la suma de los cuadrados de los residuos ($S_r$):
$$S_r = \sum_{i=1}^{n} (y_i - (a_1 x_i + a_0))^2$$

Los coeficientes óptimos se calculan directamente resolviendo las **ecuaciones normales**:
$$a_1 = \frac{n \sum (x_i y_i) - \sum x_i \sum y_i}{n \sum x_i^2 - (\sum x_i)^2}$$
$$a_0 = \bar{y} - a_1 \bar{x}$$

### 2. Regresión Polinomial y Modelos No Lineales
Cuando la tendencia de los datos no es rectilínea, se puede extender el criterio de mínimos cuadrados a polinomios de grado superior ($y = a_0 + a_1 x + a_2 x^2$) o linealizar ecuaciones mediante transformaciones algebraicas:
* **Modelo Exponencial ($y = \alpha e^{\beta x}$):** Se aplica logaritmo natural a ambos lados $\ln(y) = \ln(\alpha) + \beta x$, reduciéndolo a una ecuación lineal estándar donde $Y = \ln(y)$, $A_0 = \ln(\alpha)$ y $A_1 = \beta$.

---

## 5.4 Tabla Comparativa: Interpolación vs. Ajuste

| Criterio | Interpolación Polinomial / Splines | Ajuste por Mínimos Cuadrados |
| :--- | :--- | :--- |
| **Paso por los puntos** | Pasa **exactamente** por cada uno de los puntos dados. | No pasa necesariamente por los puntos; busca una tendencia global. |
| **Naturaleza de los datos** | Datos analíticos exactos, tablas matemáticas o de ingeniería sin ruido. | Datos experimentales con errores de medición o fluctuaciones. |
| **Grado de la función** | Elevado si hay muchos puntos (excepto en Splines). | Bajo e independiente del número de puntos de datos ($N$). |
| **Riesgos** | Propenso a oscilaciones severas si se usa un solo polinomio alto. | Malinterpretar la tendencia si se elige un modelo físico erróneo. |

---

## 5.5 Ejemplo de Implementación en Python

El siguiente script en Python utiliza la librería `SciPy` y `NumPy` para contrastar un ajuste por **Mínimos Cuadrados (Regresión)** frente a una interpolación por **Trazadores Cúbicos**:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 1. Definición de datos experimentales con ruido
x_datos = np.array([0, 1, 2, 3, 4, 5, 6])
y_datos = np.array([0.5, 2.1, 3.8, 4.2, 5.9, 8.3, 9.1])

# 2. Interpolación por Trazadores Cúbicos (Spline)
spline = CubicSpline(x_datos, y_datos)

# 3. Ajuste por Mínimos Cuadrados (Línea Recta - Polinomio Grado 1)
coef_recta = np.polyfit(x_datos, y_datos, 1)
funcion_recta = np.poly1d(coef_recta)

# 4. Generación de puntos densos para graficar las curvas continuas
x_continuo = np.linspace(0, 6, 200)

print("--- Análisis de Ajuste de Funciones ---")
print(f"Ecuación de la recta ajustada: y = {coef_recta[0]:.4f}x + {coef_recta[1]:.4f}")

# Código base opcional para visualización gráfica en entorno local:
# plt.scatter(x_datos, y_datos, color='red', label='Datos Experimentales')
# plt.plot(x_continuo, spline(x_continuo), label='Spline Cúbico (Interpolación)', color='blue')
# plt.plot(x_continuo, funcion_recta(x_continuo), label='Mínimos Cuadrados (Ajuste)', linestyle='--', color='green')
# plt.legend()
# plt.show()
