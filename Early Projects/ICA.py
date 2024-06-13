import random

n = random.randint(1,10)

guess = input("Enter a random number: ")

if guess == n:
    print("Good job! You got it!")
else:
    print("Pleas try again")
