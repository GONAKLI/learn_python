# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number
    def __mul__(self, other):
        return self.number + other.number

c = Complex(5)
d = Complex(18)

print(c + d)