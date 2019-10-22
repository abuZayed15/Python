"""
@author = Abu Zayed
@name = Rock, Paper, Scissor
"""

from random import randint
hum_score = 0
com_score = 0
select = ""
com_select = ""
print("...rock...")
print("...paper...")
print("...scissors...")

#0 rock
#1 paper
#2 scissor

#start of loop
while select != "n" :

    #generate random number; assign number to R,P,S
    com_number = randint(0,2)
    if com_number == 0 :
        com_select = "rock"
    elif com_number == 1 :
        com_select = "paper"
    else :
        com_select = "scissor"


    #prompt for user input
    select = input("(Enter your choice): ").lower()
    if select == "rock" and com_number == 2 : # rock x scissor        
        hum_score += 1
        print(f"The computer plays: {com_select}")
        print(f"Player Score: {hum_score} Computer Score: {com_score}")
        
    elif select == "paper" and com_number == 0 : # paper x rock
        hum_score += 1
        print(f"The computer plays: {com_select}")
        print(f"Player Score: {hum_score} Computer Score: {com_score}")
    elif select == "scissor" and com_number == 1 : # scissor x paper
        hum_score += 1
        print(f"The computer plays: {com_select}")
        print(f"Player Score: {hum_score} Computer Score: {com_score}")
    elif select == "rock" and com_number == 0 or select == "paper" and com_number == 1 or select == "scissor" and com_number == 2 :
        print(f"The computer plays: {com_select}")
        print("It's a tie!")
        print(f"Player Score: {hum_score} Computer Score: {com_score}")
    else:
        com_score += 1
        print(f"The computer plays: {com_select}")
        print(f"Player Score: {hum_score} Computer Score: {com_score}")
    
    
    
    #repeat or end game
    
    if select == "quit" or select == "q" :
        break

    if hum_score == 3 :
        print("Player win!")
        print("CONGRATS, YOU WON!")
        select = input("Would you like to play again? (y/q) : ").lower()
        if select == "quit" or select == "q" :
            select = "n"
        hum_score = 0
        com_score = 0
    elif com_score == 3 :
        print("OH NO :-( THE COMPUTER WON...")
        select = input("Would you like to play again? (y/q) : ").lower()
        if select == "quit" or select == "q" :
            select = "n"
        hum_score = 0
        com_score = 0
    elif select == "quit" or select == "q" :
        break

    print("---------------------------------")


#exit message
print("Game has ended...")
