import datetime

name = input('enter your name\t')
print('good afternoon', name)
date = datetime.datetime.now()




print(f''' dear {name}
      you are selected
       {date} ''')

if "  " in name:
    print('double space detected')
    sec = name.replace("  ", " ")
    name = sec
    print(name)
     


letter = "Dear Harry,\n this python course is nice.\n Thanks!"
print(letter)