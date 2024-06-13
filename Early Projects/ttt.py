'''-----------------------------------
Tick Tack Toe
by Grady
-----------------------------------'''
import time
import random

playerInput = 1
#functions
def startScreen():
    input("Systom Started")
    print()
    print("#---------------------------#")
    print("  Welcome to tick-tack-toe!  ")
    print('  Press "Enter" to continue  ')
    print("#---------------------------#")
    input()

def printBoard():
    print("      |     |      ")
    print("   " + box1 + "  |  " + box2 + "  |  " + box3 + "   ")
    print(" _____|_____|_____ ")
    print("      |     |      ")
    print("   " + box4 + "  |  " + box5 + "  |  " + box6 + "   ")
    print(" _____|_____|_____ ")
    print("      |     |      ")
    print("   " + box7 + "  |  " + box8 + "  |  " + box9 + "   ")
    print("      |     |      ")
    print()

def printBoardInstructions():
    print(playerTurn + " pick you board slot (1-9): ")
    playerInput = int(input("> "))
    playerInput = int(playerInput)
    print()

def updateBoard():
    if playerTurn == "Player 1":
        if playerInput in validNumbers and playerInput not in usedBoxes:
            if playerInput == 1:
                box1 = "O"
            elif playerInput == 2:
                box2 = "O"
            elif playerInput == 3:
                box3 = "O"
            elif playerInput == 4:
                box4 = "O"
            elif playerInput == 5:
                box5 = "O"
            elif playerInput == 6:
                box6 = "O"
            elif playerInput == 7:
                box7 = "O"
            elif playerInput == 8:
                box8 = "O"
            else:
                box9 = "O"
        else:
            print("Invalid input please try again")
            printBoardInstructions()

    else:
        if playerInput in validNumbers and playerInput not in usedBoxes:
            if playerInput == 1:
                box1 = "O"
            elif playerInput == 2:
                box2 = "O"
            elif playerInput == 3:
                box3 = "O"
            elif playerInput == 4:
                box4 = "O"
            elif playerInput == 5:
                box5 = "O"
            elif playerInput == 6:
                box6 = "O"
            elif playerInput == 7:
                box7 = "O"
            elif playerInput == 8:
                box8 = "O"
            else:
                box9 = "O"
        else:
            print("Invalid input please try again")
            printBoardInstructions()



#varyables
playerTurn = "Player 1"

usedBoxes = []
validNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#board-varyables
box1 = "1"
box2 = "2"
box3 = "3"
box4 = "4"
box5 = "5"
box6 = "6"
box7 = "7"
box8 = "8"
box9 = "9"


#Game
startScreen()
printBoard()
printBoardInstructions()
updateBoard()
printBoard()

