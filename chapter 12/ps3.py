# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.

user = int(input('enter number\t'))
table = [i*user for i in  range(1,11)]
print(table) 