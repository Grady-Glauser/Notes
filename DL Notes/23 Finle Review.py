'''
Grady
Digital Literacy
12/13/2021 Notes
Review
'''

vouals = ["a","e","i","o","u","y"]
word = list(input("Word: "))
letters = []
for x in word:
    if x in vouals:
        letters.extend("*")
    else:
        letters.extend(x)

print(letters)