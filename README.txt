Implementación de Calculadora Matricial en Python con NumPy

ALUMNO: William Quispe

1. Metodología de Implementación (¿Cómo se realizó?)
Para cumplir con el requerimiento de una calculadora "sofisticada", se abandonó el enfoque tradicional de bucles anidados (común en Visual Basic) y se optó por la vectorización.
•	Librería NumPy: Se utilizó el objeto np.array, que permite tratar las matrices como bloques de datos únicos en lugar de listas de listas. Esto optimiza el código, reduciendo la operación de multiplicación de 15 líneas de código a una sola función: np.dot(A, B).
•	Modularidad: El código se dividió en funciones específicas (solicitar_dimensiones, crear_matriz, main). Esto permite aislar errores; si falla la entrada de datos, no afecta la lógica de cálculo.
•	Manejo de Excepciones (Robustez): Se implementaron bloques try-except. Esto blinda al programa contra errores de usuario ("User Error"), como ingresar texto cuando se piden números, evitando que el software se cierre inesperadamente.
2. Dificultades Encontradas y Soluciones
Durante el desarrollo en el entorno Google Colab, se enfrentaron los siguientes desafíos:
1.	La Indentación (Sangría) en Python:
o	Dificultad: A diferencia de Visual Basic que usa End Sub, Python define la estructura mediante espacios. Tuve errores de tipo IndentationError o expected an indented block al definir funciones y bucles.
o	Solución: Se estandarizó el uso de la tecla TAB para mantener la jerarquía del código, asegurando que las instrucciones print o return estuvieran correctamente alineadas dentro de sus funciones def.


2.	Validación Dimensional en Multiplicación:
o	Dificultad: Al principio, el programa intentaba multiplicar cualquier matriz, generando errores de sistema cuando las dimensiones no eran compatibles.
o	Solución: Se agregó una validación lógica con 
if A.shape[1] != B.shape[0].
o	Esto permite al programa "pensar" antes de calcular, verificando si el número de columnas de la Matriz A coincide con las filas de la Matriz B, tal como dicta la teoría de álgebra lineal.
3.	Transición de Paradigma:
o	Dificultad: Adaptar la lógica de programación secuencial aprendida en semestres anteriores a la lógica de funciones y librerías de Python.
o	Solución: El uso de comentarios y documentación interna (Docstrings) ayudó a mantener el orden y entender el flujo de datos entre las funciones.

