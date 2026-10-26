# Hacer una clase vehículo, que nos va a servir de base para otras los vehículos tienen atributos y métodos generales, 
# pero especialmente un deposito de combustible y un método para arrancar o parar además, 
# quiero que hagamos un tren, un avión y un barco el tren, el avion y el barco solo deberían poder marchar, 
# volar o navegar si están encendidos

class Vehiculo:
    def __init__(self, nombre, deposito):
        self.nombre = nombre
        self.deposito = deposito
        self.encendido = False

    def arranque(self):
        if self.encendido:
            self.encendido = False
            print(f"{self.nombre} parado")
        elif self.deposito <= 0:
            print(f"{self.nombre} no puede arrancar, no tiene combustible")
        else:
            self.encendido = True
            print(f"{self.nombre} encendido")

class Tren(Vehiculo):
    def marchar(self):
        if not self.encendido:
            print(f"{self.nombre} parado")
            return
        print(f"{self.nombre} circulando")

class Avion(Vehiculo):
    def volar(self):
        if not self.encendido:
            print(f"{self.nombre} parado")
            return
        print(f"{self.nombre} volando")       

class Barco(Vehiculo):
    def navegar(self):
        if not self.encendido:
            print(f"{self.nombre} parado")
            return
        print(f"{self.nombre} navegando")

tren = Tren("Ouigo", 500)
avion = Avion("Airbus", 0)    
barco = Barco("FredOlsen", 200)

tren.marchar()
avion.volar()
tren.arranque()
avion.arranque()


 