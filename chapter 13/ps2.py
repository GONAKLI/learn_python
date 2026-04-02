# 2. Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input('enter your name \t')
marks = int(input('enter your marks\t'))
mobile = int(input('enter your mobile number\t'))

print('The name of the student is {}, his marks are {} and phone number is {}'.format(name,marks,mobile))