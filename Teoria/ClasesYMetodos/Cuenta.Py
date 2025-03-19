#Autor: Antonio Karlo Hernández Pachecano
 class Cuenta:
    def __init__(self, saldo, tipo, propietario):
        self.saldo = saldo
        self.tipo = tipo
        self.propietario = propietario  
    def imprimirDetallesCuenta(self):
        print("Saldo:", self.saldo, "Tipo:", self.tipo, "Propietario:", self.propietario)

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo restante: {self.saldo}")
            return True
        else:
            print("Fondos insuficientes o cantidad inválida.")
            return False

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
print(f"Depósito exitoso. Saldo actual: {self.saldo}")
            return True
        else:
            print("Cantidad inválida.")
            return False
