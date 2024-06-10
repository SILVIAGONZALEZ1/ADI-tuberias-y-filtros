# ADI-tuberias-y-filtros
#	Programe 1 patrón tuberías y filtros.

El código implementa un patrón de diseño conocido como Cadena de Responsabilidad (Chain of Responsibility), aplicado en forma de una tubería de procesamiento (Pipeline) de datos. Este patrón permite que un objeto pase por una cadena de manejadores hasta que se procese completamente. Cada manejador en la cadena decide si procesa los datos y pasa los datos procesados al siguiente manejador.

Proceso paso a paso:
1-Convierte el texto a minúsculas:
"Hello, World! This is a test string with numbers 123 and symbols %$#." se convierte en "hello, world! this is a test string with numbers 123 and symbols %$#."

2-Elimina los caracteres no alfabéticos:
"hello, world! this is a test string with numbers 123 and symbols %$#." se convierte en "hello world this is a test string with numbers and symbols "

3-Divide la cadena en palabras:
"hello world this is a test string with numbers and symbols " se convierte en ["hello", "world", "this", "is", "a", "test", "string", "with", "numbers", "and", "symbols"]

4-Cuenta las palabras:
La lista ["hello", "world", "this", "is", "a", "test", "string", "with", "numbers", "and", "symbols"] tiene 11 palabras.

5-El resultado final impreso será:
El número de palabras en el texto procesado es: 11
