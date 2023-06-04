'''
HM Review
Grady Glauser
Game Loops
'''

#imports
import random

#Functions
def tenChecker(n):
    if n > 10:
        print(str(n) + " is greater than 10!")
    elif n < 10:
        print(str(n) + "is less than 10")
    else:
        print(str(n) + " is 10!")
def checkInput(L):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    g = input("Guess a letter: ")
    while (g not in alphabet) and (g not in L):
        g = input("Guess a valid letter: ")

    return g
def printBoard(B):
    bd = ""
    for x in B:
        bd += x
    print(bd)
def addLetters(A, B, g):
    index = 0
    for letter in A:
        if g == letter:
            B[index] = letter
        index += 1
    return B
def updateAttempts(a, g):
    if g not in A:
        at -= 1
    return at



animals = ["Lion","Tigger","Horse"]
random.shuffle(animals)
answer = (animals[0])
guess = ""
usedLetters = []
board = list(" _ " * len(answer))
print(board)
attemps = 6

while attemps > 0:
    printBoard(board)
    guess = checkInput(usedLetters)
    attemps = updateAttempts(attemps,answer,guess)
    usedLetters.append(guess)
    board = addLetters(answer,board,guess)