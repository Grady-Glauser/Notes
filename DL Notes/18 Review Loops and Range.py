'''---------------------------
Grady Glauser
10/11/2021 Notes
Review Loops and Range
---------------------------'''

#Bell Ringer
starNumber = int(input("Star size: "))
for x in range(0,starNumber):
    print("#" * starNumber)


starNumber = int(input("Star size: "))
starSimble = input("Star simble: ")
for x in range(0,starNumber):
    print(starSimble * starNumber)


starNumber = int(input("Star size: "))
print("*" * starNumber)
inLen = starNumber - 2
for x in range(0,inLen):
    print("*" + (" " * inLen) + "*")
print("*" * starNumber)



starSimble = input("Simble: ")
starNumber = int(input("Star size: "))

print("*" * starNumber)
inLen = starNumber - 2
for x in range(0,inLen):
    print("*" + (starSimble * inLen) + "*")
print("*" * starNumber)

'''
Review for loops with lists
for <Varyable> in <list>:
    <statements>
'''

names = ["ALax", "Bob", "Cathy"]
for n in names:
    print("Hello" + n)


words = input("Three things: ").split
for w in words:
    print(w)