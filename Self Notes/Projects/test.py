import random

def ai():
    global slotOne, slotTwo, slotThree, slotFour, slotFive, slotSix, slotSeven, slotEight, slotNine
    
    aiMove = ""
    ranSpace = 0
    
    if slotFive == "5":
        aiMove = "5"
    elif len(usedSpaces) == 1:
        ranSpace = random.randint(1, 4)
        if ranSpace == 1 and slotOne == "1":
            slotOne = "O"
        elif ranSpace == 2 and slotThree == "3":
            slotThree = "O"
        elif ranSpace == 3 and slotSeven == "7":
            slotSeven = "O"
        else:
            slotNine = "O"

# Assuming the variables usedSpaces, slotOne, slotThree, slotSeven, and slotNine are defined elsewhere in your code.

# Sample usage
usedSpaces = ["1"]
slotFive = "X"
slotOne, slotThree, slotSeven, slotNine = "1", "3", "7", "9"
ai()
print(slotOne, slotThree, slotSeven, slotNine, slotFive)  # Check the updated values after calling ai()
