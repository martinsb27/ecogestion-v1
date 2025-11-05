import json

class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol  # 'admin' o 'empleado'

    def to_dict(self):
        return {"nombre": self.nombre, "rol": self.rol}

    @staticmethod
    def from_dict(data):
        return Usuario(data["nombre"], data["rol"])
