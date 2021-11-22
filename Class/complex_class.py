class complex_numbers():
    
    def __init__(self, part_r, part_i):
        print("### attach real part and imaginary part ###")
        self.part_r = part_r
        self.part_i = part_i
        print(part_r + part_i)
    
    def __add__(self, number2):
        print("### Complex number--- Sum")
        print(self.part_r + number2.part_r + self.part_i + number2.part_i)
    
    def __sub__(self, number2):
        print("### Complex numbers--- Diference ###")
        print(self.part_r - number2.part_r + self.part_i - number2.part_i)
    
    def __mul__(self, number2):
        print("### Complex number--- Multiplication ###")
        print((self.part_r * number2.part_r) + (self.part_i * number2.part_i) + (self.part_r * number2.part_i) + (self.part_i * number2.part_r))
    
    def __truediv__(self, number2):
        print("### Complex number--- Division ###")
        print((self.part_r * number2.part_r) - (self.part_i * number2.part_i) - (self.part_r * number2.part_i) + (self.part_i * number2.part_r))     
    
number = complex_numbers(1, 5j)
number2 = complex_numbers(2, 3j)

sum_complex = number.__add__(number2)
res_complex = number.__sub__(number2)
mul_complex = number.__mul__(number2)
