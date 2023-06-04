'''------------------------------------
Checking strings
Grady Glauser
9/20/2021 Notes
8th Mr. Briano
More string methods
-------------------------------------'''

#BellRinger

notes = "TELEport"
print(notes.upper())
print(notes.lower())
print(notes.replace("TELE","TRANS"))

#---------------------------------------#

'''--------------------------------------

Modulus Review
% is modulus
Like: 5%2 = 1 because 5÷2 the remander is 1

Challange: have user input a 3 diget number then print the middle diget

--------------------------------------'''

numberWith3 = int(input())
numberWith3 = numberWith3 / 10
numberWith3 = int(numberWith3)
numberWith3 = numberWith3 % 10
numberWith3 = int(numberWith3)
print(" ^ This is: " + str(numberWith3))

#3-dig number 100-999
#devide by 100 then u get 0-99 remander
#goal: get middle number

#medod vs function

'''
method:
<Varable>.<method>)()
str.upprt()
str.lower()
str.replace()

Function:
print(<stuff>)
str(<stuff>)
int(<stuff>)
float(<stuff>)
'''

#checking a string
'''
syntax: <sub-str> in <str>
returnsK t/f (bool)
'''
word = "antiseptic"
prefix = "anti"
print("Is anti in antesceptic? ", prefix in word)
print("Is tele in anteseptic? ", "tele" in word)