#Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las operaciones matematicas basicas
#(suma, resta, multiplicacion y division).

class NumeroComplejo(object):

    # Constructor
    def __init__(self, numeroReal, numeroImaginario):
        self.parteReal = numeroReal
        self.parteImaginario = numeroImaginario

    # Metodo para sumar un numero complejo
    def suma(self, numeroComplejo):
        return (self.parteReal + numeroComplejo.parteReal), (self.parteImaginario + numeroComplejo.parteImaginario)

    # Metodo para restar un numero complejo
    def resta(self, numeroComplejo):
        return (self.parteReal - numeroComplejo.parteReal), (self.parteImaginario - numeroComplejo.parteImaginario)

    # Metodo para multiplicar un numero complejo
    def multiplicacion(self, numeroComplejo):
        return (self.parteReal * numeroComplejo.parteReal) - (self.parteImaginario * numeroComplejo.parteImaginario), (self.parteReal * numeroComplejo.parteImaginario) + (self.parteImaginario * numeroComplejo.parteReal)

    # Metodo para dividir un numero complejo
    def division(self, numeroComplejo):
        return ((self.parteReal * numeroComplejo.parteReal) + (self.parteImaginario * numeroComplejo.parteImaginario)) / ((numeroComplejo.parteReal * numeroComplejo.parteReal) + (numeroComplejo.parteImaginario * numeroComplejo.parteImaginario)), ((self.parteImaginario * numeroComplejo.parteReal) - (self.parteReal * numeroComplejo.parteImaginario)) / ((numeroComplejo.parteReal * numeroComplejo.parteReal) + (numeroComplejo.parteImaginario * numeroComplejo.parteImaginario))

    # Metodo para mostrar el numero complejo
    def mostrar(self):
        return self.parteReal, self.parteImaginario