### Operations with nxn matrix and 1 vector###
class cuad_matrix():
    
    def __init__(self, rows, colums):
        self.row = rows
        self.colum = colums
        self.matrix = []
        print(self.matrix)
        
    def crea_matrix(self):
        print("Please introduce the values for the nxn matrix")
        self.row = rows
        self.colums = colums
        self.matrix = []
        
        for r in range (self.row):
            self.matrix.append([])
            for c in range (self.colum):
                number = float(input("Fila {}, Columna {}: ".format (r+1, c+1)))
                self.matrix[r].append(number)
        print("###############################")
        return(self.matrix)
        
        
    
    def add_matrix(self, matrix_a, matrix_b):
        self.matrix_b = matrix_b
        self.matrix_a = matrix_a
        self.total_matrix = []
        
        for r in range(len(self.matrix_a)):
            for c in range(len(self.matrix_a[0])):
                self.matrix_a[r][c] = self.matrix_a[r][c] + self.matrix_b[r][c]
        return(self.matrix_a)
        
    
    
    def sub_matrix(self, matrix_1, matrix_2):
        self.matrix_b = matrix_1
        self.matrix_a = matrix_2
        self.total_matrix = []
        
        for r in range(len(self.matrix_a)):
            for c in range(len(self.matrix_a[0])):
                self.matrix_a[r][c] = self.matrix_a[r][c] - self.matrix_b[r][c]
        return(self.matrix_a)
    
    
    
    def prod_mavec(self, matrix_a, vector):
        self.vector = vector
        self.matrix_a = matrix_a
        self.vec_total = []
        for r in range(len(self.matrix_a)): ## recorro filas
            self.variable = 0
            for c in range(len(self.matrix_a[0])): ## recorro columnas d matriz
                self.matrix_a[r][c] = self.matrix_a[r][c] * self.vector[c] ## mult- col d vector * fila d matriz
                self.variable = self.matrix_a[r][c] + self.variable ## sumo elementos d columnas
            self.vec_total.append(self.variable)
        return(self.vec_total)
        

your_input = int(input("Introduce the number of rows and colums: "))
rows = your_input
colums = your_input ** 2
vector = [1, 2, 3] ## misma cantidad de valores que el n de filas

rc_matrix = cuad_matrix(colums, rows)
matrix_a = rc_matrix.crea_matrix()
###matrix_b = rc_matrix.crea_matrix()  ##crea 2da matriz
###sum_matrix = rc_matrix.add_matrix(matrix_a, matrix_b)  ## suma de matrices
###dif_matrix = rc_matrix.sub_matrix(matrix_a, matrix_b)  ## resta de matrices
###prod_mv = rc_matrix.prod_mavec(matrix_a, vector)  ## producto d un vector * matriz

##print(matrix_a, matrix_b)
##print(sum_matrix)
##print(dif_matrix)
##print(prod_mv)