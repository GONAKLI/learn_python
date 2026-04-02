# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

a = int(input('enter a\t'))

b = int(input('enter b\t'))


try:
    a/b
except ZeroDivisionError:
    print('infinite')
else:
    print(a/b)