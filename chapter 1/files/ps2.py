

# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score....

def game(score):
    with open('hi-score.txt', 'r') as f:
        data = f.read()
        if(data):
            data = int(data)
            if(data < int(score)):
                with open('hi-score.txt', 'w') as f:
                    f.write(str(score))
                    return score
            else:
                with open('hi-score.txt', 'r') as f:
                    data = f.read()
                    data = int(data)
                    return data
        else:
             with open('hi-score.txt', 'w') as f:
                    f.write(str(score))
                    return score



i=True
while(i == True):
    user = (input("enter score\t"))
    if(user == 'exit'):
        i=False
    elif(user.isdigit()):
        print(game(user))
    else:
        print('something Went wrong !!!')



    

