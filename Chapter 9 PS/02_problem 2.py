'''
The game() in a prg lets a user play a game and returns the score as an integer You need to read a file 'hi score.txt'
which is either or conatins the previous high score WAP to update a high score whenever the game() breaks the high score
'''

import random
def game():
    print("You are playing game.....")
    score = random.randint(1,90)
    # featch the highscore
    with open("highscore.txt") as f:
        highscore = f.read()
    if(highscore != ""):
        highscore = int(highscore)
    else:
        highscore = 0   

    print(f"Your score : {score}")
    if(score>highscore):
        # write this highscore in file
        with open("highscore.txt" , "w") as f:
            f.write(str(score))
    return score

game()