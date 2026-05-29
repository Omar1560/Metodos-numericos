# Unidad 1: Introducción a los Métodos Numéricos

Este repositorio contiene el desarrollo teórico, matemático y conceptual de los temas correspondientes a la primera unidad de Métodos Numéricos. En esta sección se sientan las bases sobre la teoría de errores, aproximaciones, software de cómputo y la naturaleza de los algoritmos iterativos.

---

## 1.1 Importancia de los métodos numéricos

### Definición y Contexto
Los métodos numéricos son técnicas mediante las cuales es posible formular problemas matemáticos de tal manera que puedan resolverse utilizando operaciones aritméticas elementales (sumas, restas, multiplicaciones y divisiones). 

Antes de la llegada de las computadoras modernas, los ingenieros y científicos dependían exclusivamente de métodos analíticos (soluciones exactas mediante álgebra y cálculo) o métodos gráficos. Sin embargo, muchos problemas del mundo real involucran sistemas de ecuaciones no lineales complejas, geometrías irregulares o comportamientos físicos que no tienen una solución analítica cerrada.

### ¿Por qué son cruciales en la ingeniería moderna?
* **Resolución de Sistemas Complejos:** Permiten resolver sistemas con miles de ecuaciones lineales o ecuaciones diferenciales parciales que modelan fenómenos físicos reales.
* **Simulación y Prototipado Virtual:** Facilitan el diseño de software de simulación estructural, dinámica de fluidos (CFD) y optimización de procesos sin necesidad de construir costosos prototipos físicos.
* **Adaptabilidad Computacional:** Reducen problemas de cálculo infinitesimal a algoritmos iterativos lógicos que pueden ser ejecutados a gran velocidad por microprocesadores.

---

## 1.2 Conceptos básicos: cifra significativa, precisión, exactitud, incertidumbre y sesgo

Para garantizar la confiabilidad de cualquier aproximación numérica, es indispensable dominar los conceptos que rigen la teoría de la medición y el error.

### 1. Cifras Significativas
Son los dígitos de un número que se consideran confiables o que tienen un significado físico real. El concepto es fundamental en los métodos numéricos porque los sistemas informáticos representan los números con una cantidad finita de bits, lo que introduce de forma inherente errores de redondeo.
* **Regla general:** Un método numérico asegura un resultado con $n$ cifras significativas si el error estimado cumple con la condición:
  $$\varepsilon_s = (0.5 \times 10^{2-n})\%$$

### 2. Exactitud vs. Precisión
* **Exactitud (*Accuracy*):** Se refiere a qué tan cercano está el valor calculado o medido respecto al **valor verdadero** o real del fenómeno.
* **Precisión (*Precision*):** Se refiere a la repetibilidad o qué tan cercanos están los valores calculados entre sí cuando se realiza la misma operación de manera sucesiva.


### 3. Incertidumbre y Sesgo
* **Incertidumbre:** Es la dispersión o el grado de duda asociado al resultado de un cálculo o medición. Cuantifica el rango dentro del cual se espera que se encuentre el valor real.
* **Sesgo (*Bias*):** Es un error sistemático que causa que los resultados se desvíen constantemente en una dirección específica lejos del valor verdadero. Un algoritmo con un alto sesgo arrojará resultados inexactos de manera consistente.

---

## 1.3 Tipos de errores

En el análisis numérico, el error total de un modelo es la suma de diferentes componentes inherentes al proceso de modelado y computación.

### Fórmulas del Error Fundamentales
* **Error Verdadero ($E_v$):**
  $$E_v = \text{Valor Verdadero} - \text{Valor Aproximado}$$
* **Error Relativo Verdadero Fraccionario ($\varepsilon_v$):**
  $$\varepsilon_v = \frac{\text{Valor Verdadero} - \text{Valor Aproximado}}{\text{Valor Verdadero}}$$
* **Error Normalizado Aproximado ($\varepsilon_a$):** Se utiliza cuando no se conoce el valor real (lo común en ingeniería), comparando la aproximación actual con la anterior:
  $$\varepsilon_a = \left| \frac{\text{Aproximación Actual} - \text{Aproximación Anterior}}{\text{Aproximación Actual}} \right| \times 100\%$$

### Clasificación de Errores por su Origen
1.  **Errores de Truncamiento:** Son aquellos causados por interrumpir un proceso matemático infinito y reemplazarlo por un procedimiento finito. El ejemplo clásico es aproximar una función continua mediante un número limitado de términos de la **Serie de Taylor**:
    $$f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2$$
2.  **Errores de Redondeo:** Se originan debido a que las computadoras no pueden representar ciertos números de forma exacta (como $\pi$, $e$ o fracciones continuas). Al usar el estándar de punto flotante (IEEE 754), los decimales sobrantes se eliminan o redondean al bit más cercano.
3.  **Errores Inherentes o de Datos:** Son los errores preexistentes en los datos de entrada del problema, provenientes usualmente de las limitaciones de precisión de los instrumentos de medición física.

---

## 1.4 Software de cómputo numérico

La implementación de métodos numéricos requiere herramientas de software optimizadas para el procesamiento de matrices y álgebra lineal de alto rendimiento.

| Tipo de Software | Herramientas Principales | Características Clave |
| :--- | :--- | :--- |
| **Entornos Propietarios** | `MATLAB` | Excelente soporte comercial, Toolboxes especializadas, optimización nativa para operaciones matriciales y gráficos avanzados. |
| **Alternativas Open-Source** | `GNU Octave`, `Scilab` | Compatibilidad sintáctica muy alta con MATLAB, sin costo de licenciamiento, ideales para entornos académicos y scripts ligeros. |
| **Lenguajes de Programación** | `Python` (con `NumPy`, `SciPy`, `Matplotlib`) | El estándar actual en ciencia de datos e ingeniería. Sintaxis limpia, librerías robustas y alta velocidad de ejecución gracias a bindings en C/Fortran. |

---

## 1.5 Métodos iterativos

### Definición y Mecanismo
Un método iterativo es un algoritmo matemático que genera una secuencia de aproximaciones sucesivas para resolver un problema, partiendo desde una estimación inicial llamada **valor semilla** ($X_0$). 

A diferencia de los métodos directos (como la eliminación Gaussiana, que calcula la solución exacta en un número fijo de pasos), los métodos iterativos repiten un bucle de cálculo con el objetivo de aproximarse progresivamente a la solución correcta.

### Criterio de Convergencia y Parada
Un método iterativo se considera **convergente** si los resultados sucesivos se acercan cada vez más a la solución verdadera conforme avanza el número de iteraciones. El proceso se detiene cuando se cumple alguna de las siguientes condiciones de paro:

1.  **Tolerancia de Error Alcanzada:** El error aproximado calculado es menor que el límite permitido:
    $$|\varepsilon_a| < \varepsilon_s$$
2.  **Límite de Iteraciones (Criterio de Resguardo):** Se alcanza un número máximo de iteraciones predefinido (`max_iter`). Esto evita que el programa se quede atrapado en un bucle infinito en caso de que el método sea **divergente** (es decir, que los valores se disparen hacia el infinito).

```python
# Ejemplo de estructura lógica de un método iterativo en Python
def metodo_iterativo(valor_inicial, tolerancia, max_iter):
    x_ant = valor_inicial
    for iteracion in range(1, max_iter + 1):
        # Aplicación de la función de recurrencia g(x)
        x_nuevo = g(x_ant) 
        
        # Cálculo del error aproximado
        error = abs((x_nuevo - x_ant) / x_nuevo) * 100
        
        if error < tolerancia:
            print(f"Convergencia alcanzada en la iteración {iteracion}")
            return x_nuevo
            
        x_ant = x_nuevo
    print("El método no convergió dentro del límite de iteraciones.")
    return None
