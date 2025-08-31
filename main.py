# Autores Samuel Diaz, Jonathan Urriago, Sara Peña
from data.seed_data import usuarios, servicios
from logic.gestion_citas import crear_cita, listar_citas
from models import usuario
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
                if c.get_infoCliente().cedula == usuario.cedula:
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
        print("9. Cambiar usuario")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for c in listar_citas():
                if c.get_ccEncargado() == usuario.cedula:
                    print(c)
        elif opcion == "2":
            cc = input("Ingrese cédula del cliente de la cita a atender: ")
            for c in listar_citas():
                if c.get_infoCliente().cedula == cc and c.get_ccEncargado() == usuario.cedula:
                    if c.atender():
                        print("✅ Cita atendida:", c)
                    else:
                        print("⚠️ No se pudo atender la cita.")

        elif opcion == "9":
            return  # Regresa al menú inicial

        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_admin(usuario):
    while True:
        print(f"\n=== Menú Administrador ({usuario.nombre}) ===")
        print("1. Ver todas las citas")
        print("2. Cancelar cita")
        print("3. Asignar cita")
        print("4. Crear cita para mí")
        print("9. Cambiar usuario")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for c in listar_citas():
                print(c)
        elif opcion == "2":
            cc = input("Ingrese cédula del cliente de la cita a cancelar: ")
            for c in listar_citas():
                if c.get_infoCliente().cedula == cc:
                    if c.cancelar(usuario):
                        print("✅ Cita cancelada:", c)
                    else:
                        print("⚠️ No se pudo cancelar la cita.")
        elif opcion == "3":
            print("\n--- Asignar nueva cita ---")
            clientes = [u for u in usuarios if not u.isEmployee or u.tipo() == "Cliente"]
            for i, c in enumerate(clientes):
                print(f"{i+1}. {c.nombre} {c.apellido} ({c.cedula})")
            idx_cliente = int(input("Seleccione cliente: ")) - 1
            cliente = clientes[idx_cliente]
            for i, s in enumerate(servicios):
                print(f"{i+1}. {s}")
            idx_servicio = int(input("Seleccione servicio: ")) - 1
            servicio = servicios[idx_servicio]
            empleados = [u for u in usuarios if u.isEmployee]
            for i, e in enumerate(empleados):
                print(f"{i+1}. {e.nombre} {e.apellido} ({e.cedula})")
            idx_empleado = int(input("Seleccione empleado: ")) - 1
            empleado = empleados[idx_empleado]
            fecha = input("Ingrese fecha (YYYY-MM-DD): ")
            cita = crear_cita(cliente, servicio, empleado, fecha)
            print("✅ Cita asignada:", cita)
            pass
        elif opcion == "4":
            print("\n--- Crear cita para administrador ---")
            for i, s in enumerate(servicios):
                print(f"{i+1}. {s}")
            idx_servicio = int(input("Seleccione servicio: ")) - 1
            servicio = servicios[idx_servicio]
            empleados = [u for u in usuarios if u.isEmployee]
            for i, e in enumerate(empleados):
                print(f"{i+1}. {e.nombre} {e.apellido} ({e.cedula})")
            idx_empleado = int(input("Seleccione empleado: ")) - 1
            empleado = empleados[idx_empleado]
            fecha = input("Ingrese fecha (YYYY-MM-DD): ")
            cita = crear_cita(usuario, servicio, empleado, fecha)
            print("✅ Cita creada:", cita)
        elif opcion == "9":
            return
        elif opcion == "0":
            break
        else:
            print("Opción inválida")



def main():
    while True:
        print("=== SALÓN DE BELLEZA ===")
        print("Usuarios disponibles para login:")
        for i, u in enumerate(usuarios):
            print(f"{i+1}. {u.cedula} - {u.tipo()} ({u.nombre})")

        try:
            idx = int(input("\nSeleccione el número de usuario: ")) - 1
            usuario = usuarios[idx]
        except (ValueError, IndexError):
            print("Selección inválida.")
            continue

        # Si es cliente y empleado, preguntar el menú
        if usuario.tipo() == "Cliente" and hasattr(usuario, "isEmployee") and usuario.isEmployee:
            print("\nEste usuario es Cliente y Empleado.")
            rol = input("¿Desea entrar como (1) Cliente o (2) Empleado? ")
            if rol == "2":
                menu_empleado(usuario)
            else:
                menu_cliente(usuario)
        elif usuario.tipo() == "Administrador":
            menu_admin(usuario)
        elif usuario.tipo() == "Empleado":
            menu_empleado(usuario)
        else:
            menu_cliente(usuario)


if __name__ == "__main__":
    main()
