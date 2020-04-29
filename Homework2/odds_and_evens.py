"""
Odds and Evens game simulator
"""

#import random module
import random

print("Let's play odds and evens")
passChoice = False

#user choice (odds or evens)
while not passChoice:
    playerChoice = input("Do you want to be (odds) or (evens)? ")
    if playerChoice == "odds" or playerChoice == "evens":
        passChoice = True

#user round choice
winFinish = int(input("What do you want to play up to? "))

#number of wins make sense
if winFinish > 0:
    print("Alrighty, " + str(winFinish) + " will win the game.")
else:
    print("NO ONE WINS. GAME OVER!")

#intializing variables
roundCounter = 1
winCounter = 0
playerWins = 0
computerWins = 0

#main game inside while loop
while winCounter < winFinish + 1:

    #round header
    print("")
    print("====")
    print("Round " + str(roundCounter))
    print("====")
    print("Number of wins")
    print("Player: " + str(playerWins) + ", Computer: " + str(computerWins))

    #game playout
    fingersPlayed = int(input("How many fingers will you play? "))
    print("")
    if fingersPlayed == 1 or fingersPlayed == 2:
        compFingers = random.randint(1, 2)
        print("Player played " + str(fingersPlayed))
        print("Computer played " + str(compFingers))
        totalFingers = fingersPlayed + compFingers

        #add up to 1 fingers
        if totalFingers == 1:
            print("Total is 1 (odds)")
            if playerChoice == "odds":
                print("Player scores 1 win!")
                playerWins += 1
            elif playerChoice == "evens":
                print("Computer scores 1 win!")
                computerWins += 1
            roundCounter += 1
            winCounter += 1

        #add up to 2 fingers
        elif totalFingers == 2:
            print("Total is 2 (evens)")
            if playerChoice == "evens":
                print("Player scores 1 win!")
                playerWins += 1
            elif playerChoice == "odds":
                print("Computer scores 1 win!")
                computerWins += 1
            roundCounter += 1
            winCounter += 1

        #add up to 3 fingerrs
        elif totalFingers == 3:
            print("Total is 3 (odds)")
            if playerChoice == "odds":
                print("Player scores 1 win!")
                playerWins += 1
            elif playerChoice == "evens":
                print("Computer scores 1 win!")
                computerWins += 1
            roundCounter += 1
            winCounter += 1

        #add up to 4 fingers
        elif totalFingers == 4:
            print("Total is 4 (evens)")
            if playerChoice == "evens":
                print("Player scores 1 win!")
                playerWins += 1
            elif playerChoice == "odds":
                print("Computer scores 1 win!")
                computerWins += 1
            roundCounter += 1
            winCounter += 1

    #skip to next round if input unreadable
    else:
        roundCounter += 1
        winCounter += 1

#player win declaration
if playerWins > computerWins:
    print("")
    print("Player wins the game!")

#computer win declaration
elif computerWins > playerWins:
    print("")
    print("Computer wins the game!")