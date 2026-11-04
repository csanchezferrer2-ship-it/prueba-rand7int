# Prueba Técnica: rand7() a partir de rand5()

## Descripción del problema
El objetivo de este repositorio es implementar una función que genere números enteros aleatorios entre 1 y 7 con una distribución uniforme, utilizando únicamente una función base proporcionada que genera números aleatorios entre 1 y 5 (`rand5()`).

## Solución propuesta
Para garantizar que todos los números del 1 al 7 tengan exactamente la misma probabilidad de aparecer (14.28%), he implementado un algoritmo basado en la técnica de **muestreo de rechazo** (rejection sampling). 

Cualquier intento de sumar los resultados o hacer operaciones aritméticas simples sobre llamadas múltiples generaría un sesgo estadístico (distribución normal/campana de Gauss). Para evitarlo, la solución sigue estos pasos:

1. **Expansión del espacio muestral:** 
   Utilizando la fórmula `(rand5() - 1) * 5 + rand5()`, generamos una distribución perfectamente uniforme de enteros entre el 1 y el 25.

2. **Muestreo de rechazo:** 
   Como necesitamos 7 resultados posibles de manera uniforme, buscamos el múltiplo de 7 más cercano que sea menor o igual a 25, que es el **21**. Los valores que caen entre 22 y 25 se descartan (se rechazan) y se vuelve a iterar.

3. **Mapeo uniforme:** 
   Para los números del 1 al 21, aplicamos la operación módulo (`% 7`). Esto divide los 21 resultados en 7 conjuntos exactos de 3 elementos cada uno, devolviendo restos del 0 al 6. Al sumarle 1 al final, desplazamos el resultado para devolver un número equitativo entre 1 y 7.

## Escalabilidad del algoritmo
El enfoque utilizado es altamente versátil y permite adaptar la función a otras distribuciones modificando solo los límites:

* **Ej. Para un rand8():** Usando el mismo espacio de 25, cambiaríamos el límite de aceptación a 24 (el múltiplo de 8 más cercano) y aplicaríamos `(num % 8) + 1`.
* **Para rangos mayores de 25:** Se puede escalar el espacio muestral añadiendo más dimensiones con potencias de 5.