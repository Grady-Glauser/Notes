'''------------------------------------
Grady Glauser
Basics Review & Data Types
6/2/2023
-------------------------------------'''

myNumber = int(input("What is your number: "))
if myNumber == 1:
    exit() #"Exit" exits or just stops code
else:
    print("Not 1?!")

'''
< > greater and less than
<= >= greater thant/lest than or equil to
'''

print("Hello, World") #print outputs anything

myVar = "This is my varyable (it is also a string)"

if myVar is str():
    print("if statementsa must also be indented")


carname = "Volvo" #This varyable is a string
x = 50 #This is an int (a number with no desimal)

print(x + 10) #you can do math in if statements with opperaters

z = x + 10 #varyables can also store the result of nubers

'''
varyables cannot begin with a number
they cannot have spaces or dashes


Cases:

there are difforents ways to formeat varyable names called cases

snake case: when words are septerated by nubers
eg. vareable_one

Pascale case: when word are seperated by caps
eg. VaryableOne

Camel Case: when words are seperated by capitols exept for the intial word
eg. varOne
'''

#you can assign multiple things like this
a = b = c = 1
d, e, f = 1, 2, 3

def myFun():
    global x #makes somthing beleg ousside of functions


'''

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType

'''

x = 5j
print(x + x) #complex is like algibra also it uses "j"

myTupple = ("hi", "there") #tupples are locked

print(range(6)) #tess youe the amount of charicter in a string or the amount in an int

f = 34.2 #floata are like inst, but with no decimal

x = {"name" : "John", "age" : 36}

#display x:
print(x["name"], x["age"])

#display the data type of x:
print(type(x)) 


noneType = None

myBool = True #bools are ether t/f

x = bool(5 == 1)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = bytes(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = memoryview(bytes(45))

#display x:
print(x)

#display the data type of x:
print(type(x)) 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10)) #prints random number in rance btween 1 and 10
myRandomInt = random.randrange(1, 100) #This is a random varyable