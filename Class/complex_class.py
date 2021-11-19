class complex_numbers():
    
    def __init__(self, part_r, part_i):
        print("### attach real part and imaginary part ###")
        self.part_r = part_r
        self.part_i = part_i
        print(part_r + part_i)
    
    def __add__(self, number2):
        print("### Complex number--- Sum")
        print(self.part_r + number2.part_r, self.part_i + number2.part_i)
    
    def __sub__(self, number):
        print("### Complex numbers--- Diference ###")
        print(self.part_r - number2.part_r, self.part_i - number2.part_i)
    
    def __mul__(self, number):
        print("### Complex number--- Multiplication ###")
        print(self.part_r * number2.part_r, self.part_i * number2.part_i)
    
    def __truediv__(self, number):
        print("### Complex number--- Multiplication ###")
        print(self.part_r / number2.part_r, self.part_i / number2.part_i)    
    
number = complex_numbers(1, 5j)
number2 = complex_numbers(2, 3j)

complex_numbers.add = number + number2
complex_numbers.sub = number - number2
complex_numbers.mul = number * number2
complex_numbers.pow = number / number2