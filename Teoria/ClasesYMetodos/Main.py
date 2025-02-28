#Author: Antonio Karlo Hernandez Pachecano
from Cliente import Cliente
from Cuenta import Cuenta

class Main: 
    pass
class mensajeBienvenida(): 
    def __init__(self):
        pass
    def darBienvenida(self): 
        print("Hola")
        
mensaje = mensajeBienvenida()
mensaje.darBienvenida()

Cliente1 = Cliente("Maria", "Iztapalapa 11", 18)
imprimirDetalles(cliente1)
Cuenta1 = Cuenta(250, "debito", "Maria")

