'''------------------------------
Grady Glauser
10/7/2021 Notes
Loops and range
------------------------------'''
import time

color = input("What color do blue and red make: ")
if color.upper() == "PURPLE":
    print("Correct!")
else:
    print("Rong!")

'''
The following conditions are True:
1. True
2. And free standing value
'''

if "Grady":
    print("True")
else:
    print("False")



#Review
'''
Review: Keeping Score
The following uses variable reassignment
x = 1
x = x + 1
print(x)
'''

score = 0
answer = int(input("1 + 2 = "))
if answer == 3:
    print("Correct!")
    score = score + 1
else:
    print("Rong")
answer = int(input("5 + 2 = "))
if answer == 7:
    print("Correct!")
    score = score + 1
else:
    print("Wrong")
print("Your score is {}/2".format(score))

'''
---For loops---

Loops:
1. Whiel Loops
2. For Loops

In a for loop the condition is counting a condition. use a for loop if you want a block of code to be exacuted a amount of types.

Syntax:
for <varyable> in <colectuion>
    <sub statement>
Varyables in this case are used to represent members of the colection

Use range for a int list
'''

fruits = ["apple", "banana", "orrange"]
for x in fruits:
    print(x)
    #did we reach the end of the list

print("useing range")
for x in range(0,10):
    print(x)


uInput = int(input("input: "))
for n in range(1,uInput + 1):
    print(n * 7)

uInput2 = int(input("input: "))
for n in range(1,uInput2 + 1):
    print(n * "*")