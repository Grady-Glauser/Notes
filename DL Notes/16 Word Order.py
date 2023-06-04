'''---------------------------------
Grady Glauser
10/5/2021 Notes
Review
---------------------------------'''

#Bell Ringer

age = input("Age: ")
if int(age) <= 6:
    print("$3")
elif int(age) >= 50:
    print("$5")
elif int(age) >= 7:
    print("$8")

#Conditions
'''
Example: ==, >, <, >=, <=,

AND OR
Example: If a person is wearing a helmit and pads are they are safe

If john is wearing a helm and pads he is safe?
    No john is not safe.

In logic if a condition is true of false:
There are compound conditions / or 
A conditions is true if bouth are true.
'''

age  = int(input("Age: "))
food = int(input("Food: "))

#You can enter my house if you have food, and are older than 18 years old.

if age > 18 and food > 0:
    print("Welcome to my house")
elif age > 18 or food > 0:
    print("You must be old or you need more food")
else:
    print("You are too young and have no food")



if "cat" < "dog":
    print("Dogs are the best") #the computer knows dogs are the best! (and it is in dictionary order)

if "cat" == "cat":
    print("True")