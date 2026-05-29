# Unidad 3: Métodos de Solución de Sistemas de Ecuaciones

Esta sección del repositorio está dedicada al estudio de los métodos numéricos utilizados para resolver sistemas de ecuaciones lineales (SEL) de la forma $A \mathbf{x} = \mathbf{b}$. Se abordan tanto los métodos directos (exactos en ausencia de errores de redondeo) como los métodos iterativos (aproximaciones sucesivas).

---

## 3.1 Importancia de los sistemas de ecuaciones lineales

En la ingeniería y las ciencias aplicadas, la mayoría de los fenómenos físicos continuos que se modelan mediante ecuaciones diferenciales se transforman, tras un proceso de discretización, en un sistema de ecuaciones lineales.

### Áreas de Aplicación Comunes
* **Análisis de Estructuras:** Cálculo de fuerzas internas y reacciones en armaduras estáticas y marcos estructurales (matrices de rigidez).
* **Circuitos Eléctricos:** Aplicación de las leyes de Kirchhoff para determinar corrientes y voltajes en redes eléctricas complejas.
* **Redes de Flujo:** Modelado de la distribución de presiones y caudales en redes de tuberías de agua o gas.
* **Procesamiento de Imágenes y Gráficos:** Transformaciones geométricas, interpolaciones bidimensionales y filtrado digital de datos.

---

## 3.2 Métodos directos

Los métodos directos son algoritmos que determinan la solución exacta de un sistema de ecuaciones en un número finito de pasos algebraicos predecibles, asumiendo que no existen errores de redondeo computacional.

### 1. Eliminación Gaussiana Simple
Consiste en transformar la matriz de coeficientes original $A$ en una matriz triangular superior mediante operaciones elementales entre renglones. Una vez obtenida la forma triangular, las incógnitas se calculan de abajo hacia arriba mediante un proceso de **sustitución hacia atrás**.

Dado el sistema:
$$\begin{bmatrix} a_{11} & a_{12} & a_{13} \\ 0 & a_{22}' & a_{23}' \\ 0 & 0 & a_{33}'' \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2' \\ b_3'' \end{bmatrix}$$

La última variable se despeja directamente: $x_3 = b_3'' / a_{33}''$, y se sustituye recursivamente en los renglones superiores.

### 2. Eliminación de Gauss-Jordan
Es una variación de la eliminación gaussiana. En este método, las operaciones elementales se aplican de tal manera que la matriz de coeficientes se transforma en una **matriz identidad** ($I$). 

$$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} d_1 \\ d_2 \\ d_3 \end{bmatrix}$$

* **Ventaja:** No requiere sustitución hacia atrás; las soluciones aparecen directamente en el vector de términos independientes.
* **Desventaja:** Requiere aproximadamente un $50\%$ más de operaciones aritméticas que la eliminación gaussiana simple, lo que la hace menos eficiente para sistemas grandes.

### 3. Estrategias de Pivoteo (Pivoteo Parcial)
Durante la eliminación, si un elemento de la diagonal principal (el pivote $a_{kk}$) es muy cercano o igual a cero, la división por este término genera un error desastroso o una división entre cero.

Para evitarlo, se aplica el **Pivoteo Parcial**: antes de eliminar los términos de una columna, se busca el elemento con el mayor valor absoluto en esa misma columna (debajo del renglón actual) y se intercambian los renglones correspondientes. Esto minimiza drásticamente la propagación de los errores de redondeo.

---

## 3.3 Métodos iterativos

Los métodos iterativos obtienen la solución de un sistema mediante aproximaciones sucesivas partiendo de un vector inicial $\mathbf{x}^{(0)}$. Son preferibles para sistemas de ecuaciones gigantescos (miles o millones de variables) o matrices dispersas (aquellas con la mayoría de sus elementos iguales a cero), donde los métodos directos consumirían demasiada memoria RAM.

### Criterio de Convergencia: Diagonal Dominante
Para garantizar que un método iterativo converja a la solución única, la matriz de coeficientes $A$ debe ser **estrictamente dominante por diagonales**. Esto significa que en cada renglón, el valor absoluto del elemento de la diagonal principal debe ser mayor que la suma de los valores absolutos de los demás elementos del mismo renglón:

$$|a_{ii}| > \sum_{j \neq i} |a_{ij}|$$

### 1. Método de Jacobi
En este algoritmo, se despeja la variable $x_i$ de la ecuación $i$. Para calcular los valores de la iteración nueva $(k+1)$, se utilizan **únicamente** los valores obtenidos en la iteración anterior $(k)$:

$$x_i^{(k+1)} = \frac{b_i - \sum_{j \neq i} a_{ij} x_j^{(k)}}{a_{ii}}$$

### 2. Método de Gauss-Seidel
Es una optimización directa del método de Jacobi. Consiste en utilizar de manera inmediata los valores de las variables recién calculados en la iteración actual $(k+1)$ en lugar de esperar hasta el siguiente ciclo:

$$x_i^{(k+1)} = \frac{b_i - \sum_{j < i} a_{ij} x_i^{(k+1)} - \sum_{j > i} a_{ij} x_j^{(k)}}{a_{ii}}$$

* **Ventaja:** Generalmente converge el doble de rápido que el método de Jacobi.



---

## 3.4 Comparativa de Métodos

| Característica | Métodos Directos (Gauss / Gauss-Jordan) | Métodos Iterativos (Jacobi / Gauss-Seidel) |
| :--- | :--- | :--- |
| **Tipo de Solución** | Exacta (limitada solo por redondeo). | Aproximada (sujeta a una tolerancia $\varepsilon_s$). |
| **Número de Pasos** | Fijo y finito, dependiente del tamaño $N$. | Variable, dependiente de la convergencia. |
| **Ideal para...** | Sistemas pequeños o medianos y matrices densas. | Sistemas masivos y matrices dispersas (*sparse*). |
| **Uso de Memoria** | Alto (requiere almacenar y modificar la matriz). | Bajo (mantiene la estructura original intacta). |

---

## 3.5 Ejemplo de Implementación Algorítmica

A continuación se presenta una implementación base del método iterativo de **Gauss-Seidel** en Python utilizando arreglos de `NumPy`:

```python
import numpy as np

def gauss_seidel(A, b, x0, tol=1e-5, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)
    
    for k in range(max_iter):
        x_old = np.copy(x)
        
        for i in range(n):
            # Suma de los términos correspondientes a la fila i
            suma = b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = suma / A[i, i]
            
        # Calcular el error relativo aproximado
        error = np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
        
        if error < tol:
            print(f"✓ Convergencia exitosa en {k+1} iteraciones.")
            return x
            
    print("⚠ Se alcanzó el máximo de iteraciones sin converger.")
    return x

# Ejemplo de uso con una matriz diagonal dominante
A_matriz = [[4, 1, 2],
            [1, 5, 1],
            [1, 1, 3]]
b_vector = [9, 12, 11]
x_inicial = [0, 0, 0]

solucion = gauss_seidel(A_matriz, b_vector, x_inicial)
print("Solución aproximada:", solucion)
