class Cliente: 
    def _init_(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
    def imprimirDetalle(self): 
        print("Nombre: ", self.nombre,"Direccion", self.direccion, Edad: ", self.edad)
cliente1= Cliemte("Carlos", "calle Epuris 123", 35)
cliente1.imprimirDetalles()
