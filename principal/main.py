from datetime import datetime
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clases.habitaciones import Habitacion
from clases.huesped import Huesped
from clases.reservas import Reserva

class MenuPrincipal:
    def __init__(self):
        self.habitaciones = {}  # Diccionario de habitaciones {id_habitacion: objeto_habitacion}
        self.huespedes = {}    # Diccionario de huéspedes {rut: objeto_huesped}
        self.reservas = {}     # Diccionario de reservas {id_reserva: objeto_reserva}
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        """Carga datos de ejemplo para el sistema"""
        # Crear algunas habitaciones de ejemplo
        habitaciones_inicial = [
            (1, "101", "Individual", 45000),
            (2, "102", "Doble", 65000),
            (3, "201", "Suite", 120000),
            (4, "202", "Familiar", 95000)
        ]
        for id_hab, num, tipo, precio in habitaciones_inicial:
            hab = Habitacion(id_hab, num, tipo, precio)
            self.habitaciones[id_hab] = hab

    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
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
        """Menú de gestión de habitaciones"""
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
        """Menú de gestión de huéspedes"""
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
        """Menú de gestión de reservas"""
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
        """Menú de reportes"""
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

    # Métodos de gestión de habitaciones
    def ver_habitaciones(self):
        """Muestra todas las habitaciones"""
        print("\n=== LISTADO DE HABITACIONES ===")
        for hab in self.habitaciones.values():
            hab.mostrar_detalles()

    def agregar_habitacion(self):
        """Agrega una nueva habitación"""
        print("\n=== AGREGAR HABITACIÓN ===")
        try:
            id_hab = len(self.habitaciones) + 1
            n_habitacion = input("Número de habitación: ")
            print("\nTipos disponibles:", ", ".join(Habitacion.TIPOS_VALIDOS.keys()))
            tipo = input("Tipo de habitación: ")
            precio = float(input("Precio por noche: "))
            
            hab = Habitacion(id_hab, n_habitacion, tipo, precio)
            self.habitaciones[id_hab] = hab
            hab.agregar_habitacion()
            print("Habitación agregada exitosamente")
        except ValueError as e:
            print(f"Error: {e}")

    def modificar_habitacion(self):
        """Modifica una habitación existente"""
        self.ver_habitaciones()
        id_hab = int(input("\nIngrese ID de la habitación a modificar: "))
        if id_hab in self.habitaciones:
            hab = self.habitaciones[id_hab]
            print("\nDeje en blanco para mantener el valor actual")
            
            nuevo_tipo = input("Nuevo tipo (Enter para mantener): ")
            nuevo_precio = input("Nuevo precio (Enter para mantener): ")
            
            kwargs = {}
            if nuevo_tipo:
                kwargs['tipo'] = nuevo_tipo
            if nuevo_precio:
                kwargs['precio_noche'] = float(nuevo_precio)
                
            if hab.modificar_habitacion(**kwargs):
                print("Habitación modificada exitosamente")
            else:
                print("No se realizaron modificaciones")
        else:
            print("Habitación no encontrada")

    def programar_limpieza_habitacion(self):
        """Programa la limpieza de una habitación"""
        self.ver_habitaciones()
        id_hab = int(input("\nIngrese ID de la habitación para limpieza: "))
        if id_hab in self.habitaciones:
            hab = self.habitaciones[id_hab]
            if hab.programar_limpieza():
                print("Limpieza programada exitosamente")
            else:
                print("No se pudo programar la limpieza")
        else:
            print("Habitación no encontrada")

    def agregar_nota_mantenimiento(self):
        """Agrega una nota de mantenimiento a una habitación"""
        self.ver_habitaciones()
        id_hab = int(input("\nIngrese ID de la habitación: "))
        if id_hab in self.habitaciones:
            hab = self.habitaciones[id_hab]
            nota = input("Ingrese nota de mantenimiento: ")
            hab.agregar_nota_mantenimiento(nota)
            print("Nota de mantenimiento agregada")
        else:
            print("Habitación no encontrada")

    # Métodos de gestión de huéspedes
    def ver_huespedes(self):
        """Muestra todos los huéspedes registrados"""
        print("\n=== LISTADO DE HUÉSPEDES ===")
        for huesped in self.huespedes.values():
            huesped.mostrar_informacion()
            print("-" * 40)

    def registrar_huesped(self):
        """Registra un nuevo huésped"""
        print("\n=== REGISTRAR HUÉSPED ===")
        try:
            id_huesped = len(self.huespedes) + 1
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            rut = input("RUT (formato: XXXXXXXX-X): ")
            telefono = input("Teléfono: ")
            correo = input("Correo electrónico: ")
            
            huesped = Huesped(id_huesped, nombre, apellido, rut, telefono, correo)
            self.huespedes[rut] = huesped
            huesped.crear_perfil()
            print("Huésped registrado exitosamente")
        except ValueError as e:
            print(f"Error: {e}")

    def buscar_huesped(self):
        """Busca un huésped por RUT"""
        rut = input("\nIngrese RUT del huésped: ")
        if rut in self.huespedes:
            self.huespedes[rut].mostrar_informacion()
        else:
            print("Huésped no encontrado")

    def actualizar_huesped(self):
        """Actualiza la información de un huésped"""
        rut = input("\nIngrese RUT del huésped a actualizar: ")
        if rut in self.huespedes:
            huesped = self.huespedes[rut]
            print("\nDeje en blanco para mantener el valor actual")
            
            nuevo_telefono = input("Nuevo teléfono (Enter para mantener): ")
            nuevo_correo = input("Nuevo correo (Enter para mantener): ")
            
            kwargs = {}
            if nuevo_telefono:
                kwargs['telefono'] = nuevo_telefono
            if nuevo_correo:
                kwargs['correo'] = nuevo_correo
                
            try:
                huesped.actualizar_informacion(**kwargs)
                print("Información actualizada exitosamente")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Huésped no encontrado")

    def ver_historial_huesped(self):
        """Muestra el historial de reservas de un huésped"""
        rut = input("\nIngrese RUT del huésped: ")
        if rut in self.huespedes:
            self.huespedes[rut].mostrar_historial_reservas()
        else:
            print("Huésped no encontrado")

    # Métodos de gestión de reservas
    def ver_reservas(self):
        """Muestra todas las reservas"""
        print("\n=== LISTADO DE RESERVAS ===")
        for reserva in self.reservas.values():
            detalles = reserva.obtener_detalles()
            for campo, valor in detalles.items():
                print(f"{campo}: {valor}")
            print("-" * 40)

    def crear_reserva(self):
        """Crea una nueva reserva"""
        print("\n=== CREAR RESERVA ===")
        try:
            # Buscar huésped
            rut = input("RUT del huésped: ")
            if rut not in self.huespedes:
                print("Huésped no encontrado. Primero debe registrar al huésped.")
                return

            # Mostrar habitaciones disponibles
            print("\nHabitaciones disponibles:")
            for hab in self.habitaciones.values():
                if hab.estado == "Disponible":
                    hab.mostrar_detalles()

            # Seleccionar habitación
            id_hab = int(input("\nID de la habitación deseada: "))
            if id_hab not in self.habitaciones:
                print("Habitación no encontrada")
                return

            # Fechas
            fecha_entrada = input("Fecha de entrada (YYYY-MM-DD): ")
            fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")

            # Crear reserva
            id_reserva = len(self.reservas) + 1
            reserva = Reserva(
                id_reserva,
                self.huespedes[rut],
                self.habitaciones[id_hab],
                fecha_entrada,
                fecha_salida
            )

            if reserva.confirmar_reserva():
                self.reservas[id_reserva] = reserva
                self.huespedes[rut].agregar_reserva(reserva)
                print("Reserva creada exitosamente")
                detalles = reserva.obtener_detalles()
                for campo, valor in detalles.items():
                    print(f"{campo}: {valor}")
            else:
                print("No se pudo confirmar la reserva")

        except ValueError as e:
            print(f"Error: {e}")

    def modificar_reserva(self):
        """Modifica una reserva existente"""
        id_reserva = int(input("\nIngrese ID de la reserva a modificar: "))
        if id_reserva in self.reservas:
            reserva = self.reservas[id_reserva]
            print("\nDeje en blanco para mantener el valor actual")
            
            nueva_fecha_entrada = input("Nueva fecha de entrada (YYYY-MM-DD) (Enter para mantener): ")
            nueva_fecha_salida = input("Nueva fecha de salida (YYYY-MM-DD) (Enter para mantener): ")
            
            if reserva.modificar_fechas(nueva_fecha_entrada, nueva_fecha_salida):
                print("Reserva modificada exitosamente")
                reserva.obtener_detalles()
            else:
                print("No se pudo modificar la reserva")
        else:
            print("Reserva no encontrada")

    def cancelar_reserva(self):
        """Cancela una reserva"""
        id_reserva = int(input("\nIngrese ID de la reserva a cancelar: "))
        if id_reserva in self.reservas:
            if self.reservas[id_reserva].cancelar_reserva():
                print("Reserva cancelada exitosamente")
            else:
                print("No se pudo cancelar la reserva")
        else:
            print("Reserva no encontrada")

    def hacer_check_in(self):
        """Realiza el check-in de una reserva"""
        id_reserva = int(input("\nIngrese ID de la reserva para check-in: "))
        if id_reserva in self.reservas:
            reserva = self.reservas[id_reserva]
            if reserva.estado == "Confirmada":
                reserva.habitacion.estado = "Ocupada"
                print("Check-in realizado exitosamente")
            else:
                print("La reserva debe estar confirmada para hacer check-in")
        else:
            print("Reserva no encontrada")

    def hacer_check_out(self):
        """Realiza el check-out de una reserva"""
        id_reserva = int(input("\nIngrese ID de la reserva para check-out: "))
        if id_reserva in self.reservas:
            if self.reservas[id_reserva].finalizar_reserva():
                print("Check-out realizado exitosamente")
            else:
                print("No se pudo realizar el check-out")
        else:
            print("Reserva no encontrada")

    # Métodos de reportes
    def reporte_habitaciones_disponibles(self):
        """Muestra las habitaciones disponibles"""
        print("\n=== HABITACIONES DISPONIBLES ===")
        disponibles = [h for h in self.habitaciones.values() if h.estado == "Disponible"]
        for hab in disponibles:
            hab.mostrar_detalles()
        print(f"\nTotal habitaciones disponibles: {len(disponibles)}")

    def reporte_reservas_actuales(self):
        """Muestra las reservas actuales"""
        print("\n=== RESERVAS ACTUALES ===")
        actuales = [r for r in self.reservas.values() if r.estado == "Confirmada"]
        for reserva in actuales:
            detalles = reserva.obtener_detalles()
            for campo, valor in detalles.items():
                print(f"{campo}: {valor}")
            print("-" * 40)
        print(f"\nTotal reservas actuales: {len(actuales)}")

    def reporte_ocupacion(self):
        """Muestra el porcentaje de ocupación del hotel"""
        total = len(self.habitaciones)
        ocupadas = len([h for h in self.habitaciones.values() if h.estado == "Ocupada"])
        porcentaje = (ocupadas / total * 100) if total > 0 else 0
        print(f"\nOcupación actual del hotel: {porcentaje:.2f}%")
        print(f"Habitaciones ocupadas: {ocupadas}")
        print(f"Total habitaciones: {total}")

    def reporte_ingresos(self):
        """Muestra los ingresos del período"""
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
