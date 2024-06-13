'''-----------------------
Grady Glauser
Python Refrsher Notes Using Tourtorial - https://www.youtube.com/watch?v=rfscVS0vtbw&list=WL&index=2
5/11/24 - 5/12/24
-----------------------'''

from math import *

print("Hello World")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

characterName = "John"
characterAge = 35
numberExample = 76.3
print(int(numberExample))
boolExample = True

print(f"There once was a man named {characterName} and he was {characterAge} years old.")
print("There once was a man named " + str(characterName) + " and he was " + str(characterAge) + " years old.")
print("There once was a man named", characterName, "and he was", characterAge, "years old.")


print("Line \"one\"\nLine \"two\"")

print(characterName.isupper())
print(characterName.upper())
print(characterName.upper().isupper())
print(len(characterName))

name = "Christian"
print(name[0])
print(name.index("i"))

insult = "You nerd!"
print(insult.replace("nerd", "n**d"))

print(round(numberExample))
print(sqrt(numberExample))

'''
num1 = input("First number: ")
num2 = input("Second number: ")
result = float(num1) + float(num2)
print(result)

color = input("Enter a color: ")
pluralNoun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print(f"Roses are {color}\n{pluralNoun} are blue\nI love {celebrity}")
'''

friends = ["Christian", "Grady", "Jack"]
print(friends[-2])
favNumbers = [1024,1,2,2,4,8,16,32,64,128,256]
favNumbers.append(512)
favNumbers.pop()
favNumbers.count(2)
favNumbers.reverse()
favNumbers.sort()

cords = (128, 64)
print(cords[0])

def greet(a):
    print(f"Hello {a}!")
greet("\"name\"")

def cube(num):
    return num*num*num

print(cube(5))

isTall = True
if isTall:
    print("You are tall")
else:
    print("You are not tall")


monthConv = {
    "Jan": "January",
    "Feb": "Febuwary",
    "Mar": "March",
    "Apr": "April",
    "May": "May"
}

def convMonth(m):
    #return monthConv[m]
    return monthConv.get(m, "No valid month")


print(convMonth("Mar"))

i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
for i in range(10):
    print(i)

for n in favNumbers:
    print(n)


#Guessing Game
'''
sWord = "word"
guess = ""
guesCount = 15
while sWord != guess and guesCount >= 1:
    guess = input(f"Guess the word, you have {guesCount} guesses remaing: ")
    guesCount -= 1
if guess == sWord:
    print(f"You win with {guesCount} guesses remaining!")
else:
    print("You are out of guesses and have lost.")
'''

print(2**3)

numberGrid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(numberGrid[1][1])

for row in numberGrid:
    for col in row:
        print(col)

def tranlate(p):
    tranlation = ""
    for l in p:
        if l in "AEIOUaeiou":
            if l.isupper():
                tranlation = tranlation + "G"
            else:
                tranlation = tranlation + "g"
        else:
            tranlation = tranlation + l
    return tranlation
    
print(tranlate(input("Enter a phrase: ")))

try:
    numberExample = int(input("Enter a number: "))
    print(numberExample)
except ValueError as e:
    print(e)