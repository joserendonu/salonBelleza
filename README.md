# tengo una app en python llamada salonBelleza
Existen las clases: 
    Servicio: codigo, descripcion, precio, duracion, 
    Usuario: tipo(Administrador, Empleado, Cliente), 
            cedula, nombre, apellido, telefono, fechaNacimiento, servicio, isEmployee,
            isAdmin, 
    Cita: infoCliente, servicioContratado, ccEncargado, fechaCita, estado("pendiente", "atendida", "cancelada"),
          precioCita, descuento,
# si es admin 50%, si es empleado lo atiende otro empleado y descuento 30%
# se puede cancelar una cita si tiene estado pendiente y es el mismo usuario que va a tener la cita o es admin
# necesito que cada clase esté en un archivo aparte y crear archivos distribuidos para la lógica del negocio
# necesito que no haya base de datos sino que se quemen 3 usuarios un administrador, 
# un empleado y un cliente 
# finalmente deseo qie se genere un ejecutable donde al seleccionar el tipo de usuario muestre las opciones que va a tener cada tipo de usuario 




