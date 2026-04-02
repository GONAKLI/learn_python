# 5. Repeat program 4 for a list of such words to be censored.

# donkey is a king,
# Sanju is the biggest zero obtainer,
# DONKEY IS sANJU FRIEND,
# Monkey Hates DonkEY very much

# brother is BHAi in english

listed = ['donkey', 'sanju', 'monkey', 'bhai']
updated = ''
def saves():
    # with open('list.txt', 'w') as f:
    #     f.write(str(userList))
    with open('list.txt', 'r') as f:
        data = f.read().lower()
       
    if(data):
        
        for i in listed:
            data=  data.replace(i, '######')
        with open('list.txt', 'w') as f:
            f.write(data)
   
           
        




print( saves() )
