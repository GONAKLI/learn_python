'''
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module.
'''

from random import randint

i= 0
computer = randint(1,100)
print(computer)
status = True
guess = 0

def game():
    user = (input('guess number\t'))

    if(user == 'exit'):
        global status
        status = False
        return 'exit from game'
    elif(user.isdigit()):
        user = int(user)
        global guess
        guess +=1
        if(user < computer):
            print('\nHigher number please\n')
        elif(user > computer):
            print('\nLower Number Please\n')
        elif(user == computer):
            print('\nYou won The Game')
            print('Total No. of Guess : ', guess)
            status = False
   


while(status):
    game()