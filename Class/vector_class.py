class vector():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.escalar = 0
        print("Vector:")
        print("[",x, y, z,"]")
    
    def adding(self, escalar):
        print("### Addition ###")
        self.escalar = escalar
        print(self.x + self.escalar, self.y + self.escalar, self.z + self.escalar)
    
    def subs(self, escalar):
        print("### Substraction ###")
        print(self.x - self.escalar, self.y - self.escalar, self.z - self.escalar)
        
    def multi(self, escalar):
        print("### Multiply ###")
        print(self.x * self.escalar, self.y * self.escalar, self.z * self.escalar)
        
    def div(self, escalar):
        print("### Division ###")
        print(self.x / self.escalar, self.y / self.escalar, self.z / self.escalar)
    

new_escalar = 10
your_vector = vector(1, 2, 3)

your_vector.adding(new_escalar)
your_vector.subs(new_escalar)
your_vector.multi(new_escalar)
your_vector.div(new_escalar)