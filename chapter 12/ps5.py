# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

user = int(input('enter number\t'))

table = [i*user for i in range(1,11)]

print(table)

with open(f'table {user}', 'w') as f:
    f.write(str(table))