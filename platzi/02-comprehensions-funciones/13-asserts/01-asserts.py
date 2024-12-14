# En Python, la declaración assert se utiliza como una herramienta de depuración para verificar que ciertas condiciones sean verdaderas en tiempo de ejecución. Si la condición evaluada en la declaración assert resulta falsa, el programa genera una excepción AssertionError, lo que permite identificar problemas de manera temprana.

# sintaxis
# assert condition, message

# condition: Es una expresión booleana que se espera que sea True.
# message (opcional): Un mensaje de error que se muestra si la condición es False.


# ¿Cuándo usar assert?
# Para verificar condiciones que deberían ser siempre verdaderas durante la ejecución normal del programa.
# Ideal para detectar errores de lógica en etapas de desarrollo y pruebas.
# No se debe usar para manejar errores esperados en producción, ya que assert puede deshabilitarse cuando el intérprete de Python se ejecuta con la opción -O (optimización).


# Mejores Prácticas

# Evita usar assert para lógica crítica de la aplicación: Por ejemplo, no lo utilices para verificar la entrada del usuario en un entorno de producción.
# Proporciona mensajes descriptivos: Esto facilita identificar el problema al depurar.
# No dependas de assert para validaciones que deban ejecutarse siempre: Usa validaciones explícitas y manejo de excepciones para casos críticos.
# Úsalo principalmente en etapas de desarrollo y pruebas: Es una herramienta útil para garantizar que tu código cumple con los supuestos iniciales.