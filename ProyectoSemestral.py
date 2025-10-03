# Inicializamos una lista global para la pila de historial de cambios
# Usamos una lista para simular una pila (LIFO - Last In, First Out)
# La pila se inicializa fuera de main() para que sea accesible por las funciones que la modifican.
historial_cambios = []

def registrar_curso(cursos):
    #Solicita el nombre y la nota del curso y los agrega al diccionario
    while True:
        nombre = input("Ingresa el nombre del curso: ").strip()
        if nombre:
            break
        else:
            print("El nombre del curso no puede estar vacío. Intenta de nuevo.")

    while True:
        try:
            nota = float(input(f"Ingresa la nota de '{nombre}' (0-100): "))
            if 0 <= nota <= 100:
                cursos[nombre] = nota
                print(f"Curso '{nombre}' registrado con la nota {nota}.")
                break
            else:
                print("La nota debe ser un número entre 0 y 100. Intenta de nuevo.")
        except ValueError:
            print("Nota inválida. Por favor, ingresa un número.")

def mostrar_cursos(cursos):
    """Muestra todos los cursos y sus notas."""
    if not cursos:
        print("No hay cursos registrados.")
    else:
        print("\n--- Cursos y Notas ---")
        for curso, nota in cursos.items():
            print(f"- {curso}: {nota}")
        print("--------------------------------\n")

def calcular_promedio(cursos):
    """Calcula y muestra el promedio de todas las notas."""
    if not cursos:
        print("No hay cursos para calcular el promedio.")
    else:
        total_notas = sum(cursos.values())
        promedio = total_notas / len(cursos)
        print(f"El promedio general es: {promedio:.2f}")

def contar_aprobados_reprobados(cursos):
    """Cuenta y muestra la cantidad de cursos aprobados y reprobados."""
    if not cursos:
        print("No hay cursos para contar.")
    else:
        aprobados = 0
        reprobados = 0
        # En el escencario de mi gestor de notas, 60 es la nota mínima de aprobación
        for nota in cursos.values():
            if nota >= 60:
                aprobados += 1
            else:
                reprobados += 1
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}")

def buscar_curso_lineal(cursos):
    """
    5. Busca un curso por nombre usando búsqueda lineal.
    Permite coincidencia parcial e ignora mayúsculas/minúsculas.
    """
    if not cursos:
        print("No hay cursos para buscar.")
        return

    nombre_buscar = input("Ingresa el nombre del curso a buscar: ").strip().lower()
    encontrado = False
    
    for curso, nota in cursos.items():
        if nombre_buscar in curso.lower():
            print(f"\nCurso encontrado: {curso} - Nota: {nota}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"No se encontró ningún curso que contenga '{nombre_buscar}'.")

def actualizar_nota(cursos):
    
    # Actualiza la nota de un curso existente y guarda el cambio en la pila.

    if not cursos:
        print("No hay cursos para actualizar.")
        return
        
    nombre_curso = input("Ingresa el nombre del curso para actualizar la nota: ").strip()
    
    if nombre_curso in cursos:
        nota_anterior = cursos[nombre_curso] # Guardamos la nota anterior
        while True:
            try:
                nueva_nota = float(input(f"Ingresa la nueva nota para '{nombre_curso}' (0-100): "))
                if 0 <= nueva_nota <= 100:
                    if nueva_nota != nota_anterior: # Solo registramos si la nota cambia
                        # Guardar en la pila (simulación de PUSH)
                        historial_cambios.append(f"Se actualizó: {nombre_curso} - Nota anterior: {nota_anterior} -> Nueva nota: {nueva_nota}")
                        cursos[nombre_curso] = nueva_nota
                        print("Nota actualizada correctamente.")
                    else:
                        print("La nota es la misma, no se realizó ninguna actualización.")
                    break
                else:
                    print("La nota debe ser un número entre 0 y 100. Intenta de nuevo.")
            except ValueError:
                print("Nota inválida. Por favor, ingresa un número.")
    else:
        print(f"El curso '{nombre_curso}' no se encuentra registrado.")

def eliminar_curso(cursos):
    
    #Elimina un curso del diccionario y guarda el cambio en la pila.
    #Pide confirmación antes de eliminar.

    if not cursos:
        print("No hay cursos para eliminar.")
        return

    nombre_curso = input("Ingresa el curso a eliminar: ").strip()
    
    if nombre_curso in cursos:
        confirmacion = input(f"¿Estás seguro que desea eliminar el curso '{nombre_curso}'? (s/n): ").lower()
        if confirmacion == 's':
            nota_eliminada = cursos.pop(nombre_curso) # Elimina y obtiene la nota
            # Guardar en la pila (simulación de PUSH)
            historial_cambios.append(f"Se eliminó: {nombre_curso} - Nota: {nota_eliminada}")
            print("Curso eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print(f"El curso '{nombre_curso}' no se encuentra en la lista.")

def ordenar_por_nota(cursos):
    """
    8. Ordena los cursos por nota en orden descendente usando ordenamiento burbuja.
    """
    if not cursos:
        print("No hay cursos para ordenar.")
        return

    # Convertir el diccionario a una lista de tuplas (nombre, nota) para ordenar
    cursos_lista = list(cursos.items())
    n = len(cursos_lista)

    # Implementación del ordenamiento burbuja (Bubble Sort)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparamos las notas (índice 1 de la tupla)
            if cursos_lista[j][1] < cursos_lista[j + 1][1]:
                # Intercambio
                cursos_lista[j], cursos_lista[j + 1] = cursos_lista[j + 1], cursos_lista[j]

    print("\n--- Cursos ordenados por nota (Descendente) ---")
    for i, (curso, nota) in enumerate(cursos_lista):
        print(f"{i + 1}. {curso} - Nota: {nota}")

def ordenar_por_nombre(cursos):
    
    #. Ordena los cursos por nombre alfabéticamente usando ordenamiento por inserción.
    
    if not cursos:
        print("No hay cursos para ordenar.")
        return

    # Convertir el diccionario a una lista de tuplas (nombre, nota) para ordenar
    cursos_lista = list(cursos.items())
    n = len(cursos_lista)

    # Implementación del ordenamiento por inserción (Insertion Sort)
    for i in range(1, n):
        curso_actual = cursos_lista[i]
        j = i - 1
        # Comparamos los nombres (índice 0 de la tupla), ignorando mayúsculas/minúsculas
        while j >= 0 and curso_actual[0].lower() < cursos_lista[j][0].lower():
            cursos_lista[j + 1] = cursos_lista[j]
            j -= 1
        cursos_lista[j + 1] = curso_actual

    print("\n--- Cursos ordenados por nombre (Alfabético) ---")
    for i, (curso, nota) in enumerate(cursos_lista):
        print(f"{i + 1}. {curso} - Nota: {nota}")
        
    return cursos_lista # Se retorna la lista ordenada para la búsqueda binaria

def buscar_curso_binaria(cursos):
    """
    10. Busca un curso por nombre usando búsqueda binaria.
    Requiere que la lista esté ordenada por nombre.
    """
    if not cursos:
        print("No hay cursos para buscar.")
        return

    # Se ordena la lista antes de la búsqueda binaria
    cursos_lista_ordenada = sorted(list(cursos.items()), key=lambda x: x[0].lower())

    nombre_buscar = input("Ingresa el nombre del curso a buscar: ").strip().lower()
    inicio = 0
    fin = len(cursos_lista_ordenada) - 1
    encontrado = False

    while inicio <= fin:
        medio = (inicio + fin) // 2
        nombre_curso_medio = cursos_lista_ordenada[medio][0].lower()

        if nombre_curso_medio == nombre_buscar:
            print(f"\nCurso encontrado: {cursos_lista_ordenada[medio][0]} - Nota: {cursos_lista_ordenada[medio][1]}")
            encontrado = True
            break
        elif nombre_buscar > nombre_curso_medio:
            inicio = medio + 1
        else:
            fin = medio - 1

    if not encontrado:
        print("Curso no encontrado. Asegúrate de ingresar el nombre completo y correctamente escrito.")

# ----------------------------------------------------
## 11. Simular cola de solicitudes de revisión (FIFO)
# ----------------------------------------------------

def simular_cola_revision():
    """
    Simula una cola (FIFO) de solicitudes de revisión de cursos.
    """
    # Usamos una lista para simular la cola (FIFO - First In, First Out)
    cola_solicitudes = [] 
    print("\n--- Simular cola de solicitudes de revisión ---")
    
    while True:
        curso_solicitado = input("Ingrese curso para revisión (escriba 'fin' para terminar): ").strip()
        
        if curso_solicitado.lower() == 'fin':
            break
        
        if curso_solicitado:
            # Se agrega al final (simulación de ENQUEUE/PUT)
            cola_solicitudes.append(curso_solicitado)
        else:
            print("El nombre del curso no puede estar vacío.")

    if not cola_solicitudes:
        print("No se ingresaron solicitudes de revisión.")
        return

    print("\nProcesando solicitudes:")
    # Recorrer la cola en orden de ingreso
    while cola_solicitudes:
        # Se extrae del inicio (simulación de DEQUEUE/GET)
        curso_a_revisar = cola_solicitudes.pop(0) 
        print(f"Revisando: {curso_a_revisar}")
        
    print("Simulación de revisión finalizada.")

# ----------------------------------------------------
## 12. Mostrar historial de cambios (PILA - LIFO)
# ----------------------------------------------------

def mostrar_historial_cambios():
    """
    Muestra el historial de cambios (modificaciones o eliminaciones) de notas 
    en orden inverso al que se aplicaron, simulando una pila (LIFO).
    """
    global historial_cambios
    
    if not historial_cambios:
        print("\nNo hay historial de cambios recientes.")
        return

    print("\n--- Historial de cambios recientes (PILA) ---")
    
    # Recorrer la pila de forma inversa (del último al primero)
    # Usamos una copia invertida para mostrar sin modificar la pila original
    for i, cambio in enumerate(reversed(historial_cambios)):
        print(f"{i + 1}. {cambio}")
        
    print("---------------------------------------------")


def main():
    """Función principal que maneja el menú del gestor de notas."""
    # El diccionario 'cursos' se mantiene local a main
    cursos = {} 
    # La pila 'historial_cambios' es global, definida al inicio del script.

    while True:
        print("\n--- GESTOR DE NOTAS ACADÉMICAS ---")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre (Búsqueda Lineal)")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Ordenar cursos por nota (Burbuja)")
        print("9. Ordenar cursos por nombre (Inserción)")
        print("10. Buscar curso por nombre (Búsqueda Binaria)")
        # Nuevas funcionalidades
        print("11. Simular cola de solicitudes de revisión")
        print("12. Mostrar historial de cambios (PILA)")
        # Cambiamos la opción de salida
        print("13. Salir") 
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            registrar_curso(cursos)
        elif opcion == '2':
            mostrar_cursos(cursos)
        elif opcion == '3':
            calcular_promedio(cursos)
        elif opcion == '4':
            contar_aprobados_reprobados(cursos)
        elif opcion == '5':
            buscar_curso_lineal(cursos)
        elif opcion == '6':
            # Se ha modificado para registrar en la pila
            actualizar_nota(cursos) 
        elif opcion == '7':
            # Se ha modificado para registrar en la pila
            eliminar_curso(cursos) 
        elif opcion == '8':
            ordenar_por_nota(cursos)
        elif opcion == '9':
            ordenar_por_nombre(cursos)
        elif opcion == '10':
            buscar_curso_binaria(cursos)
        # Manejo de las nuevas opciones
        elif opcion == '11': 
            simular_cola_revision()
        elif opcion == '12': 
            mostrar_historial_cambios()
        elif opcion == '13':
            print("¡Gracias por usar el gestor de notas! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una de las opciones del 1 al 13.")

if __name__ == "__main__":
    main()
