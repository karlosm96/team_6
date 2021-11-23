# Crear una clase que represente un vector de 3 dimensiones. Tenga 4 metodos que permitan las operaciones matematicas basicas (+,-,* y / por un escalar)

class Vector3Dimensiones:
    #Constructor de la clase 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    #Metodo para sumar
    def suma(self, vector):
        return self.x + vector.x, self.y + vector.y, self.z + vector.z
    
    #Metodo para restar
    def resta(self, vector):
        return self.x - vector.x, self.y - vector.y, self.z - vector.z
    
    #Metodo para multiplicar
    def multiplicacion(self, escalar):
        return self.x * escalar, self.y * escalar, self.z * escalar
    
    #Metodo para dividir
    def division(self, escalar):
        return self.x / escalar, self.y / escalar, self.z / escalar
    
    