# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.


f = open("poems.txt")

data = f.read().lower()

if("twinkle" in data):
    print("twinkle is present")
else:
    print("twinkle is not present")

f.close()






