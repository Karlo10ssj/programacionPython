#Autor: Antonio Karlo Hernández Pachecano
 class Cuenta:
    def __init__(self, saldo, tipo, propietario):
        self.saldo = saldo
        self.tipo = tipo
        self.propietario = propietario  
    def imprimirDetallesCuenta(self):
        print("Saldo:", self.saldo, "Tipo:", self.tipo, "Propietario:", self.propietario)

    def retirar(self):
        pass

    def depositar(self):
        pass
