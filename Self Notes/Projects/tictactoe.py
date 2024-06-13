import random

def printBoard():
    print(f"\n     |     |     \n {slotOne} | {slotTwo} | {slotThree} \n_____|_____|_____\n     |     |     \n {slotFour} | {slotFive} | {slotSix} \n_____|_____|_____\n     |     |     \n {slotSeven} | {slotEight} | {slotNine} \n     |     |     \n")

def playerInput():
    playerMove =  input("Waht slot do you want to move to?\n> ")
    if playerMove not in "123456789" or playerMove in usedSpaces:
        print("Invalid input or space is allready occupied")
        playerInput()
    return playerMove

def fillSlot(s):
    global slotOne; global slotTwo; global slotThree; global slotFour; global slotFive; global slotSix; global slotSeven; global slotEight; global slotNine
    if s == "1":
        slotOne = " X "
    elif s == "2":
        slotTwo = " X "
    elif s == "3":
        slotThree = " X "
    elif s == "4":
        slotFour = " X "
    elif s == "5":
        slotFive = " X "
    elif s == "6":
        slotSix = " X "
    elif s == "7":
        slotSeven = " X "
    elif s == "8":
        slotEight = " X "
    else:
        slotNine = " X "
    usedSpaces.append(s)
    
def aiOne():
    global slotOne; global slotTwo; global slotThree; global slotFour; global slotFive; global slotSix; global slotSeven; global slotEight; global slotNine
    global aiMove
    global ranSpace
    aiMove = ""
    ranSpace = 0
    if slotFive == "[5]":
        slotFive = " O "
        usedSpaces.append("5")
    
    #move one
    elif len(usedSpaces) == 1:
        ranSpace = random.randint(1, 4)
        if ranSpace == 1 and slotOne == "[1]":
            slotOne = " O "
            usedSpaces.append("5")
        elif ranSpace == 2 and slotThree == "[3]":
            slotThree = " O "
            usedSpaces.append("5")
        elif ranSpace == 3 and slotSeven == "[7]":
            slotSeven = " O "
            usedSpaces.append("5")
        else:
            slotNine = " O "
            usedSpaces.append("9")

def aiTwo():
    global slotOne; global slotTwo; global slotThree; global slotFour; global slotFive; global slotSix; global slotSeven; global slotEight; global slotNine
    global aiMove
    global ranSpace
    aiMove = ""
    ranSpace = 0
    if slotFive == "[5]":
        slotFive = " O "
        usedSpaces.append("5")
    

    if slotFive == " X ":
        if slotOne == " X ":
            slotNine = " O "
            usedSpaces.append("9")
        elif slotThree == " X ":
            slotSeven = " O "
            usedSpaces.append("7")
        elif slotSeven == " X ":
            slotThree = " O "
            usedSpaces.append("3")
        else:
            slotOne = " O "
            usedSpaces.append("1")




#Varyable Setup

slotOne = "[1]"
slotTwo = "[2]"
slotThree = "[3]"
slotFour = "[4]"
slotFive = "[5]"
slotSix = "[6]"
slotSeven = "[7]"
slotEight = "[8]"
slotNine = "[9]"

playerMove = 0
usedSpaces = []



#Game
printBoard()
fillSlot(playerInput())

aiOne()
printBoard()
fillSlot(playerInput())

aiTwo()
printBoard()