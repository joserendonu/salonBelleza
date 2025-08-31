from models.usuario import Usuario
from models.servicio import Servicio

# Usuarios quemados
usuarios = [
    Usuario("Administrador", "1001", "Ana", "Gomez", "3001112233", "1985-02-10", isAdmin=True),
    Usuario("Empleado", "2001", "Luis", "Perez", "3002223344", "1990-05-15", isEmployee=True),
    Usuario("Cliente", "3001", "Maria", "Lopez", "3003334455", "1995-07-20"),
]

# Servicios quemados
servicios = [
    Servicio("S01", "Corte de cabello", 20000, 30),
    Servicio("S02", "Manicure", 15000, 25),
    Servicio("S03", "Tintura", 50000, 90),
]
