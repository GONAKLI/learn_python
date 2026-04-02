# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.
try:
    with(
    
        open('1.txt') as f1,
        open('2.txt') as f2,
        open('3.txt') as f3
    ):
        pass
except FileNotFoundError:
    print("File does not exist here")
else:
    print('programm successfully executed')
finally:
    print('programm ends here')