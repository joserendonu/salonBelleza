# Autores Samuel Diaz, Jonathan Urriago, Sara Peña
from models.cita import Cita

citas = []

def crear_cita(cliente, servicio, empleado, fecha):
    nueva = Cita(cliente, servicio, empleado.cedula, fecha)
    citas.append(nueva)
    return nueva

def listar_citas():
    return citas
