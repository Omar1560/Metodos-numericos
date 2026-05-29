# Unidad 2: Métodos Numéricos para la Resolución de Ecuaciones e Interpolación

Este repositorio contiene el desarrollo teórico, matemático y práctico de los temas correspondientes a la segunda unidad de Métodos Numéricos. Incluye definiciones rigurosas, fórmulas fundamentales, explicaciones algorítmicas y ejemplos resueltos paso a paso.

---

## 2.1 Métodos de intervalo

### Definición y Fundamento Teórico
Los métodos de intervalo (también conocidos como métodos cerrados o racheadores) se basan en el principio de que una función continua cambia de signo en la vecindad de una raíz real. Estos métodos requieren obligatoriamente de dos valores iniciales (un límite inferior y uno superior) que "encierren" o hagan un sándwich a la raíz.

El fundamento matemático detrás de estos algoritmos es el **Teorema del Valor Intermedio** (específicamente el **Teorema de Bolzano**), el cual establece lo siguiente:

> Si una función $f(x)$ es continua en un intervalo cerrado $[a, b]$ y el producto de sus imágenes en los extremos tiene signos opuestos, es decir:
> 
> $$f(a) \cdot f(b) < 0$$
> 
> Entonces existe al menos una raíz real $\xi$ (xi) dentro del intervalo $(a, b)$ tal que $f(\xi) = 0$.

### Características Principales
* **Convergencia Asegurada:** Al encerrar la raíz en un intervalo con cambio de signo, el método siempre convergerá a una solución.
* **Velocidad de Convergencia:** Generalmente son más lentos en comparación con los métodos abiertos (como Newton-Raphson), pero son significativamente más robustos y no divergen.
* **Limitaciones:** No pueden detectar raíces dobles o de multiplicidad par donde la función toca el eje $X$ pero no lo cruza, ya que en esos puntos no ocurre un cambio de signo.

---

## 2.2 Método de bisección

### Definición
Es el algoritmo de búsqueda de raíces más simple y confiable dentro de los métodos de intervalo. Consiste en dividir sistemáticamente el intervalo a la mitad hasta que el tamaño del subintervalo sea menor que una tolerancia predefinida.



### Fórmulas y Algoritmo
Dado un intervalo inicial $[X_l, X_u]$ (donde $l$ es *lower*/inferior y $u$ es *upper*/superior), tal que $f(X_l) \cdot f(X_u) < 0$:

1.  **Calcular el punto medio** (que funciona como la aproximación de la raíz, $X_r$):
    $$X_r = \frac{X_l + X_u}{2}$$

2.  **Evaluar los subintervalos** para determinar dónde se encuentra la raíz mediante los siguientes criterios:
    * Si $f(X_l) \cdot f(X_r) < 0$: La raíz está en el subintervalo inferior. Se actualiza el límite superior: `X_u = X_r`.
    * Si $f(X_l) \cdot f(X_r) > 0$: La raíz está en el subintervalo superior. Se actualiza el límite inferior: `X_l = X_r`.
    * Si $f(X_l) \cdot f(X_r) = 0$: Se encontró la raíz exacta; el algoritmo termina.

3.  **Calcular el error relativo aproximado porcentual** para evaluar el criterio de parada:
    $$|\varepsilon_a| = \left| \frac{X_{r,\text{nuevo}} - X_{r,\text{anterior}}}{X_{r,\text{nuevo}}} \right| \times 100\%$$

El proceso se repite iterativamente hasta que $|\varepsilon_a| < \varepsilon_s$ (tolerancia propuesta).

### Ejemplo Práctico Resuelto
**Problema:** Encontrar la raíz real de la función $f(x) = x^3 - x - 2$ en el intervalo $[1, 2]$ con una tolerancia de error inferior al $10\%$.

| Iteración | $X_l$ (Inferior) | $X_u$ (Superior) | $X_r$ (Punto Medio) | $f(X_l)$ | $f(X_r)$ | $f(X_l) \cdot f(X_r)$ | $|\varepsilon_a| (\%)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 1.0000 | 2.0000 | 1.5000 | -2.0000 | -0.1250 | +0.2500 ($>0$) | --- |
| **2** | 1.5000 | 2.0000 | 1.7500 | -0.1250 | 1.6094 | -0.2012 ($<0$) | 14.28% |
| **3** | 1.5000 | 1.7500 | 1.6250 | -0.1250 | 0.6660 | -0.0833 ($<0$) | **7.69%** |

**Resultado:** Tras 3 iteraciones, la aproximación de la raíz es **$X_r = 1.6250$** con un error estimado del **$7.69\%$**, cumpliendo exitosamente con la tolerancia establecida.

---

## 2.3 Método de aproximaciones sucesivas

### Definición
También conocido como **Método de Punto Fijo**, es un método abierto que no requiere encerrar la raíz bajo un intervalo. Se basa en transformar algebraicamente la ecuación original $f(x) = 0$ en una forma equivalente:

$$x = g(x)$$

Un punto fijo de la función $g(x)$ es un valor de $x$ para el cual se cumple la igualdad, coincidiendo exactamente con la raíz de la función original $f(x)$.

### Fórmula de Iteración
A partir de un valor semilla o inicial $X_0$, la ecuación de recurrencia para calcular los siguientes puntos es:

$$X_{n+1} = g(X_n)$$

### Criterio de Convergencia
Este método no siempre converge. Para asegurar que los valores no se disparen al infinito, la derivada de la función de iteración $g(x)$ debe cumplir con la condición de ser una contracción en el entorno de la raíz:

$$|g'(x)| < 1$$

### Ejemplo Práctico Resuelto
**Problema:** Resolver la ecuación $x^2 - 3x + 1 = 0$ usando el valor inicial $X_0 = 0$.

1.  **Despejar $x$ para obtener $g(x)$:**
    $$3x = x^2 + 1 \implies g(x) = \frac{x^2 + 1}{3}$$
2.  **Validar convergencia:**
    $$g'(x) = \frac{2x}{3} \implies |g'(0)| = 0 < 1 \quad \text{(Garantiza convergencia)}$$

| Iteración ($n$) | $X_n$ | $X_{n+1} = g(X_n)$ | Error Absoluto $|X_{n+1} - X_n|$ |
| :---: | :---: | :---: | :---: |
| **0** | 0.0000 | 0.3333 | 0.3333 |
| **1** | 0.3333 | 0.3704 | 0.0371 |
| **2** | 0.3704 | 0.3790 | 0.0086 |
| **3** | 0.3790 | **0.3812** | **0.0022** |

**Resultado:** El valor de la raíz tiende a estabilizarse rápidamente en torno a **$0.3812$**.

---

## 2.4 Métodos de interpolación

### Definición
La interpolación es el proceso matemático mediante el cual se construye una función (normalmente un polinomio) que pasa **exactamente** por un conjunto de puntos de datos discretos conocidos $(x_i, y_i)$. Se utiliza para estimar valores intermedios donde no se dispone de mediciones reales.

### 1. Interpolación Lineal
Es la forma más simple de interpolación. Consiste en conectar dos puntos contiguos $(x_0, y_0)$ y $(x_1, y_1)$ mediante una línea recta.

$$f(x) = y_0 + \frac{y_1 - y_0}{x_1 - x_0}(x - x_0)$$

### 2. Interpolación Polinomial de Lagrange
Evita tener que calcular explícitamente los coeficientes de un sistema de ecuaciones mediante el uso de polinomios base de Lagrange $L_i(x)$.

$$P_n(x) = \sum_{i=0}^{n} L_i(x) \cdot y_i$$

Donde los coeficientes de base se calculan como productos combinados:

$$L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$$



### Ejemplo Práctico (Lagrange de Grado 1)
**Datos dados:** $(x_0=1, y_0=2)$ y $(x_1=4, y_1=7)$. Se requiere interpolar el valor estimado cuando **$x = 2$**.

1.  **Calcular los polinomios base $L_0$ y $L_1$:**
    $$L_0(2) = \frac{2 - 4}{1 - 4} = \frac{-2}{-3} = \frac{2}{3}$$
    $$L_1(2) = \frac{2 - 1}{4 - 1} = \frac{1}{3}$$

2.  **Construir el polinomio final $P_1(2)$:**
    $$P_1(2) = \left(\frac{2}{3}\right)(2) + \left(\frac{1}{3}\right)(7) = \frac{4}{3} + \frac{7}{3} = \frac{11}{3} \approx 3.6667$$

---

## 2.5 Aplicaciones

Los métodos numéricos estudiados en esta unidad tienen un impacto directo en la resolución de problemas reales de ingeniería y ciencias:

* **Ingeniería Química e Industrial:** Cálculo del factor de compresibilidad de gases reales empleando ecuaciones de estado no lineales complejas (como *Van der Waals* o *Redlich-Kwong*). Como el despeje analítico del volumen o la presión es imposible, se emplean algoritmos de bisección o punto fijo.
* **Análisis de Estructuras (Ingeniería Civil):** Determinación de las curvas de deflexión y puntos de máxima tensión en vigas o puentes sometidos a cargas variables a través de la interpolación polinomial de los datos arrojados por sensores físicos.
* **Ciencias de la Computación y Gráficos:** Renderizado de curvas suaves y modelado en 3D a través de puntos de control definidos empleando interpolaciones por trazadores (*splines*), optimizando el rendimiento gráfico con baja carga computacional.
