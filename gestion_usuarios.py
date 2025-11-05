import json
import os
from modelos.usuarios import Usuario

RUTA_ARCHIVO = "datos/usuarios.json"

def cargar_usuarios():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return [Usuario.from_dict(u) for u in datos]

def guardar_usuarios(usuarios):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump([u.to_dict() for u in usuarios], f, indent=4)

def registrar_usuario():
    nombre = input("Ingrese nombre del usuario: ")
    rol = input("Ingrese rol (admin/empleado): ").lower()
    if rol not in ["admin", "empleado"]:
        print("⚠️ Rol inválido.")
        return
    usuarios = cargar_usuarios()
    if any(u.nombre == nombre for u in usuarios):
        print("⚠️ El usuario ya existe.")
        return
    usuarios.append(Usuario(nombre, rol))
    guardar_usuarios(usuarios)
    print("✅ Usuario registrado con éxito.")

def listar_usuarios():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("\nUsuarios registrados:")
    for u in usuarios:
        print(f"- {u.nombre} ({u.rol})")
