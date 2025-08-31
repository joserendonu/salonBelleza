from data.seed_data import usuarios, servicios
from logic.gestion_citas import crear_cita, listar_citas
from models.cita import Cita
import datetime


def menu_cliente(usuario):
    while True:
        print(f"\n=== Menú Cliente ({usuario.nombre}) ===")
        print("1. Ver servicios")
        print("2. Crear cita")
        print("3. Ver mis citas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Servicios disponibles ---")
            for s in servicios:
                print(s)

        elif opcion == "2":
            print("\n--- Crear nueva cita ---")
            for i, s in enumerate(servicios):
                print(f"{i+1}. {s}")
            idx = int(input("Seleccione servicio: ")) - 1
            servicio = servicios[idx]
            empleado = next((u for u in usuarios if u.isEmployee), None)
            fecha = input("Ingrese fecha (YYYY-MM-DD): ")
            cita = crear_cita(usuario, servicio, empleado, fecha)
            print("✅ Cita creada:", cita)

        elif opcion == "3":
            print("\n--- Mis citas ---")
            for c in listar_citas():
                if c.infoCliente.cedula == usuario.cedula:
                    print(c)

        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_empleado(usuario):
    while True:
        print(f"\n=== Menú Empleado ({usuario.nombre}) ===")
        print("1. Ver citas asignadas")
        print("2. Atender cita")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for c in listar_citas():
                if c.ccEncargado == usuario.cedula:
                    print(c)

        elif opcion == "2":
            cc = input("Ingrese cédula del cliente de la cita a atender: ")
            for c in listar_citas():
                if c.infoCliente.cedula == cc and c.ccEncargado == usuario.cedula:
                    if c.atender():
                        print("✅ Cita atendida:", c)
                    else:
                        print("⚠️ No se pudo atender la cita.")
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_admin(usuario):
    while True:
        print(f"\n=== Menú Administrador ({usuario.nombre}) ===")
        print("1. Ver todas las citas")
        print("2. Cancelar cita")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for c in listar_citas():
                print(c)

        elif opcion == "2":
            cc = input("Ingrese cédula del cliente de la cita a cancelar: ")
            for c in listar_citas():
                if c.infoCliente.cedula == cc:
                    if c.cancelar(usuario):
                        print("✅ Cita cancelada:", c)
                    else:
                        print("⚠️ No se pudo cancelar la cita.")

        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def main():
    print("=== SALÓN DE BELLEZA ===")
    print("Usuarios disponibles para login (cedula):")
    for u in usuarios:
        print(f"{u.cedula} - {u.tipo} ({u.nombre})")

    ced = input("\nIngrese su cédula: ")
    usuario = next((u for u in usuarios if u.cedula == ced), None)

    if not usuario:
        print("Usuario no encontrado.")
        return

    if usuario.isAdmin:
        menu_admin(usuario)
    elif usuario.isEmployee:
        menu_empleado(usuario)
    else:
        menu_cliente(usuario)


if __name__ == "__main__":
    main()
