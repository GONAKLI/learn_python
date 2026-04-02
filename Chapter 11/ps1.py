# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Dvector:
    @staticmethod
    def ft():
        print('2 d vector')

class d3vector(Dvector):
    @staticmethod
    def ct():
        print('3d vector')

i = d3vector()
i.ct()
i.ft()

