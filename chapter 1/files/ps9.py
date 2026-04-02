
with open('original.txt') as f:
    content = f.read()

with open('duplicate.txt') as f:
    data = f.read()

if(data == content):
    print('files content are same')
else:
    print('files are unique')