def registrar_curso(cursos): #Fucion para registrar los cursos
    """Solicita el nombre y la nota del curso y los agrega al diccionario."""
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

def mostrar_cursos(cursos): #funcion/procedimiento para mostrar los cursos
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

def main():
    """Función principal que maneja el menú del gestor de notas."""
    cursos = {}

    while True:
        print("\n--- GESTOR DE NOTAS ACADÉMICAS ---")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Salir")
        
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
            print("¡Gracias por usar el gestor de notas! ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una de las opciones del 1 al 5.")

if __name__ == "__main__":
    main()