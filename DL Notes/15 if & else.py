'''---------------------------------
Notes
Grady Glauser
10/4/2021 Notes
else / if
---------------------------------'''

#write 3 conditions
if 7 > 3:
    print("7 is more that 3")
if 3 == 3:
    print("3 is 3")
if 4 != 3 +1:
    print("No 3 + 1 = 4")
else:
    print("Yes 3 + 1 = 4")

#condition structures
'''
Evrything you need:
    1. Syntax: if <blank> = <blank>:
    2. Condition
    3. Subordinate statement (indented code)

Condition is true/false
A subordinate statement is indented code
indentation helps the computer group code
this is also known as a block
'''

print("---Notes---")

#if
grade = int(input("What grade are you in: "))
if grade == 8:
    print("You are in middle school!")
print("Thank You!")

#if else
if grade == 9:
    print("You are a freshmen")
else:
    print("You are not a freshmen")
'''
In a if else statement the computer will exicute the if statement noarmaly, 
but if it is false then it skips to the else and runs it.
'''

#else-if
print("---Age Check---")
age = int(input("How old are you: "))
if age == 0:
    print("You are an unborn")
elif age <= 12:
    print("You are an child")
elif 12 < age < 20:
    print("You are a teenager")
else:
    print("You are an adult")