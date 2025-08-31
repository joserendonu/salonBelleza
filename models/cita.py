# Autores Samuel Diaz, Jonathan Urriago, Sara Peña

class Cita:
    def __init__(self, infoCliente, servicioContratado, ccEncargado, fechaCita):
        self.__infoCliente = infoCliente
        self.__servicioContratado = servicioContratado
        self.__ccEncargado = ccEncargado
        self.__fechaCita = fechaCita
        self.__estado = "pendiente"
        self.__precioCita = servicioContratado.precio
        self.__descuento = 0
        self.__aplicar_descuento()

    def __aplicar_descuento(self):
        if self.__infoCliente.isAdmin:
            self.__descuento = 50
            self.__precioCita *= 0.5
        elif self.__infoCliente.isEmployee:
            self.__descuento = 30
            self.__precioCita *= 0.7

    def cancelar(self, usuario):
        if usuario.puede_cancelar(self):
            self.__estado = "cancelada"
            return True
        return False

    def atender(self):
        if self.__estado == "pendiente":
            self.__estado = "atendida"
            return True
        return False

    # Getters
    def get_infoCliente(self):
        return self.__infoCliente

    def get_servicioContratado(self):
        return self.__servicioContratado

    def get_ccEncargado(self):
        return self.__ccEncargado

    def get_fechaCita(self):
        return self.__fechaCita

    def get_estado(self):
        return self.__estado

    def get_precioCita(self):
        return self.__precioCita

    def get_descuento(self):
        return self.__descuento

    # Setters (solo si necesitas modificar desde fuera)
    def set_ccEncargado(self, cedula):
        self.__ccEncargado = cedula

    def __str__(self):
        if self.__estado == "atendida":
            return (f"Cita de {self.__infoCliente.nombre} - {self.__servicioContratado.descripcion} - "
                    f"{self.__estado} - Precio final con descuento: ${self.__precioCita:.0f}")
        else:
            return (f"Cita de {self.__infoCliente.nombre} - {self.__servicioContratado.descripcion} - "
                    f"{self.__estado}")