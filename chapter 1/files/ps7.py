# Write a program to find out the line number where python is present from ques 6.
lineno =1

with open('log.txt') as f:
    content = f.readlines()

for i in content:
    
    if('python' in i):
        print('python is found at ', lineno)
        break
    lineno +=1
else:
    print('python is not found in this')