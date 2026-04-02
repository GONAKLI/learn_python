# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.

numb = [1,2,3,4,5,6,7,8,9]

for index,item in enumerate(numb):
    # print(index, item)
    # print(type(index), type(item))
    
    if(index+1 != 3 and index+1 != 5 and index+1 != 7 ):
        continue
    else:
        print(item)