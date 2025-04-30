class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __repr__(self):
        return f"{self.real} {('+' if self.imaginary >= 0 else '-')} {abs(self.imaginary)}i"
    
    def __add__(self, num):
        return Complex(self.real+num.real, self.imaginary+num.imaginary)
    
    def __sub__(self, num):
        return Complex(self.real-num.real, self.imaginary-num.imaginary)
    
    def __mul__(self, num):
        return Complex(self.real*num.real, self.imaginary*num.imaginary)
    
    def __truediv__(self, num):
        return Complex(self.real/num.real, self.imaginary/num.imaginary)
    
    def __iadd__(self, num):
        self.real += num.real
        self.imaginary += num.imaginary
        return self

    def __isub__(self, num):
        self.real -= num.real
        self.imaginary -= num.imaginary
        return self
    
    def __imul__(self, num):
        self.real *= num.real
        self.imaginary *= num.imaginary
        return self
    
    def __itruediv__(self, num):
        self.real /= num.real
        self.imaginary /= num.imaginary
        return self
    
    def __gt__(self,num):
        if self.real>num.real:
            return True
        elif self.real==num.real and self.imaginary>num.imaginary:
            return True
        else: 
            return False  
        
    def __lt__(self,num):
        if self.real<num.real:
            return True
        elif self.real==num.real and self.imaginary<num.imaginary:
            return True
        else: 
            return False
        
    def __eq__(self,num):
        if self.real==num.real and self.imaginary==num.imaginary:
            return True
        else:
            return False
    
    def __ne__(self,num):
        if self.real==num.real and self.imaginary==num.imaginary:
            return False
        else:
            return True
    
    def __ge__(self,num):
        if self.real>=num.real:
            return True
        elif self.real==num.real and self.imaginary>=num.imaginary:
            return True
        else: 
            return False
        
    def __le__(self,num):
        if self.real<=num.real:
            return True
        elif self.real==num.real and self.imaginary<=num.imaginary:
            return True
        else: 
            return False
    
num1 = Complex(10,6)
num2 = Complex(2,3)
print("Num1:",num1)
print("Num2:",num2)

print("Add:",(num1+num2))
print("Sub:",(num1-num2))
print("Mul:",(num1*num2))
print("Div:",(num1/num2))

num1 += num2
print("Add and assign:",num1)
num1 -= num2
print("Sub and assign:",num1)
num1 *= num2
print("Mul and assign:",num1)
num1 /= num2
print("Div and assign:",num1)

print("num1 > num2:",num1 > num2)
print("num1 < num2:",num1 < num2)
print("num1 == num2:",num1 == num2)
print("num1 != num2:",num1 != num2)
print("num1 >= num2:",num1 >= num2)
print("num1 <= num2:",num1 <= num2)
