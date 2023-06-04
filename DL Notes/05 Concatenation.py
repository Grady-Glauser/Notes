'''-----------------------------
Python Concatenation
9/14/2021 Notes
Grady's Notes
-----------------------------'''

#Concatenation means combining strings

fName = "John"
lName = "Doe"
print("Name: " + fName + " " + lName)

#add 2+ strings

age = "12"
years = "18"
print(age + years)

greeting = "Hello, how are you doin "
print(greeting + fName)

yName = input("What is your name: ")
print(greeting + yName)

neighbor = input("What is your neighbors name? ")
print(greeting + neighbor)

age = input("How old are you?")

#Although age has been used, we are replacing the value

print("My friend " + neighbor + " is " + str(age) + " years old") 

#input is always a string
#you can not combine str and intun less you use str()

nAge = input("How old is your neighbor? ")
future = int(18) + int(nAge)
print("in 18 years " + str(neighbor) + " will be " + str(future) + " years old")