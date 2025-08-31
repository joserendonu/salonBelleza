# Autores Samuel Diaz, Jonathan Urriago, Sara Peña

from models.usuario import Administrador, Empleado, Cliente
from models.servicio import Servicio

usuarios = [
    Administrador("1001", "Ana", "Gomez", "3001112233", "1985-02-10"),
    Administrador("1002", "Alejandro", "Roldán", "4001112233", "1985-02-15"),
    Empleado("2001", "Luis", "Perez", "3002223344", "1990-05-15"),
    Empleado("2002", "Juan", "Pardo", "5002223344", "1990-05-25"),
    Cliente("3001", "Maria", "Lopez", "3003334455", "1995-07-20"),
    Cliente("3002", "Manuela", "Pulgarin", "3003334444", "1995-05-20"),
    Cliente("3003", "Carlos", "Duque", "3003334466", "1992-08-10", isEmployee=True),  # Cliente que también es empleado
]

# Servicios quemados
servicios = [
    Servicio("S01", "Corte de cabello", 20000, 30),
    Servicio("S02", "Manicure", 15000, 25),
    Servicio("S03", "Tintura", 50000, 90),
]
