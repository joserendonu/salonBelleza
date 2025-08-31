class Servicio:
    def __init__(self, codigo, descripcion, precio, duracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio
        self.duracion = duracion

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} (${self.precio}, {self.duracion}min)"
