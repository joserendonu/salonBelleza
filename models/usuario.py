# Autores Samuel Diaz, Jonathan Urriago, Sara Peña

class Usuario:
    def __init__(self, cedula, nombre, apellido, telefono, fechaNacimiento, isAdmin=False, isEmployee=False):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.isAdmin = isAdmin
        self.isEmployee = isEmployee

    def tipo(self):
        return "Usuario"
    # ...resto del código...

class Administrador(Usuario):
    def __init__(self, cedula, nombre, apellido, telefono, fechaNacimiento):
        super().__init__(cedula, nombre, apellido, telefono, fechaNacimiento, isAdmin=True, isEmployee=False)
    def tipo(self):
        return "Administrador"
    # ...resto del código...

class Empleado(Usuario):
    def __init__(self, cedula, nombre, apellido, telefono, fechaNacimiento):
        super().__init__(cedula, nombre, apellido, telefono, fechaNacimiento, isAdmin=False, isEmployee=True)
    def tipo(self):
        return "Empleado"
    # ...resto del código...

class Cliente(Usuario):
    def __init__(self, cedula, nombre, apellido, telefono, fechaNacimiento, isEmployee=False):
        super().__init__(cedula, nombre, apellido, telefono, fechaNacimiento, isAdmin=False, isEmployee=isEmployee)
    def tipo(self):
        return "Cliente"

    def puede_cancelar(self, cita):
        # Solo si es el cliente y la cita está pendiente
        return cita.estado == "pendiente" and cita.infoCliente.cedula == self.cedula