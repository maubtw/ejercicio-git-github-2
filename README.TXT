Proyecto Calculadora – Operación Potencia

Este proyecto implementa una calculadora en Python con estructura modular, en donde la operación de potencia ya está desarrollada.

Estructura del proyecto

main.py → Archivo principal que ejecuta el programa.

clases/operaciones.py → Contiene la clase Operaciones y los métodos de la calculadora.

README.txt → Este archivo con las indicaciones para colaboradores.

Instrucciones para colaboradores

Actualmente, el proyecto incluye la operación de potencia.
Tu tarea como colaborador es desarrollar la operación de raíz cuadrada siguiendo estas indicaciones:

Editar el archivo: clases/operaciones.py.

Dentro de la clase Operaciones, agrega un método llamado raiz().

Este método debe calcular la raíz cuadrada de self.base.

Puedes usar la función math.sqrt().

Si el número es negativo, mostrar un mensaje indicando que no es posible calcular la raíz.

Agregar un método mostrarRaiz() (opcional) para imprimir el resultado de manera clara.

Modificar main.py si es necesario, para probar la nueva operación.

Respetar el mismo estilo de código usado en potencia().