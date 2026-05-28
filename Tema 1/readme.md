TEMA 1: Introducción a los Métodos Numéricos

1.1 Importancia de los métodos numéricos

Los métodos numéricos transforman problemas formulados mediante cálculo, álgebra lineal o ecuaciones diferenciales en operaciones aritméticas simples.Donde la matemática analítica busca una función exacta y = f(x), los métodos numéricos buscan una colección de puntos numéricos (x_i, y_i) que aproximen el comportamiento real con un margen de error controlado. Su importancia radica en que permiten resolver sistemas no lineales o geometrías complejas que no tienen solución exacta por métodos tradicionales.

1.2 Conceptos básicos y sus fórmulas

Cifra significativaEs el número de dígitos que se usan con confianza. Para determinar el número de cifras significativas de un resultado basado en su error, se utiliza el Criterio de Cómputo de Scarboroug:Si se garantiza que el error numérico es menor que un límite preestablecido, el resultado es correcto hasta 
n
 cifras significativas si el error aproximado porcentual cumple con:

<img width="184" height="35" alt="image" src="https://github.com/user-attachments/assets/0ef39f59-c877-4a82-92bd-dc63b8e578ec" />


Exactitud: Proximidad de un valor calculado al valor verdadero. Precisión: Proximidad de los valores calculados entre sí al repetir el método.

<img width="866" height="276" alt="image" src="https://github.com/user-attachments/assets/7eccedbc-b0ba-4e0a-b86c-7663305ac392" />

Incertidumbre y Sesgo

Incertidumbre: Intervalo en el que se asume que se encuentra el valor verdadero:
<img width="128" height="27" alt="image" src="https://github.com/user-attachments/assets/2f6440b6-b858-40c3-9503-31c83558af71" />
(donde U es la incertidumbre).

Sesgo: Error sistemático medido como la diferencia entre la media de los datos calculados.
<img width="123" height="29" alt="image" src="https://github.com/user-attachments/assets/c78bf55a-97a2-413e-b6c4-89ea92be1bbf" />

1.3 Fórmulas analíticas de los Tipos de Errores

En métodos numéricos, los errores se cuantifican de manera absoluta y relativa para evaluar la calidad de la aproximación.1. Error Absoluto (E_t)Es la diferencia numérica directa entre el valor verdadero (E) y el valor aproximado (A):

<img width="343" height="31" alt="image" src="https://github.com/user-attachments/assets/3d6bce2b-1f3b-44b0-8002-20b94e393cc3" />

2.Error Relativo Porcentual Verdadero

Para que el error no dependa de la escala o magnitud de la variable, se normaliza respecto al valor verdadero:

<img width="424" height="52" alt="image" src="https://github.com/user-attachments/assets/0a454273-2029-4038-8aaf-473976c3a927" />

3.Error Relativo Porcentual Aproximado
En problemas reales de ingeniería, no conocemos el valor verdadero. Por lo tanto, el error se calcula comparando la aproximación actual con la aproximación 
obtenida en el paso anterior (esencial en métodos iterativos):

<img width="502" height="54" alt="image" src="https://github.com/user-attachments/assets/492cbf15-f8bf-4ad3-a9f8-35ce2fca29f5" />

Error de Truncamiento (Serie de Taylor)
Ocurre al interrumpir un proceso matemático infinito. La fórmula matemática para modelar cualquier función suave mediante una aproximación polinomial es la Serie de Taylor:

<img width="570" height="52" alt="image" src="https://github.com/user-attachments/assets/92567c96-f6a9-4849-8bef-c0136035b6c6" />

1.4 Software de cómputo numérico

Las operaciones numéricas se ejecutan mediante vectores y matrices usando software que implementa librerías de alto rendimiento (como LAPACK o BLAS).

MATLAB / Octave: Diseñados nativamente para el manejo de arreglos multidimensionales.

Python: Utiliza la librería NumPy, la cual está escrita en C y permite vectorizar operaciones aritméticas, evitando los lentos ciclos for nativos de Python.

1.5 Métodos iterativos y criterios de convergencia

Un método iterativo calcula una secuencia de valores {x_1, x_2, x_3, , x_k} que busca aproximarse a la raíz o solución analítica 

.La ecuación general de recurrencia de un sistema iterativo unidimensional se expresa como:

<img width="113" height="34" alt="image" src="https://github.com/user-attachments/assets/5dcee143-77ac-4fcd-be8c-144c8c35688c" />

Condición de Convergencia (Teorema del Punto Fijo)

Para asegurar que un método iterativo va a aproximarse al resultado correcto en lugar de fallar (divergir), la derivada de la función iterativa g(x) evaluada en la vecindad de la solución debe cumplir con:

<img width="97" height="29" alt="image" src="https://github.com/user-attachments/assets/63b039e5-6d45-4f61-82c3-c7561ac9117b" />

Algoritmos de solucion

Métodos Cerrados (Bracketing Methods)

Requieren de dos valores iniciales (x_l inferior y x_u superior) que encierren a la raíz. Se basan en el Teorema del Valor Intermedio, el cual matemáticamente dice que si una función continua cambia de signo en un intervalo, existe al menos una raíz en ese intervalo:

<img width="227" height="148" alt="image" src="https://github.com/user-attachments/assets/7a2b6330-3fa1-4816-9807-b805d91ea7e9" />

Métodos Abiertos (Open Methods)
No necesitan encerrar la raíz, solo requieren uno o dos valores iniciales de arranque. Son algoritmos mucho más rápidos (convergencia veloz), pero corren el riesgo de divergir (fallar).Algoritmo de Newton-Raphson: Utiliza la recta tangente a la curva en el punto actual para proyectar el siguiente valor sobre el eje 
x
. Es el algoritmo más eficiente si se conoce la derivada.

Fórmula del algoritmo:

<img width="227" height="106" alt="image" src="https://github.com/user-attachments/assets/e5353ff5-4a40-4593-a556-0f8abd4df16d" />


Enunciado del Problema (Control de Calidad en Manufactura)

Un ingeniero de control de calidad está calibrando una máquina automatizada que corta ejes de transmisión para motores. El plano de diseño exige que el diámetro exacto de cada eje sea de 25.00MM (Este es nuestro Valor Verdadero, x).Para evaluar el estado de la máquina, se toma una muestra aleatoria de 5 ejes cortados consecutivamente y se miden con un micrómetro láser de alta precisión. Las lecturas obtenidas son:

<img width="314" height="32" alt="image" src="https://github.com/user-attachments/assets/57ea0333-bedb-4732-a747-2793022c5a55" />

Se solicita:

Calcular el Sesgo de la máquina de corte.Calcular la Incertidumbre de las mediciones utilizando la desviación estándar de la muestra como indicador de la dispersión con un factor de cobertura básico .Determinar si el problema de la máquina es de Exactitud o de Precisión.

<img width="1097" height="576" alt="image" src="https://github.com/user-attachments/assets/a165570c-af38-45ee-8124-e39218f6804f" />

Código en Python para Automatizar el Análisis

Este script procesa los datos, calcula los componentes de error y genera un reporte limpio en la terminal.

import numpy as np

def analizar_mediciones(datos, valor_verdadero): """ Calcula el sesgo, la media y la incertidumbre (desviación estándar) de un conjunto de datos experimentales. """ datos = np.array(datos, dtype=float) n = len(datos)

   # 1. Calcular la media aritmética
   media = np.mean(datos)
  
  # 2. Calcular el Sesgo (Error Sistemático)
  sesgo = media - valor_verdadero
  
  # 3. Calcular la Incertidumbre basada en la Desviación Estándar Muestral (ddof=1 para n-1)
  incertidumbre = np.std(datos, ddof=1)
  
  # Imprimir Reporte Técnico
  print("=" * 50)
  print("        REPORTE DE INCERTIDUMBRE Y SESGO")
  print("=" * 50)
  print(f"Número de muestras analizadas : {n}")
  print(f"Valor Nominal (Verdadero)     : {valor_verdadero:.2f} mm")
  print(f"Media de las lecturas         : {media:.2f} mm")
  print("-" * 50)
  print(f"SESGO DETECTADO               : {sesgo:+.2f} mm")
  print(f"INCERTIDUMBRE (Dispersión)    : ±{incertidumbre:.2f} mm")
  print("-" * 50)
  
  # Diagnóstico automatizado de Calidad
  print("DIAGNÓSTICO DEL PROCESO:")
  if abs(sesgo) > 0.05 and incertidumbre <= 0.03:
      print("-> El sistema es PRECISO pero INEXACTO (Alto Sesgo, Baja Incertidumbre).")
      print("   Acción: Calibrar el punto cero / offset de la máquina.")
  elif abs(sesgo) <= 0.05 and incertidumbre > 0.05:
      print("-> El sistema es EXACTO pero IMPRECISO (Bajo Sesgo, Alta Incertidumbre).")
      print("   Acción: Revisar vibraciones o rigidez estructural del equipo.")
  elif abs(sesgo) <= 0.05 and incertidumbre <= 0.03:
      print("-> El sistema es EXACTO Y PRECISO. Operación óptima.")
  else:
      print("-> El sistema es INEXACTO E IMPRECISO. Requiere mantenimiento general.")
  print("=" * 50)
  
  # --- Datos del Problema ---
  lecturas_ejes = [25.12, 25.15, 25.10, 25.14, 25.14]
  valor_diseno = 25.00
  
  # Ejecución del programa
  analizar_mediciones(lecturas_ejes, valor_diseno)
  
  #Salida
  
  #Número de muestras analizadas : 5
  #Valor Nominal (Verdadero)     : 25.00 mm
  #Media de las lecturas         : 25.13 mm
  
  #SESGO DETECTADO               : +0.13 mm
  #INCERTIDUMBRE (Dispersión)    : ±0.02 mm
  #DIAGNÓSTICO DEL PROCESO:
  
  
