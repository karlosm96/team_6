#Crear una clase que represente una matriz de 3x3 dimensiones. Tengan 3 metodos que permitan las operaciones matematicas basicas (excluimos la division) (+ y - entre matrices, * solo por un vector).

class Matriz3x3Dimensiones:

    #Constructor de la clase 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    #Metodo para sumar por una matriz
    def suma_matriz(self, matriz):
        return self.x + matriz.x, self.y + matriz.y, self.z + matriz.z
    
    #Metodo para restar por una matriz
    def resta_matriz(self, matriz):
        return self.x - matriz.x, self.y - matriz.y, self.z - matriz.z
          
    #Metodo para multiplicar por un vector
    def multiplicacion_vector(self, vector):
        return self.x * vector.x, self.y * vector.y, self.z * vector.z
    
    