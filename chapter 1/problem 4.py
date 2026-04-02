# Write a program to store seven fruits in a list entered by the user.

# list = []

# l1 = input('enter fruit name: ')
# list.append(l1)
# l2 = input('enter fruit name: ')
# list.append(l2)
# l3 = input('enter fruit name: ')
# list.append(l3)
# l4 = input('enter fruit name: ')
# list.append(l4)
# l5 = input('enter fruit name: ')
# list.append(l5)
# l6 = input('enter fruit name: ')
# list.append(l6)
# l7 = input('enter fruit name: ')
# list.append(l7)
# print(list)

# Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks = []
marks.append(int(input('enter marks')))
marks.append(int(input('enter marks')))
marks.append(int(input('enter marks')))
marks.append(int(input('enter marks')))
marks.append(int(input('enter marks')))
marks.append(int(input('enter marks')))
marks.sort()

print(marks)

# Check that a tuple type cannot be changed in python.

value = (7,9,4,3,2,1)
print(type(value))
# value[1] =99

# Write a program to sum a list with 4 numbers.

sum = [10,15,20,25]
total = sum[0] + sum[1] + sum[2] + sum[3]
print('sum of value is ', total)

# Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print('count of 0 is:',a.count(0))