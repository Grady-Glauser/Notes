'''----------------------
Grady Glauser
Data Types and Casting
6/3/23
----------------------'''

name = "John Doe"
age = 35

#name = int(name) -A string cannot be turned into an int unless it is a just number
age = str(age) #An int can be made into a string and back into an int

age = float(age) #Ints can also be made into floates adding a ".0" ti the end of the number on the other hand if you change a float such as "3.14" into an in it will delete the decimal and become a "3", this can be usefull when trying to remove a decimal


#strings must be inside a pair of " or '
print("Hello")
print('Hello')

a = "Hello"
print(a)

#strings can occupy multiple lines when pairing three sets of quoation marks together

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

#Charicter space in a string can be treated some what like a list because you can do .len() or get a spacific charicter with [1-~], or in an if statement you can use "in" to find a set of charicters in a string
a = "Hello, World!"
print(a[1])


for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")


#you can also print in a range in text
b = "Hello, World!"
print(b[2:5])

#you can also print up to somthing
print(b[:5]) #this does not include "5"


b = "Hello, World!"
print(b[-5:-2]) #when using a negitive position the string starts at the back of the list

'''
#String Modification
.upper() makes all charicters in a string uppercase
.lower() makes all charicters lower case
.strip() removes white space from the beggining and the end of strings, ("   Hello There  ").lower would result in "Hello There"
.replace("H", "J") #Replace just replaces the specified charicter with another difforent specified charicter
.split(",") splits at the specified charicter creating a list
'''

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a = "Hello"
b = "World"
c = a + " " + b #you can combine strings into bigger strings
print(c)


#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


txt = "We are the so-called \"Vikings\" from the north." #You can use a back slash to inset normaly unuseable charicters


'''
I'm not typing this out, but here are all the difforent string methods:
https://www.w3schools.com/python/python_strings_methods.asp
'''

isinstance(txt, str) #isinstance checks if somthing is somthing

#x ** y is like x^y
#x // y rounds down, same as just foing int() and killing the float

g = 1
h = 2

g += 1 #works
h =+ 2 #=+ same as just =

print(g)
print(h)