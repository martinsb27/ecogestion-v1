from servicios.gestion_usuarios import registrar_usuario, listar_usuarios
from servicios.gestion_tareas import crear_tarea, consultar_tareas_por_usuario

def mostrar_menu():
    print("\n=== ECOGESTIÓN - SISTEMA DE GESTIÓN INTERNA ===")
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Crear tarea")
    print("4. Consultar tareas por usuario")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            crear_tarea()
        elif opcion == "4":
            consultar_tareas_por_usuario()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
