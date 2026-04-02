# 8. Write a program to make a copy of a text file “this. txt”
import random

with open('original.txt') as f:
    content = f.read()

with open('duplicate.txt', 'w') as f:
    f.write(content)

print('completed')