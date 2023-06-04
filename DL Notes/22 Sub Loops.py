'''
Nested For Loops
Grady Glauser
Digital Literacy
12/10/2021 Notes
Loops in a loop
'''
#bell ringer

# question = ""
# while question != "yes" and question != "no":
#     question = input("Yes or no: ").lower()

#Nest Loop
'''
A loop with in a loop :)
'''
filterz = ["apple","orange"]
userSen = input("Sentence: ").lower().split()

for w in filterz:
    for n in userSen:
        print(w,n)


def listToString():
    s = ""
    l = ""
    for e in l:
        s += e + ""
    return s