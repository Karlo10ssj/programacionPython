class Cliente: 
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
    def imprimirDetalle(self): 
        print("Nombre: ", self.nombre,"Direccion", self.direccion, Edad: ", self.edad)
cliente1= Cliente("Carlos", "calle Epuris 123", 35)
cliente1.imprimirDetalles()
