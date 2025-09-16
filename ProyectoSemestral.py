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
        for nota in cursos.values():
            if nota >= 60:
                aprobados += 1
            else:
                reprobados += 1
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}")

# --- Nuevas funciones agregadas ---

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
    
    # Actualiza la nota de un curso existente.

    if not cursos:
        print("No hay cursos para actualizar.")
        return
        
    nombre_curso = input("Ingresa el nombre del curso para actualizar la nota: ").strip()
    
    if nombre_curso in cursos:
        while True:
            try:
                nueva_nota = float(input(f"Ingresa la nueva nota para '{nombre_curso}' (0-100): "))
                if 0 <= nueva_nota <= 100:
                    cursos[nombre_curso] = nueva_nota
                    print("Nota actualizada correctamente.")
                    break
                else:
                    print("La nota debe ser un número entre 0 y 100. Intenta de nuevo.")
            except ValueError:
                print("Nota inválida. Por favor, ingresa un número.")
    else:
        print(f"El curso '{nombre_curso}' no se encuentra registrado.")

def eliminar_curso(cursos):
   
    #Elimina un curso del diccionario.
    Pide confirmación antes de eliminar.

    if not cursos:
        print("No hay cursos para eliminar.")
        return

    nombre_curso = input("Ingresa el curso a eliminar: ").strip()
    
    if nombre_curso in cursos:
        confirmacion = input(f"¿Estás seguro que desea eliminar el curso '{nombre_curso}'? (s/n): ").lower()
        if confirmacion == 's':
            del cursos[nombre_curso]
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

    # Implementación del ordenamiento burbuja
    for i in range(n):
        for j in range(0, n - i - 1):
            if cursos_lista[j][1] < cursos_lista[j + 1][1]:
                cursos_lista[j], cursos_lista[j + 1] = cursos_lista[j + 1], cursos_lista[j]

    print("\n--- Cursos ordenados por nota ---")
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

    # Implementación del ordenamiento por inserción
    for i in range(1, n):
        curso_actual = cursos_lista[i]
        j = i - 1
        while j >= 0 and curso_actual[0].lower() < cursos_lista[j][0].lower():
            cursos_lista[j + 1] = cursos_lista[j]
            j -= 1
        cursos_lista[j + 1] = curso_actual

    print("\n--- Cursos ordenados por nombre ---")
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

def main():
    """Función principal que maneja el menú del gestor de notas."""
    cursos = {}

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
        print("11. Salir")
        
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
            actualizar_nota(cursos)
        elif opcion == '7':
            eliminar_curso(cursos)
        elif opcion == '8':
            ordenar_por_nota(cursos)
        elif opcion == '9':
            ordenar_por_nombre(cursos)
        elif opcion == '10':
            buscar_curso_binaria(cursos)
        elif opcion == '11':
            print("¡Gracias por usar el gestor de notas! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una de las opciones del 1 al 11.")

if __name__ == "__main__":
    main()
