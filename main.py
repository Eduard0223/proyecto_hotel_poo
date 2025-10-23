# =================================================================
# hotel_db/menu.py
# Menú Principal con llamadas a métodos de persistencia.
# =================================================================

from datetime import datetime
import os
import sys
# Ajustar la ruta para importar correctamente 'clases' y 'db'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clases.habitaciones import Habitacion
from clases.huesped import Huesped
from clases.reservas import Reserva
from db.conexion import obtener_datos_iniciales 


class MenuPrincipal:
    def __init__(self):
        self.habitaciones = {}  
        self.huespedes = {}     
        self.reservas = {}      
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        """Carga datos EXISTENTES desde la base de datos."""
        print("Cargando datos desde la base de datos...")
        
        # 1. Cargar Habitaciones
        campos_hab = ["id_habitacion", "num_habitacion", "tipo", "precio_noche", "estado"]
        for row in obtener_datos_iniciales("habitaciones", campos_hab):
            hab = Habitacion(row['id_habitacion'], row['num_habitacion'], row['tipo'], row['precio_noche'], estado=row['estado'])
            self.habitaciones[hab.id] = hab
            
        # 2. Cargar Huéspedes
        campos_huesped = ["id_huesped", "nombre", "apellido", "rut", "telefono", "correo"]
        for row in obtener_datos_iniciales("huespedes", campos_huesped):
            huesped = Huesped(row['id_huesped'], row['nombre'], row['apellido'], row['rut'], row['telefono'], row['correo'])
            self.huespedes[huesped.rut] = huesped
            
        # 3. Cargar Reservas: REQUIERE lógica de JOIN/ID para relacionar objetos.
        # Por ahora, se omite esta carga para evitar complejidad sin las tablas de DB.
        
        print(f"Cargados {len(self.habitaciones)} habitaciones y {len(self.huespedes)} huéspedes.")

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu_principal(self):
        while True:
            self.limpiar_pantalla()
            print("\n=== SISTEMA DE GESTIÓN HOTELERA ===")
            print("1. Gestión de Habitaciones")
            print("2. Gestión de Huéspedes")
            print("3. Gestión de Reservas")
            print("4. Reportes")
            print("5. Salir")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.menu_habitaciones()
            elif opcion == "2":
                self.menu_huespedes()
            elif opcion == "3":
                self.menu_reservas()
            elif opcion == "4":
                self.menu_reportes()
            elif opcion == "5":
                print("\n¡Gracias por usar el sistema!")
                break
            else:
                input("\nOpción inválida. Presione Enter para continuar...")

    def menu_habitaciones(self):
        while True:
            self.limpiar_pantalla()
            print("\n=== GESTIÓN DE HABITACIONES ===")
            print("1. Ver todas las habitaciones")
            print("2. Agregar habitación")
            print("3. Modificar habitación")
            print("4. Programar limpieza")
            print("5. Agregar nota de mantenimiento")
            print("6. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.ver_habitaciones()
            elif opcion == "2":
                self.agregar_habitacion()
            elif opcion == "3":
                self.modificar_habitacion()
            elif opcion == "4":
                self.programar_limpieza_habitacion()
            elif opcion == "5":
                self.agregar_nota_mantenimiento()
            elif opcion == "6":
                break
            
            input("\nPresione Enter para continuar...")

    def menu_huespedes(self):
        while True:
            self.limpiar_pantalla()
            print("\n=== GESTIÓN DE HUÉSPEDES ===")
            print("1. Ver todos los huéspedes")
            print("2. Registrar nuevo huésped")
            print("3. Buscar huésped")
            print("4. Actualizar información de huésped")
            print("5. Ver historial de reservas de huésped")
            print("6. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.ver_huespedes()
            elif opcion == "2":
                self.registrar_huesped()
            elif opcion == "3":
                self.buscar_huesped()
            elif opcion == "4":
                self.actualizar_huesped()
            elif opcion == "5":
                self.ver_historial_huesped()
            elif opcion == "6":
                break
            
            input("\nPresione Enter para continuar...")

    def menu_reservas(self):
        while True:
            self.limpiar_pantalla()
            print("\n=== GESTIÓN DE RESERVAS ===")
            print("1. Ver todas las reservas")
            print("2. Crear nueva reserva")
            print("3. Modificar reserva")
            print("4. Cancelar reserva")
            print("5. Check-in")
            print("6. Check-out")
            print("7. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.ver_reservas()
            elif opcion == "2":
                self.crear_reserva()
            elif opcion == "3":
                self.modificar_reserva()
            elif opcion == "4":
                self.cancelar_reserva()
            elif opcion == "5":
                self.hacer_check_in()
            elif opcion == "6":
                self.hacer_check_out()
            elif opcion == "7":
                break
            
            input("\nPresione Enter para continuar...")

    def menu_reportes(self):
        # Los métodos de reporte (4.1 a 4.4) se mantienen igual, usando la data cargada.
        while True:
            self.limpiar_pantalla()
            print("\n=== REPORTES ===")
            print("1. Habitaciones disponibles")
            print("2. Reservas actuales")
            print("3. Ocupación del hotel")
            print("4. Ingresos del período")
            print("5. Volver al menú principal")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.reporte_habitaciones_disponibles()
            elif opcion == "2":
                self.reporte_reservas_actuales()
            elif opcion == "3":
                self.reporte_ocupacion()
            elif opcion == "4":
                self.reporte_ingresos()
            elif opcion == "5":
                break
            
            input("\nPresione Enter para continuar...")


    # =================================================================
    # MÉTODOS DE GESTIÓN CON PERSISTENCIA
    # =================================================================

    # --- Habitaciones ---

    def ver_habitaciones(self):
        print("\n=== LISTADO DE HABITACIONES ===")
        for hab in self.habitaciones.values():
            hab.mostrar_detalles()

    def agregar_habitacion(self):
        print("\n=== AGREGAR HABITACIÓN ===")
        try:
            n_habitacion = input("Número de habitación: ")
            print("\nTipos disponibles:", ", ".join(Habitacion.TIPOS_VALIDOS.keys()))
            tipo = input("Tipo de habitación: ")
            precio = float(input("Precio por noche: "))
            
            # ID None: será actualizado por el método de la clase con el ID de la DB
            hab = Habitacion(None, n_habitacion, tipo, precio) 
            
            if hab.agregar_habitacion(): # INSERT en DB
                self.habitaciones[hab.id] = hab 
                print(f"Habitación agregada y registrada en la base de datos (ID: {hab.id}).")
            else:
                 print("Error: No se pudo agregar la habitación a la base de datos.")
        except ValueError as e:
            print(f"Error: {e}")

    def modificar_habitacion(self):
        self.ver_habitaciones()
        try:
            id_hab = int(input("\nIngrese ID de la habitación a modificar: "))
        except ValueError:
            print("ID no válido.")
            return

        if id_hab in self.habitaciones:
            hab = self.habitaciones[id_hab]
            print("\nDeje en blanco para mantener el valor actual")
            
            nuevo_tipo = input(f"Nuevo tipo (Actual: {hab.tipo}): ")
            nuevo_precio_str = input(f"Nuevo precio (Actual: {hab.precio_noche}): ")
            
            kwargs = {}
            if nuevo_tipo:
                kwargs['tipo'] = nuevo_tipo
            if nuevo_precio_str:
                kwargs['precio_noche'] = float(nuevo_precio_str)
            
            if hab.modificar_habitacion(**kwargs): # UPDATE en DB
                print("Habitación modificada exitosamente y actualizada en la base de datos.")
            else:
                print("No se realizaron modificaciones o hubo un error en la base de datos.")
        else:
            print("Habitación no encontrada")

    def programar_limpieza_habitacion(self):
        self.ver_habitaciones()
        try:
            id_hab = int(input("\nIngrese ID de la habitación para limpieza: "))
        except ValueError:
            print("ID no válido.")
            return
            
        if id_hab in self.habitaciones:
            hab = self.habitaciones[id_hab]
            if hab.programar_limpieza(): # UPDATE en DB
                print("Limpieza programada exitosamente y actualizada en la base de datos.")
            else:
                print("No se pudo programar la limpieza")
        else:
            print("Habitación no encontrada")

    def agregar_nota_mantenimiento(self):
        self.ver_habitaciones()
        try:
            id_hab = int(input("\nIngrese ID de la habitación: "))
        except ValueError:
            print("ID no válido.")
            return
            
        if id_hab in self.habitaciones:
            hab = self.habitaciones[id_hab]
            nota = input("Ingrese nota de mantenimiento: ")
            if hab.agregar_nota_mantenimiento(nota): # UPDATE en DB
                print("Nota de mantenimiento agregada y estado actualizado a Mantenimiento.")
            else:
                print("Error al actualizar la base de datos.")
        else:
            print("Habitación no encontrada")

    # --- Huéspedes ---

    def ver_huespedes(self):
        print("\n=== LISTADO DE HUÉSPEDES ===")
        for huesped in self.huespedes.values():
            huesped.mostrar_informacion()
            print("-" * 40)

    def registrar_huesped(self):
        print("\n=== REGISTRAR HUÉSPED ===")
        try:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            rut = input("RUT (formato: XXXXXXXX-X): ")
            telefono = input("Teléfono: ")
            correo = input("Correo electrónico: ")
            
            if rut in self.huespedes:
                print("Error: El RUT ya está registrado.")
                return

            huesped = Huesped(None, nombre, apellido, rut, telefono, correo)
            
            if huesped.crear_perfil(): # INSERT en DB
                self.huespedes[rut] = huesped
                print("Huésped registrado y perfil creado en la base de datos.")
            else:
                 print("Error: No se pudo crear el perfil del huésped en la base de datos.")

        except ValueError as e:
            print(f"Error: {e}")

    def buscar_huesped(self):
        rut = input("\nIngrese RUT del huésped: ")
        if rut in self.huespedes:
            self.huespedes[rut].mostrar_informacion()
        else:
            print("Huésped no encontrado")

    def actualizar_huesped(self):
        rut = input("\nIngrese RUT del huésped a actualizar: ")
        if rut in self.huespedes:
            huesped = self.huespedes[rut]
            print("\nDeje en blanco para mantener el valor actual")
            
            nuevo_telefono = input(f"Nuevo teléfono (Actual: {huesped.telefono}): ")
            nuevo_correo = input(f"Nuevo correo (Actual: {huesped.correo}): ")
            
            kwargs = {}
            if nuevo_telefono:
                kwargs['telefono'] = nuevo_telefono
            if nuevo_correo:
                kwargs['correo'] = nuevo_correo
                
            try:
                if huesped.actualizar_informacion(**kwargs): # UPDATE en DB
                     print("Información actualizada exitosamente y en la base de datos.")
                else:
                    print("No se realizaron modificaciones o hubo un error en la base de datos.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Huésped no encontrado")

    def ver_historial_huesped(self):
        rut = input("\nIngrese RUT del huésped: ")
        if rut in self.huespedes:
            self.huespedes[rut].mostrar_historial_reservas()
        else:
            print("Huésped no encontrado")

    # --- Reservas ---

    def ver_reservas(self):
        print("\n=== LISTADO DE RESERVAS ===")
        for reserva in self.reservas.values():
            detalles = reserva.obtener_detalles()
            for campo, valor in detalles.items():
                print(f"{campo}: {valor}")
            print("-" * 40)

    def crear_reserva(self):
        print("\n=== CREAR RESERVA ===")
        try:
            rut = input("RUT del huésped: ")
            if rut not in self.huespedes:
                print("Huésped no encontrado. Primero debe registrar al huésped.")
                return

            print("\nHabitaciones disponibles:")
            disponibles = [h for h in self.habitaciones.values() if h.estado == "Disponible"]
            for hab in disponibles:
                hab.mostrar_detalles()

            id_hab = int(input("\nID de la habitación deseada: "))
            
            if id_hab not in self.habitaciones or self.habitaciones[id_hab].estado != "Disponible":
                print("Habitación no encontrada o no disponible")
                return

            fecha_entrada = input("Fecha de entrada (YYYY-MM-DD): ")
            fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")

            reserva = Reserva(
                None, # ID None, será actualizado por la clase
                self.huespedes[rut],
                self.habitaciones[id_hab],
                fecha_entrada,
                fecha_salida
            )

            if reserva.confirmar_reserva(): # INSERT en 'reservas' y UPDATE en 'habitaciones'
                self.reservas[reserva.id] = reserva
                self.huespedes[rut].agregar_reserva(reserva)
                print("Reserva creada y registrada en la base de datos.")
            else:
                print("No se pudo confirmar la reserva.")

        except ValueError as e:
            print(f"Error: {e}")

    def modificar_reserva(self):
        # Este método debe ser actualizado para usar reserva.modificar_fechas()
        print("\nFuncionalidad de modificación de reserva pendiente de implementar con persistencia DB.")

    def cancelar_reserva(self):
        id_reserva = int(input("\nIngrese ID de la reserva a cancelar: "))
        if id_reserva in self.reservas:
            if self.reservas[id_reserva].cancelar_reserva(): # UPDATE en 'reservas' y 'habitaciones'
                print("Reserva cancelada exitosamente y actualizada en la base de datos.")
            else:
                print("No se pudo cancelar la reserva")
        else:
            print("Reserva no encontrada")

    def hacer_check_in(self):
        id_reserva = int(input("\nIngrese ID de la reserva para check-in: "))
        if id_reserva in self.reservas:
            reserva = self.reservas[id_reserva]
            if reserva.estado == "Confirmada":
                if reserva.realizar_check_in(): # UPDATE en 'reservas' y 'habitaciones'
                    print("Check-in realizado exitosamente y actualizado en la base de datos.")
                else:
                    print("Error al realizar check-in en la base de datos.")
            else:
                print("La reserva debe estar confirmada para hacer check-in")
        else:
            print("Reserva no encontrada")

    def hacer_check_out(self):
        id_reserva = int(input("\nIngrese ID de la reserva para check-out: "))
        if id_reserva in self.reservas:
            if self.reservas[id_reserva].finalizar_reserva(): # UPDATE en 'reservas' y 'habitaciones'
                print("Check-out realizado exitosamente y actualizado en la base de datos.")
            else:
                print("No se pudo realizar el check-out")
        else:
            print("Reserva no encontrada")
    
    # --- Métodos de reportes (se mantienen igual) ---

    def reporte_habitaciones_disponibles(self):
        print("\n=== HABITACIONES DISPONIBLES ===")
        disponibles = [h for h in self.habitaciones.values() if h.estado == "Disponible"]
        for hab in disponibles:
            hab.mostrar_detalles()
        print(f"\nTotal habitaciones disponibles: {len(disponibles)}")

    def reporte_reservas_actuales(self):
        print("\n=== RESERVAS ACTUALES ===")
        actuales = [r for r in self.reservas.values() if r.estado == "Confirmada"]
        for reserva in actuales:
            detalles = reserva.obtener_detalles()
            for campo, valor in detalles.items():
                print(f"{campo}: {valor}")
            print("-" * 40)
        print(f"\nTotal reservas actuales: {len(actuales)}")

    def reporte_ocupacion(self):
        total = len(self.habitaciones)
        ocupadas = len([h for h in self.habitaciones.values() if h.estado == "Ocupada"])
        porcentaje = (ocupadas / total * 100) if total > 0 else 0
        print(f"\nOcupación actual del hotel: {porcentaje:.2f}%")
        print(f"Habitaciones ocupadas: {ocupadas}")
        print(f"Total habitaciones: {total}")

    def reporte_ingresos(self):
        print("\n=== REPORTE DE INGRESOS ===")
        total = sum(r.total for r in self.reservas.values() if r.estado in ["Confirmada", "Finalizada"])
        print(f"Ingresos totales: ${total:,.0f}")
        print("\nDesglose por estado:")
        for estado in ["Confirmada", "Finalizada"]:
            subtotal = sum(r.total for r in self.reservas.values() if r.estado == estado)
            print(f"{estado}: ${subtotal:,.0f}")


if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.mostrar_menu_principal()