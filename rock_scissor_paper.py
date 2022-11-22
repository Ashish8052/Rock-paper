print("RULES AND REGULATION ")
print("ROCK VS PAPER >> PAPER WINS")
print("ROCK VS SCISSOR >> ROCK WINS")
print("PAPER VS SCISSOR >> SCISSOR WINS")

import random
l=["rock","scissor","papaer"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''
        GAME START
        1 YES
        2 NO|EXIT >>>'''))
    if uc==1:
        for a in range(1,6):
            user_input=int(input('''
        1 ROCK
        2 PAPER
        3 SCISSOR >>>'''))
            if user_input==1:
                uchoice="rock"
            elif user_input==2:
                uchoice="scissor"
            elif user_input==3:
                uchoice="paper"
            cchoice=random.choice(l)
            if cchoice==uchoice:
                print("Computer Value >>",cchoice)
                print("User Value >>",uchoice)
                print("Game draw >>")
                ucount=ucount+1
                ccount=ccount+1 
            elif (uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock")or(uchoice=="scissor" and cchoice=="paper"):
                print("Computer Value >>",cchoice)
                print("User Value >>",uchoice)
                print("You win >>")
                ucount=ucount+1
            else:
                print("Computer Value >>",cchoice)
                print("User Value >>",uchoice)
                print("Computer win")
                ccount=ccount+1
                 

    else:
        break


