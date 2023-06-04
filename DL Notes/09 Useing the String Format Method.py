'''---------------------------------------------
Concatonateing numbers
Grady Glauser
9/21/2021 Notes
8th Mr. Briano
Useing the string format method
---------------------------------------------'''

#Bell Ringer
word = input()
print("You like ridding your make to school: ", "I enjoy riding my bike to school." in word)

#str format ----------------------
'''
Three ways to add dumbers to strings
    1. Use commas in the print
    2. Change number to str
    2. Use the str format method
'''
# print("I am " + 3 + " years old.")
print("I am", 3, "years old.")
print("I am " + str(3) + "years old")

'''
The third way uses the str format method
REMEMBER: A method syntax is str.<method name>()
Example: str.upper() / str.lower()
A function is <function name>(data)
'''

intro = "Hello, me name is {} and I am {} old."
years = 12
name =  input("What is your name: ")
print(intro.format(name,years))

hobbies = "My hobbys are {}, {}, and {}."
hobby1 = input("Hobby 1: ")
hobby2 = input("Hobby 2: ")
hobby3 = input("Hobby 3: ")
print(hobbies.format(hobby1, hobby2, hobby3))