1. -- Introducción a los Métodos Numéricos --

Los métodos numéricos son técnicas matemáticas que permiten obtener soluciones aproximadas a problemas que, generalmente, no tienen solución analítica exacta o cuya solución es muy difícil de calcular de forma directa. Se basan en algoritmos sistemáticos que transforman un problema matemático complejo en una serie de operaciones aritméticas simples, factibles de ejecutar con computadoras.

Históricamente, estos métodos existieron mucho antes de las computadoras modernas. Matemáticos como Newton, Euler, Gauss y Runge desarrollaron muchos de los algoritmos que hoy en día siguen siendo la base de la computación científica. Sin embargo, fue la aparición de las computadoras digitales lo que permitió aplicarlos a problemas de escala real en ingeniería, física, biología y economía.

-- Definición formal --

Un método numérico es un procedimiento algorítmico que aproxima la solución de un problema matemático mediante un número finito de operaciones aritméticas, produciendo un resultado con un error controlado y medible

1.1 Importancia de los Métodos Numéricos

La importancia de los métodos numéricos radica en su capacidad para resolver problemas del mundo real que de otro modo serían intratables. En prácticamente todas las ramas de la ingeniería y las ciencias aplicadas, los modelos matemáticos conducen a ecuaciones que no admiten solución analítica cerrada.

¿Por qué son necesarios los métodos numéricos?

•	La mayoría de las ecuaciones diferenciales ordinarias y parciales que modelan fenómenos físicos reales no tienen solución analítica.
•	Los sistemas de ecuaciones lineales de gran dimensión, provenientes de la discretización de modelos continuos, requieren algoritmos eficientes.
•	La integración y diferenciación numérica son esenciales cuando se trabaja con datos experimentales discretos

<img width="626" height="276" alt="image" src="https://github.com/user-attachments/assets/ab1c59fc-e18e-422b-a1ff-b897b94110c8" />

1.2 Conceptos Básicos

Antes de profundizar en los métodos numéricos, es fundamental comprender los conceptos básicos que se utilizan para describir la calidad y confiabilidad de los resultados obtenidos. Estos conceptos permiten evaluar y comparar distintos métodos entre sí.

1.2.1 Cifras Significativas

Las cifras significativas (o dígitos significativos) son los dígitos de un número que tienen significado físico o matemático en el contexto de una medición o cálculo. Son todos los dígitos que se conocen con certeza más el primero que es incierto.

<img width="628" height="196" alt="image" src="https://github.com/user-attachments/assets/c29a86e9-f312-4627-8b72-d81be6739a1d" />

1.2.2 Precisión vs. Exactitud

En el contexto de los métodos numéricos, es crucial distinguir entre precisión y exactitud, ya que son conceptos distintos aunque con frecuencia se confunden en el lenguaje cotidiano

<img width="621" height="51" alt="image" src="https://github.com/user-attachments/assets/8a5120d2-f325-485c-9bd1-5dd757704a3f" />

<img width="618" height="46" alt="image" src="https://github.com/user-attachments/assets/71ee7b7f-8d87-4265-8639-775372b471a2" />

<img width="633" height="154" alt="image" src="https://github.com/user-attachments/assets/1b3fdfad-f91d-469b-9c5b-0d67739e4a44" />

1.3 Tipos de Errores

En los métodos numéricos, los errores son inevitables. Sin embargo, podemos clasificarlos, cuantificarlos y controlarlos. Conocer los tipos de errores es fundamental para elegir el método más apropiado y para interpretar correctamente los resultados.

1.3.1 Error Verdadero o Absoluto

<img width="627" height="52" alt="image" src="https://github.com/user-attachments/assets/70fb04bf-cabb-4b23-9f84-54a1e2942db2" />

El error verdadero es la diferencia entre el valor exacto (teórico) y el valor calculado por el método numérico. En la práctica, raramente se conoce el valor verdadero, por lo que esta definición es más conceptual que operativa.

1.3.2 Error Relativo

<img width="617" height="68" alt="image" src="https://github.com/user-attachments/assets/4001eadd-2e26-4e4e-a249-49fb0e5d2cc4" />

El error relativo es más informativo que el error absoluto porque lo relaciona con la magnitud del valor verdadero. Un error de 1 metro es insignificante si se mide la distancia a la Luna, pero catastrófico si se mide la dimensión de un componente electrónico

1.3.3 Error Aproximado (Criterio de Parada)

En los métodos iterativos, no se conoce el valor verdadero, por lo que se utiliza el error aproximado: la diferencia entre dos iteraciones consecutivas. Este error se usa como criterio de parada del algoritmo

<img width="614" height="46" alt="image" src="https://github.com/user-attachments/assets/d9443a72-2935-4e5e-9aed-834d8c4c10b5" />

1.3.4 Error de Redondeo

El error de redondeo ocurre porque las computadoras solo pueden representar un número finito de dígitos. Los números reales con infinitos decimales (como pi, e, o 1/3) deben truncarse al número de bits disponibles en el procesador.

<img width="630" height="218" alt="image" src="https://github.com/user-attachments/assets/a03de9c4-1590-4c2b-8818-2d8ccdbc636a" />

1.3.5 Error de Truncamiento

El error de truncamiento se produce cuando se usa un procedimiento matemático finito para aproximar uno que, en su forma exacta, requeriría un número infinito de operaciones. El ejemplo más claro es la aproximación de una función mediante los primeros términos de su serie de Taylor

<img width="633" height="275" alt="image" src="https://github.com/user-attachments/assets/9e881225-3d6f-494a-9165-4201cfa3b8f7" />

1.4 Software de Cómputo Numérico

El avance de los métodos numéricos está íntimamente ligado al desarrollo de software especializado. Actualmente existen numerosas herramientas, desde lenguajes de programación de propósito general hasta paquetes matemáticos altamente especializados, que facilitan la implementación y visualización de estos métodos.

1.4.1 Lenguajes de Programación

<img width="627" height="235" alt="image" src="https://github.com/user-attachments/assets/a58cc39c-bd58-4696-b991-27567f16cd08" />

1.4.2 Librerías y Entornos Especializados

•	NumPy / SciPy (Python): Álgebra lineal, optimización, integración, ecuaciones diferenciales.
•	LAPACK / BLAS: Librerías de bajo nivel para álgebra lineal, base de muchos otros paquetes.
•	Mathematica / Wolfram Alpha: Cálculo simbólico y numérico integrado.
•	GNU Octave: Alternativa libre a MATLAB con alta compatibilidad.
•	R: Enfocado en estadística y análisis de datos.
•	OpenFOAM: Dinámica de fluidos computacional de código abierto.

1.4.3 Ejemplo práctico en Python

<img width="608" height="88" alt="image" src="https://github.com/user-attachments/assets/d93981b7-c895-4904-a707-8e747df6ae1f" />
<img width="608" height="128" alt="image" src="https://github.com/user-attachments/assets/ddd92e88-93c7-49eb-8705-f210d21344d2" />

1.5 Métodos Iterativos

Los métodos iterativos son algoritmos que generan una secuencia de aproximaciones sucesivas a la solución, mejorando la estimación en cada paso hasta alcanzar la precisión deseada. Son especialmenteP útiles cuando no existe una fórmula directa (de forma cerrada) para calcular la solución

1.5.1 Convergencia y Divergencia

Un método iterativo converge cuando la secuencia de aproximaciones se acerca al valor verdadero. Diverge cuando las aproximaciones se alejan indefinidamente. La convergencia depende tanto del método como del problema y la estimación inicial.

<img width="629" height="73" alt="image" src="https://github.com/user-attachments/assets/af35115c-fa85-4f13-856e-1fa3b0021f9d" />

1.5.2 Método de Bisección

El método de bisección es el método iterativo más simple y robusto. Requiere que la función cambie de signo en un intervalo [a, b], lo que garantiza la existencia de al menos una raíz por el Teorema de Valor Intermedio

<img width="629" height="263" alt="image" src="https://github.com/user-attachments/assets/f0c897c0-41f5-4db2-86b8-cbfba7fbb3bb" />

1.5.3 Método de Newton-Raphson

El método de Newton-Raphson es uno de los algoritmos iterativos más poderosos para encontrar raíces. Utiliza la derivada de la función para construir la tangente a la curva en el punto actual y usa su intersección con el eje x como la siguiente aproximación

<img width="628" height="55" alt="image" src="https://github.com/user-attachments/assets/fb483c5b-e56c-48d1-b7eb-11c24338965e" />

Este método tiene convergencia cuadrática cerca de la raíz, lo que significa que el número de dígitos correctos se duplica en cada iteración. Sin embargo, puede diverger si la estimación inicial es muy lejana a la raíz o si f'(x) = 0 en algún punto de la iteración.

1.5.4 Método de la Secante

El método de la secante es una modificación del método de Newton-Raphson que evita el cálculo de la derivada, aproximándola mediante la pendiente de una secante entre dos puntos consecutivos

<img width="629" height="72" alt="image" src="https://github.com/user-attachments/assets/cd15f82d-27a0-43c9-8f02-d7d80ce527e0" />

Requiere dos estimaciones iniciales en lugar de una, y tiene una convergencia superlineal (orden ≈ 1.618, el número áureo), lo que lo hace más lento que Newton-Raphson pero más robusto en casos donde la derivada es difícil de calcular.

1.5.5 Comparación de Métodos Iterativos

<img width="625" height="235" alt="image" src="https://github.com/user-attachments/assets/b261a15d-1e0a-45fa-9e08-db7bd24e1e26" />

1.5.6 Criterios de Parada

Todos los métodos iterativos necesitan un criterio que indique cuándo detener el proceso. Los criterios más comunes son:

1.	Error relativo aproximado: |epsilon_a| < epsilon_s (criterio de Scarborough)
2.	Número máximo de iteraciones: previene bucles infinitos en caso de divergencia.
3.	Valor de la función: |f(x_n)| < delta, el valor de la función está suficientemente cerca de cero.
4.	Cambio absoluto: |x_{n+1} - x_n| < tolerancia_absoluta
