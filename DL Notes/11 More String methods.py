'''-------------------------------
Grady Glauser
9/24/2021 Notes
More str methods
-------------------------------'''

sentence = "The fall festival is today!"
print(sentence.upper()) #upper -THE FALL FESTIVAL IS TODAY! - str
print(len(sentence)) #len - 27 - int
print(sentence[0]) #T - str
print(sentence[4:8]) #slice - fall - str

#letter = sentence[len(sentence)] #str
print(len(sentence) + 5)
print("I like " + sentence[4:8])

sentence2 = input("go")
print(sentence2[len(sentence2)::-1])