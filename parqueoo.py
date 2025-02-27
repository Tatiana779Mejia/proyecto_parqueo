import re 
from datetime import datetime 

class Parqueo:
    TARIFA_POR_HORA = 2.0  # Tarifa fija por hora

    def __init__(self, total_espacios):
        self.espacios_disponibles = total_espacios
        self.estacionados = {}

        # registrar entrada

    def registrar_entrada(self):
        """Registra la entrada de un vehículo."""
        if self.espacios_disponibles > 0:
            placa = input("\nIngresa la placa del vehículo: ").upper().strip()

            # Validar placa (alfanumérica, 5-8 caracteres)
            if not re.match(r'^[A-Z0-9-]{5,8}$', placa):
                print("\n⚠️ Placa inválida. Usa solo letras y números (Ej: ABC123).")
                return

            if placa in self.estacionados:
                print("\n🚗 ¡Este vehículo ya está registrado!")
            else:
                self.estacionados[placa] = {
                    "hora_entrada": datetime.now()
                }
                self.espacios_disponibles -= 1
                print(f"\n✅ ¡Vehículo {placa} registrado con éxito!")
        else:
            print("\n🚫 ¡No hay espacios disponibles! Intenta más tarde.")
        print("-" * 40)
        # Registrar salida
    def registrar_salida(self):
        """Registra la salida de un vehículo y cobra el estacionamiento."""
        placa = input("\nIngresa la placa del vehículo: ").upper().strip()

        #calcularemos la tarifa

        if placa in self.estacionados:
            tiempo_total = (datetime.now() - self.estacionados.pop(placa)["hora_entrada"]).total_seconds()
            horas = tiempo_total // 3600
            minutos = (tiempo_total % 3600) / 60
            monto = round((tiempo_total / 3600) * self.TARIFA_POR_HORA, 2)

        #+1 espacio disponible
            self.espacios_disponibles += 1
            print(f"\n🚗 ¡Vehículo {placa} salió con éxito!")
            print(f"⏳ Tiempo estacionado: {int(horas)} horas y {int(minutos)} minutos")
            print(f"💲 Monto a pagar: ${monto:.2f}")
        else:
            print("\n❌ ¡Placa no registrada en el parqueo!")
        print("-" * 40)

        # Espacios displonibles

    def ver_espacios_disponibles(self):
        """Muestra la cantidad de espacios disponibles en el parqueo."""
        print(f"\n🅿️ Espacios disponibles: {self.espacios_disponibles}")
        print("-" * 40)

    def menu(self):
        """Muestra el menú interactivo del parqueo."""
        while True:
            print("\n" + "=" * 40)
            print("🚘 Sistema de Parqueo")
            print("=" * 40)
            print("1. Registrar Entrada")
            print("2. Registrar Salida y Cobrar")
            print("3. Ver Espacios Disponibles")
            print("4. Salir")
            opcion = input("\n🔹 Elige una opción (1-4): ").strip()

            if opcion == "1":
                self.registrar_entrada()
            elif opcion == "2":
                self.registrar_salida()
            elif opcion == "3":
                self.ver_espacios_disponibles()
            elif opcion == "4":
                print("\n✅ ¡Gracias por usar el sistema de parqueo!")
                break
            else:
                print("\n⚠️ Opción inválida. Intenta nuevamente.")
            print("-" * 40)

if __name__ == "__main__":
    parqueo = Parqueo(10)  # Iniciar parqueo con 10 espacios
    parqueo.menu()
