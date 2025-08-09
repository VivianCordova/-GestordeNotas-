# -GestordeNotas-
Gestor de notas academias
Gestor de Notas Académicas: Objetivo y Audiencia
El objetivo de un Gestor de Notas Académicas es ser una herramienta eficiente para que estudiantes y educadores puedan registrar, organizar y visualizar calificaciones de manera sistemática. El sistema permitirá un seguimiento preciso del rendimiento académico a lo largo del tiempo. Esto ayuda a identificar áreas de mejora, monitorear el progreso y facilitar la preparación de informes o resúmenes de calificaciones de manera rápida y sin errores. En esencia, su propósito es simplificar la gestión de datos académicos, haciendo que el proceso sea menos propenso a equivocaciones manuales y más accesible para el usuario. Este tipo de gestor está dirigido principalmente a estudiantes de cualquier nivel educativo (desde secundaria hasta universidad) que necesiten llevar un control detallado de sus calificaciones. 

Requisitos Funcionales
Registrar un nuevo curso y nota: El usuario podrá ingresar el nombre de un curso, El sistema almacenará esta información de forma estructurada.
Mostrar todas las notas: El sistema presentará un listado completo de todos los cursos y las notas registradas hasta el momento.
Ordenar cursos por nota: El usuario podrá solicitar que el listado de cursos se ordene de forma ascendente o descendente, según la calificación.
Mostrar historial de cambios: Se llevará un registro de cualquier modificación (actualización de notas, eliminación de cursos), permitiendo al usuario revisar el historial de cambios realizados.

Requisitos No Funcionales y Estructura de Programación
El sistema se ejecutará en una consola de Python, La interfaz será simple, basada en texto, y estará diseñada para la comodidad del usuario final.

La lógica del programa estará estructurada mediante el uso de bucles y condicionales. Por ejemplo, un ciclo para (for) podría usarse para iterar sobre la lista de notas y mostrarlas en pantalla, mientras que un ciclo mientras (while) mantendrá el menú principal activo, permitiendo al usuario realizar múltiples acciones hasta que decida salir. Los condicionales (if/elif/else) se utilizarán para gestionar las opciones del menú, dirigiendo al programa a la función correspondiente según la elección del usuario (por ejemplo, si el usuario presiona "1", el programa ejecutará la función para registrar una nueva nota). Esta estructura garantiza que el programa sea robusto, fácil de navegar y que responda de manera predecible a las interacciones del usuario.
