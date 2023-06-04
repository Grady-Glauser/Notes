'''--------------------------------------------
C: Review
Grady Glauser
10/1/2021 Notes
if statements
--------------------------------------------'''

'''
1. Store things with a varyable
2. Know your data types
3. Know your operations
'''

#Numbers
'''
1. Numbers without a desimal are ints
    3, -5, 15
    age, score
2. Numbers with a desimal are floats
    pi, hight, weight
    +,-,/,*
'''

#Strings
'''
1. Use quotes to make a string
    string = "string", name = "grady"
    name, greeting
'''

example = "hi"
name = "Grady" #str
age = 12 #int
money = 5.99 #floar
grades = [7, 8, 9, 10, 11, 12] #list
smart = True #bool

#Lists
'''
Hold any kind of data type
Use plural varyable names for a list
'''

#Function and Methods

#Function
    #print(example) #prints in the terminal
    #len(example) #gives len on charictors in a varyable
#Method  
'''
    .upper
    .lower
    .replace
    .find
    .rfind
    .format
'''

#Challange:
'''
Write a program that accepts one user input, thenumber of cents.
the program prints the amount into
'''



money = int(input())

quarters = int((money / 25))
remaining = money % 25

dimes = int((remaining / 10))
remaining = remaining % 10

nickles = int((remaining / 5))
remaining = remaining % 5

penneys = int((remaining / 1))

print(str(quarters) + ", " + str(dimes) + ", " + str(nickles) + ", " + str(penneys))