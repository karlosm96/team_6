#Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las operaciones matematicas basicas
#(suma, resta, multiplicacion y division).

class NumeroComplejo:

    # Constructor de la clase
    def __init__(self, numeroReal, numeroImaginario):
        self.parteReal = numeroReal
        self.parteImaginario = numeroImaginario

    # Metodo para sumar 
    def suma(self, numeroComplejo):
        return (self.parteReal + numeroComplejo.parteReal), (self.parteImaginario + numeroComplejo.parteImaginario)

    # Metodo para restar 
    def resta(self, numeroComplejo):
        return (self.parteReal - numeroComplejo.parteReal), (self.parteImaginario - numeroComplejo.parteImaginario)

    # Metodo para multiplicar 
    def multiplicacion(self, numeroComplejo):
        return (self.parteReal * numeroComplejo.parteReal) - (self.parteImaginario * numeroComplejo.parteImaginario), (self.parteReal * numeroComplejo.parteImaginario) + (self.parteImaginario * numeroComplejo.parteReal)

    # Metodo para dividir 
    def division(self, numeroComplejo):
        return ((self.parteReal * numeroComplejo.parteReal) + (self.parteImaginario * numeroComplejo.parteImaginario)) / ((numeroComplejo.parteReal * numeroComplejo.parteReal) + (numeroComplejo.parteImaginario * numeroComplejo.parteImaginario)), ((self.parteImaginario * numeroComplejo.parteReal) - (self.parteReal * numeroComplejo.parteImaginario)) / ((numeroComplejo.parteReal * numeroComplejo.parteReal) + (numeroComplejo.parteImaginario * numeroComplejo.parteImaginario))
