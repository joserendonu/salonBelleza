class Usuario:
    def __init__(self, tipo, cedula, nombre, apellido, telefono, fechaNacimiento, isEmployee=False, isAdmin=False):
        self.tipo = tipo  # "Administrador", "Empleado", "Cliente"
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.servicio = None
        self.isEmployee = isEmployee
        self.isAdmin = isAdmin

    def __str__(self):
        return f"{self.tipo}: {self.nombre} {self.apellido} ({self.cedula})"
