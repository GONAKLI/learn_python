import random

option = ['snake', 'water', 'gun']



def result():

    random.shuffle(option)

    print(option)
    userChoice = input("enter your choice \t").lower()
    machinChoice = random.choice(option)

    if(userChoice == 'exit'):
        return

    if(userChoice == 'snake' and machinChoice == 'water'):
        print(f'User Choose {userChoice} and \n Computer choose {machinChoice} ')
        print('hence Winner is User \n\n')
    elif(userChoice == 'water' and machinChoice == 'gun'):
        print(f'User Choose {userChoice} and \n Computer choose {machinChoice} ')
        print('hence Winner is User \n\n')
    elif(userChoice == 'gun' and machinChoice == 'snake'):
        print(f'User Choose {userChoice} and \n Computer choose {machinChoice} ')
        print('hence Winner is User \n\n')

    elif(userChoice == 'water' and machinChoice == 'snake'):
        print(f'User Choose {userChoice} and \n Computer choose {machinChoice} ')
        print('hence Winner is Computer \n\n')
    elif(userChoice == 'snake' and machinChoice == 'gun'):
        print(f'User Choose {userChoice} and \n Computer choose {machinChoice} ')
        print('hence Winner is Computer \n\n')
    elif(userChoice == 'gun' and machinChoice == 'water'):
        print(f'User Choose {userChoice} and \n Computer choose {machinChoice} ')
        print('hence Winner is Computer \n\n')
    else:
         print(f'User Choose {userChoice} and \n Computer choose {machinChoice} ')
         print('Match Draws')
    
    

while(True):
    result()

print('game ended')
