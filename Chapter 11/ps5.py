# 5. Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, val):
        self.vect = val
    def __add__(self, other):
        i=0
        new =[]
        while(i<len(self.vect)):
            new.append(self.vect[i] + other.vect[i])
            i +=1
        
        print(new)
    def __mul__(self, other):
        i=0
        new = []
        res = 0
        while(i<len(self.vect)):
            new.append(self.vect[i] * other.vect[i])
            res = res + new[i]
            i +=1
        
        print(res)

x = Vector([1,2,3])
y = Vector([4,5,6])

x +y
x * y