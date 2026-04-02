# 6. Write __str__() method to print the vector as follows:
# 7i + 8j +10k
# Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self, vect):
        self.data = vect
    def __str__(self):

        i = len(self.data)
        j = 0
        ch = 105
        res =''
        while(i>0):
            res = res + str(self.data[j]) + chr(ch)
            if(i > 1):
                res = res + ' + '
            ch +=1
            i -=1
            j +=1
        return res      
    
x = Vector([5,8,9,11,6,2])
print(x)