'''------------------------------
Grady Glauser
9/28/2021 Notes
if and else
------------------------------'''

#Bell Ringer
'''
1. "John"
2. "3.6"
3. "John Doe"
4. "8.8"
'''

pi = 3.14
#Conditional Satments
#EX:
if pi == 3.14:
    print("pi is 3.14")

#synatx:
#if <condition>:
#    exicute

age = 18
if age > 17:
    print("You are an adult!")
    print("You can learn to drive")
    print("You can sign papers")
print("Your age is " + str(age))

'''
If the condition is True the program will run
subordenten statments are indented
'''

#Else
'''
Else is the "other" for an if statement
'''

#syntax
if age == 21:
    print("You are " + str(age))
else:
    print("You are not 21!")

responce = int(input("Give me a number less then 10: "))
if responce < 10:
    print("Correct!")
else:
    print("Incorrect!")

#conditions
'''
> greater than
> less than
<= greater than or equal to
>= less than or equal to

AND/OR are used to check conditions
'''