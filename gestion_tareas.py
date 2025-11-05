import json
import os
from modelos.tareas import Tarea
from servicios.gestion_usuarios import cargar_usuarios

RUTA_ARCHIVO = "datos/tareas.json"

def cargar_tareas():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return [Tarea.from_dict(t) for t in datos]

def guardar_tareas(tareas):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tareas], f, indent=4)

def crear_tarea():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
        return
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción: ")
    print("\nUsuarios disponibles:")
    for u in usuarios:
        print(f"- {u.nombre} ({u.rol})")
    asignado_a = input("Asignar a: ")
    if not any(u.nombre == asignado_a for u in usuarios):
        print("⚠️ Usuario no encontrado.")
        return
    tareas = cargar_tareas()
    tareas.append(Tarea(titulo, descripcion, asignado_a))
    guardar_tareas(tareas)
    print("✅ Tarea creada y asignada con éxito.")

def consultar_tareas_por_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    tareas = cargar_tareas()
    tareas_usuario = [t for t in tareas if t.asignado_a == nombre]
    if not tareas_usuario:
        print("⚠️ No hay tareas asignadas a este usuario.")
        return
    print(f"\nTareas asignadas a {nombre}:")
    for t in tareas_usuario:
        estado = "✅ Completada" if t.completada else "⏳ Pendiente"
        print(f"- {t.titulo}: {t.descripcion} ({estado})")
