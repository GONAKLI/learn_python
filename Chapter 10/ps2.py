# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.
import math

class Calculator:
    def square(self,a):
        return a*a
    def cube(self,a):
        return a**3
    def squareRoot(self,a):
        return math.sqrt(a)
    
number = int(input('enter a number\t'))

obj = Calculator()

print('\n')
print(f'square of {number} is : {obj.square(number)}')
print(f'cube of {number} is : {obj.cube(number)}')
print(f'squareRoot of {number} is : {obj.squareRoot(number)}')