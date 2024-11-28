def menu():
    """
    Muestra el menú principal del sistema de gestión de notas.
    Ofrece las opciones para ingresar notas, mostrar notas, modificar notas,
    calcular el promedio de notas o salir del sistema.
    """
    print("\n=== Sistema de Gestión de Notas ===")
    print("1. Ingresar notas de estudiantes")
    print("2. Mostrar todas las notas")
    print("3. Modificar la nota de un estudiante")
    print("4. Mostrar promedio de notas")
    print("5. Salir")

def ingresar_notas(estudiantes):
    """
    Permite ingresar las notas de los estudiantes en el sistema.

    Args:
        estudiantes (list): Lista que almacena los datos de los estudiantes (nombre y nota).

    Dentro de esta función, se verifica si un estudiante ya tiene una nota registrada,
    y se valida que la nota esté en un rango adecuado (0-100). Los errores en la entrada se gestionan con un bloque try-except.
    """
    while True:
        try:
            nombre = input("Ingresa el nombre del estudiante (o escribe 'salir' para regresar al menú): ").strip()
            if nombre.lower() == 'salir':
                break
            # Verificar si el estudiante ya tiene una nota registrada
            if any(estudiante["nombre"].lower() == nombre.lower() for estudiante in estudiantes):
                print("Este estudiante ya tiene una nota registrada. Usa la opción para modificar notas si deseas actualizarla.")
                continue
            nota = float(input(f"Ingresa la nota para {nombre}: "))
            if 0 <= nota <= 100:
                estudiantes.append({"nombre": nombre, "nota": nota})
                print(f"Nota de {nombre} registrada correctamente.")
            else:
                print("La nota debe estar entre 0 y 100. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número para la nota.")

def mostrar_notas(estudiantes):
    """
    Muestra las notas de todos los estudiantes registrados en el sistema.

    Args:
        estudiantes (list): Lista de estudiantes con sus respectivas notas.

    Si no hay estudiantes registrados, se muestra un mensaje adecuado.
    """
    if estudiantes:
        print("\n=== Notas de Estudiantes ===")
        for estudiante in estudiantes:
            print(f"Estudiante: {estudiante['nombre']}, Nota: {estudiante['nota']:.2f}")
    else:
        print("No hay notas registradas.")

def modificar_nota(estudiantes):
    """
    Permite modificar la nota de un estudiante existente.

    Args:
        estudiantes (list): Lista de estudiantes con sus respectivas notas.

    Si no hay estudiantes registrados, se muestra un mensaje adecuado.
    Se verifica si el estudiante existe y luego permite modificar su nota.
    """
    if not estudiantes:
        print("No hay estudiantes registrados. Agrega notas primero.")
        return

    nombre = input("Ingresa el nombre del estudiante cuya nota deseas modificar: ").strip()
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            try:
                nueva_nota = float(input(f"Ingresa la nueva nota para {estudiante['nombre']}: "))
                if 0 <= nueva_nota <= 100:
                    estudiante["nota"] = nueva_nota
                    print(f"Nota de {estudiante['nombre']} actualizada correctamente.")
                    return
                else:
                    print("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
            return

    print(f"No se encontró un estudiante con el nombre '{nombre}'.")

def mostrar_promedio(estudiantes):
    """
    Calcula y muestra el promedio de las notas de todos los estudiantes.

    Args:
        estudiantes (list): Lista de estudiantes con sus respectivas notas.

    Si no hay estudiantes registrados, se maneja una excepción y muestra un mensaje adecuado.
    """
    try:
        if not estudiantes:
            raise ZeroDivisionError("No hay estudiantes registrados.")

        suma_notas = sum(estudiante["nota"] for estudiante in estudiantes)
        promedio = suma_notas / len(estudiantes)
        print("\n=== Notas de Estudiantes ===")
        for estudiante in estudiantes:
            print(f"Estudiante: {estudiante['nombre']}, Nota: {estudiante['nota']:.2f}")
        print(f"\nPromedio de las notas: {promedio:.2f}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

def main():
    """
    Función principal que gestiona la ejecución del sistema de notas.

    Muestra el menú, permite al usuario seleccionar opciones, y ejecuta las acciones correspondientes
    basadas en la elección del usuario. El sistema se ejecuta en un bucle hasta que el usuario decide salir.
    """
    estudiantes = []
    while True:
        menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 1:
                ingresar_notas(estudiantes)
            elif opcion == 2:
                mostrar_notas(estudiantes)
            elif opcion == 3:
                modificar_nota(estudiantes)
            elif opcion == 4:
                mostrar_promedio(estudiantes)
            elif opcion == 5:
                print("Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, selecciona un número.")

main()
