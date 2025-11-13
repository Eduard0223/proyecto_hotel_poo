# Sistema de Gestión Hotelera
from conexion.base_data import Database
from clases.huesped import Huesped
from clases.habitacion import Habitacion
from clases.reserva import Reserva

# conexion a la base de datos
db = Database()
conexion = db.conectar()

if conexion:
    # cerar objetos
    huesped = Huesped(conexion)
    habitacion = Habitacion(conexion)
    reserva = Reserva(conexion)
    
    # menu principal
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE HOTEL")
        print("="*50)
        print("1. Registrar huésped")
        print("2. Ver huéspedes")
        print("3. Ver habitaciones disponibles")
        print("4. Crear reserva")
        print("5. Ver reservas")
        print("6. Cancelar reserva")
        print("0. Salir")
        print("="*50)
        
        opcion = input("Seleccione opción: ")
        
        # opcion 1 registrar huesped
        if opcion == "1":
            print("\n--- REGISTRAR HUÉSPED ---")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            rut = input("RUT: ")
            
            if huesped.agregar(nombre, apellido, telefono, email, rut):
                print("Huésped registrado correctamente")
            else:
                print("Error al registrar")
        
        # opcion 2 ver huespedes
        elif opcion == "2":
            print("\n--- LISTA DE HUÉSPEDES ---")
            huespedes = huesped.listar()
            if huespedes:
                for h in huespedes:
                    print(f"ID: {h[0]} - {h[1]} {h[2]} - RUT: {h[5]}")
            else:
                print("No hay huéspedes")
        
        # opcion 3 ver habitaciones
        elif opcion == "3":
            print("\n--- HABITACIONES DISPONIBLES ---")
            habitaciones = habitacion.listar_disponibles()
            if habitaciones:
                for hab in habitaciones:
                    print(f"ID: {hab[0]} - Habitación {hab[1]} - Tipo: {hab[2]} - Precio: ${hab[3]}")
            else:
                print("No hay habitaciones disponibles")
        
        # opcion 4 crear reserva
        elif opcion == "4":
            print("\n--- CREAR RESERVA ---")
            
            # mostrar las habitaciones
            habitaciones = habitacion.listar_disponibles()
            if habitaciones:
                for hab in habitaciones:
                    print(f"ID: {hab[0]} - Hab. {hab[1]} - {hab[2]} - ${hab[3]}/noche")
            
            print("\nDatos del huésped:")
            rut = input("RUT: ")
            
            # buscar si existe
            h = huesped.buscar(rut)
            if h:
                print(f"Huésped encontrado: {h[1]} {h[2]}")
                huesped_id = h[0]
            else:
                print("Huésped no encontrado. Registrando...")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                if huesped.agregar(nombre, apellido, telefono, email, rut):
                    huesped_id = huesped.id
                else:
                    print("Error al registrar huésped")
                    continue
            
            # datos de reserva
            habitacion_id = input("\nID de habitación: ")
            fecha_entrada = input("Fecha entrada (YYYY-MM-DD): ")
            fecha_salida = input("Fecha salida (YYYY-MM-DD): ")
            
            # verificar disponibilidad
            if habitacion.esta_disponible(habitacion_id, fecha_entrada, fecha_salida):
                exito, total = reserva.crear(huesped_id, habitacion_id, fecha_entrada, fecha_salida)
                if exito:
                    print(f"\nReserva creada! Total: ${total}")
                else:
                    print("Error al crear reserva")
            else:
                print("La habitación NO está disponible en esas fechas")
        
        # opcion 5 ver reservas
        elif opcion == "5":
            print("\n--- LISTA DE RESERVAS ---")
            reservas = reserva.listar()
            if reservas:
                for r in reservas:
                    print(f"ID: {r[0]} - {r[1]} {r[2]} - Hab: {r[3]} - {r[4]} a {r[5]} - ${r[6]} - Estado: {r[7]}")
            else:
                print("No hay reservas")
        
        # opcion 6 cancelar reserva
        elif opcion == "6":
            reservas = reserva.listar()
            if reservas:
                for r in reservas:
                    print(f"ID: {r[0]} - {r[1]} {r[2]} - Estado: {r[7]}")
                
                id_reserva = input("\nID de reserva a cancelar: ")
                if reserva.cambiar_estado(id_reserva, 'cancelada'):
                    print("Reserva cancelada")
                else:
                    print("Error al cancelar")
            else:
                print("No hay reservas")
        
        # opcion salir o 0
        elif opcion == "0":
            print("\nCerrando programa...")
            db.cerrar()
            break
        
        else:
            print("Opción inválida")
        
        input("\nPresione ENTER para continuar...")

else:
    print("No se pudo conectar a la base de datos")