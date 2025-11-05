class Tarea:
    def __init__(self, titulo, descripcion, asignado_a):
        self.titulo = titulo
        self.descripcion = descripcion
        self.asignado_a = asignado_a  # nombre del usuario
        self.completada = False

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "asignado_a": self.asignado_a,
            "completada": self.completada
        }

    @staticmethod
    def from_dict(data):
        tarea = Tarea(data["titulo"], data["descripcion"], data["asignado_a"])
        tarea.completada = data["completada"]
        return tarea
