'''-------------------------
More String methods
9/23/2021 Notes
Grady Glauser
-------------------------'''

#Bell Ringer ---------------------------------#
number = input("Number: ")
noun = input("Noun: ")
print("I  own {0} {1}s.".format(number, noun))
#---------------------------------------------#

'''
So far...
    1. STR.upper
    2. STR.lower
    3. STR.format(info)
    4. STR.replace(old, new)

New Method
    5. STR.strip()
        >removes spaces
    6. STR[INT]
        >Charter index for str
    7. STR[START:END]
        > STR slicing
    8. len(STR) > function
        > Tells amount of stuff in str
    9. STR.split(where)
        > Splits strings in cirten places
    10. STR.find(What)
        > Finds a charicter
    11.STR.rfind(What)
        > starts from the back to find charicter
'''

#strip example

userInput = "     Hello        "
print(userInput)
print(userInput.strip())

#index
sentence = "I like crashing my bike."
print(sentence[1]) #Each char has a pos
#the 3rd is i
print(sentence[-1])
#Nagitive numbers are backwards

#slicing
#for the index, print START:END for a section
print(sentence[2:5])
#end is exclusive. i.e. form 2 up to 5
#2 <= string < 5

#Length
print(len(sentence)) #22 char
#print(sentence[100]) #errrrrr

#back slice
print(sentence[22::-1])
print(sentence[len(sentence)::-1])
#sdrawkcab stnirp

#find
print(sentence.find("k"))
print(sentence.rfind("k"))
#I like to ride my dog
# r finds last (duh)

#Split
print(sentence.split()) #defalt split is a space