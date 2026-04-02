# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

def table(val):
    with open("tables/Table of " + str(val), "w") as f:
      
            i=1
            while(i<=10):
                f.write(f'{val} X {i} = {val*i} \n')
               

                i +=1


i=2
while(i<=20):
     table(i)
     i +=1