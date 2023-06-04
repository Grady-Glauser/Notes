'''
Project Notes
Grady Glauser
12/9/2021 Notes
Pseudocode
'''
#Bellringer

import random
score = 1

fruits = ["orange","banana","grapes","papya","mango","lychee","pear","tomato","starfruits","grapefruit","dragonfruit","watermelon","peach","durian","jackfruit","apercots","avicotos","boysenbetties","bluebeary","bingcherry","cherry","cantolope","crab apples","clemintine","cumbers"]

random.shuffle(fruits)
anserKey = [fruits[0],fruits[1],fruits[2],fruits[3],fruits[4]]

for w in anserKey:
    question = list(w)
    random.shuffle(question)
    print(question)
    guess = input("Answer: ")
    if guess == w:
        print("Correct!")
        score += 1


print(str(score) + "/5")