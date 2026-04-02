# 7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.

class Vector:
    def __init__(self, val):
        self.data = val
    def __len__(self):
        i = len(self.data)
        return i

x = Vector([5,7,9,4])
print(len(x))