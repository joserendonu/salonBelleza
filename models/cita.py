class Cita:
    def __init__(self, infoCliente, servicioContratado, ccEncargado, fechaCita):
        self.infoCliente = infoCliente
        self.servicioContratado = servicioContratado
        self.ccEncargado = ccEncargado
        self.fechaCita = fechaCita
        self.estado = "pendiente"
        self.precioCita = servicioContratado.precio
        self.descuento = 0
        self.aplicar_descuento()

    def aplicar_descuento(self):
        if self.infoCliente.isAdmin:
            self.descuento = 50
            self.precioCita *= 0.5
        elif self.infoCliente.isEmployee:
            self.descuento = 30
            self.precioCita *= 0.7

    def cancelar(self, usuario):
        if usuario.puede_cancelar(self):
            self.estado = "cancelada"
            return True
        return False

    def atender(self):
        if self.estado == "pendiente":
            self.estado = "atendida"
            return True
        return False

    def __str__(self):
        return f"Cita de {self.infoCliente.nombre} - {self.servicioContratado.descripcion} - {self.estado}"
