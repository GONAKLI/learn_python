# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Test:
    a = 5

obj = Test()
obj.a = 0
print(obj.a)

# no its create a local object attribute