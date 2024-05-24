from random import randint


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"




juan = Persona("Juan", randint(25, 60))
Marta = Persona("Marta",randint(20,60))

print(juan.saludar())
print("")
print(Marta.saludar())
