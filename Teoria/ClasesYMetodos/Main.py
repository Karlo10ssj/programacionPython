#Author: Antonio Karlo Hernandez Pachecano
from Cliente import Cliente
from Cuenta import Cuenta
from Menu import Menu

cliente1 = Cliente("Maria", "Iztapalapa 11", 25)
cuenta1 = Cuenta(1000, "debito", cliente1.nombre)  # Acceso directo al atributo público

# Crear instancia de Menu y mostrar el menú
menu = Menu(cliente1, cuenta1)
menu.mostrar()
