# Write a program using functions to find greatest of three numbers.

# def finder(x,y,z):
#     if(x>y and x>z):
#         return x
#     elif(y>x and y>z):
#         return y
#     elif(z>x and z>y):
#         return z
#     else:
#         return 'no one is greater'

# num = []

# for i in range(3):
#     num.append(int(input(f"enter number:  {i+1} \t")))

# print(f'the greatest number is: {finder(num[0],num[1],num[2])}')



# Write a python program using function to convert Celsius to Fahrenheit.


# def converter(val):
#     print("celsius to fahrenite converter")
#     return (9/5*val)+32


# celsius = int(input("enter celsius Degree value\t"))
# print(converter(celsius), 'F')


# How do you prevent a python print() function to print a new line at the end.

# print('i am', end="")
# print(' a', end="")
# print(' coder', end="")



# Write a recursive function to calculate the sum of first n natural numbers.

# def sum(n):
#     if(n==0):
#         return 0
#     return n + sum(n-1)

# n = int(input("enter a number\t"))
# print(sum(n))



# Write a python function to print first n lines of the following pattern:
# ***
# **
# - for n = 3
# *



# def pattern(n):
#     if(n == 1):
#        return print('*')

#     print(f"{'*' * n}")
#     pattern(n-1)

# n = int(input("enter pattern number \t"))

# pattern(n)


# Write a python function which converts inches to cms.

# def cms(x):
#     print("inches to cm converter")
#     return x * 2.54

# unit = int(input("enter inches\t"))

# print("result is : \t", cms(unit))


# Write a python function to remove a given word from a list ad strip it at the same
# time

# l = ['apple', 'banana', 'mango', 'strawberry', 'lemon']

# print(l)
# inp = input ('enter the word to remove\t').strip()
# l.remove(inp)
# print('list after\t', l)



# Write a python function to print multiplication table of a given number.
# i=1
# def table(n):
#     global i
    
#     if(i==11):
#         return 'completed'
#     print(n * i )
#     i +=1
#     table(n)


# n = int(input("enter table\t"))

# table(n)
