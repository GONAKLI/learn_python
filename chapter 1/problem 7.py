# # Write a program to print multiplication table of a given number using for loop.

# table = int(input("enter number to print table\t"))

# for i in range(1,11):
#     print(f"{table} * {i} is \t ", table*i)


# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     if(i[0] == 'S'):
#         print('good morning \t', i)


# Attempt problem 1 using while loop.

# table = int(input("enter table number \t"))

# i=1
# while(i<11):
#     print(i*table)
#     i +=1


# Write a program to find whether a given number is prime or not

# num = int(input("enter number\t"))

# i = 2
# while(i<num):
#     if(num%i == 0):
#         print("its not prime")
#         break
        
      
#     if(num%i !=0):
#         print("its a prime number")
#         break
#     i = i+1


# Write a program to find the sum of first n natural numbers using while loop.

# num = int(input("enter number\t"))

# sum =0

# i=0
# while(i<=num):
#     sum += i
#     i +=1
# print('sum is \t', sum)


# Write a program to calculate the factorial of a given number using for loop.

# num = int(input("enter number\t"))
# fact = num

# for i in range(num-1, 0, -1):
   
#     fact = fact * i
# else:
#     print('factorial is \t', fact)



# Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3


# star = '*'

# for i in range(1,6,2):
#     print(star*i)

# n=1

# while(n<=6):
#     print(star*n)
#     n +=2


# Write a program to print the following star pattern:
# *
# **
# *** for n = 3


# star = '*'

# n=1

# while(n<=3):
#     print(star*n)
#     n +=1


# Write a program to print the following star pattern.
# ***
# * * for n = 3
# ***
# star='*'

# for i in range(1,4):
  
#     if(i%2!=0):
#         print(f'{star*3}')
#     else:
#         print(f"{star} {star}")





# Write a program to print multiplication table of n using for loops in reversed
# order.

# table = int(input("enter number\t"))

# for i in range(10,0,-1):
#     print(f"{table} X {i} = {table*i}")