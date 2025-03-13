#Author: Antonio Karlo Hernandez Pachecano
# Menu.py

class Menu:
    def __init__(self):
        self.mensaje = "Bienvenido al cajero automático"

    def mostrar(self):
        print(self.mensaje)
        while True:
            print("1. Retirar")
            print("2. Depositar")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.OpcionRetirar()
            elif opcion == "2":
                self.OpcionDepositar()
            elif opcion == "3":
                self.OpcionSalir()
                break
            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

    def OpcionRetirar(self):
        print("Desde la opción Retirar")

    def OpcionDepositar(self):
        print("Desde la opción Depositar")

    def OpcionSalir(self):
        print("Saliendo del cajero automático")
