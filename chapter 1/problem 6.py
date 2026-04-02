# # Write a program to find the greatest of four numbers entered by the user.
# num1 = int(input("enter first number\t"))
# num2 = int(input("enter second number \t"))
# num3 = int(input("enter third number \t "))
# num4 = int(input("enter forth number \t"))

# if(num1>num2 and num1>num3 and num1>num4):
#     print("is greater", num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("is greater", num2)

# elif(num3>num1 and num3>num2 and num3>num4):
#     print("is greater", num3)

# elif(num4>num1 and num4>num2 and num4>num3):
#     print("is greater", num4)
# else:
#     print("no one is greater than each other")


# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# sub1 = int(input("enter hindi marks \t"))

# sub2 = int(input("enter english marks \t"))
# sub3 = int(input("enter science marks \t"))

# sum = sub1 + sub2 + sub3

# if(sub1/100*100<33 or sub2/100*100<33 or sub3/100*100<33):
#     print('you ar failed')
# else:
#     print("scored above 33% in each subject " )

# if(sum/300*100>=40):
#     print("pass", sum/300*100)
# else:
#     print("scored less tha 40 percent", sum/300*100)


# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# msg = input("enter your message\t\t")
# scam = ["Make a lot of money", "buy now", "subscribe this", "click this"]

# if(scam[0] in msg or scam[1] in msg or scam[2] in msg or scam[3] in msg):
#     print("its a scam message ")
# else:
#     print('you can safely trust it')


# Write a program to find whether a given username contains less than 10
# characters or not.

# username = input("enter your username \t")
# if(len(username)<10):
#     print('too small username')
# else:
#     print('perfect username')


# Write a program which finds out whether a given name is present in a list or not.
# listUser = ['sam', 'peter', 'bruce', 'tony', 'anil']
# userN = input("enter your name \t")
# if(userN in listUser):
#     print('you are already in our record')
# else:
#     print('user does not exist in our record')



# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50
# => F


# studentMark = int(input('enter your marks \t'))

# if(studentMark>90 and studentMark<=100):
#     print("Ex")
# elif(studentMark>80 and studentMark<=90):
#     print("A")
# elif(studentMark>70 and studentMark<=80):
#     print("B")
# elif(studentMark>60 and studentMark<=70):
#     print("C")
# elif(studentMark>=50 and studentMark<=60):
#     print("D")
# elif(studentMark>=0 and studentMark<50):
#     print("F")

# else:
#     print("INVALID MARKS !!!! ")



# Write a program to find out whether a given post is talking about “Harry” or not.

post = input("enter your post \t")
if(post.find("harry") == -1 ):
    print('we are not talking about you')
else:
    print("we are talking about harry")