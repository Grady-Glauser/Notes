import random
list1 = ["Apples", "Apricots", "Avocados", "Bananas", "Boysenberries", "Blueberries", "Bing Cherry", "Cherries", "Cantaloupe", "Crab apples", "Clementine", "Cucumbers", "Damson plum", "Dinosaur Eggs", "Dates", "Dewberries", "Dragon Fruit", "Elderberry", "Eggfruit", "Evergreen Huckleberry", "Entawak", "Fig", "Farkleberry", "Finger Lime", "Grapefruit", "Grapes", "Gooseberries", "Guava", "Honeydew melon", "Hackberry", "Honeycrisp Apples", "Indian Prune", "Indonesian" "Lime", "Imbe", "Indian Fig", "Jackfruit", "Java Apple", "Jambolan", "Kiwi", "Kaffir Lime", "Kumquat", "Lime", "Longan", "Lychee", "Loquat", "Mango", "Mandarin Orange", "Mulberry", "Melon", "Nectarine", "Navel Orange", "Nashi Pear", "Olive", "Oranges", "Ogeechee Limes", "Oval Kumquat", "Papaya", "Persimmon", "Paw Paw", "Prickly Pear", "Peach", "Pomegranate", "Pineapple", "Passion Fruit", "Quince", "Queen Anne Cherry", "Quararibea cordata", "Rambutan", "Raspberries", "Rose Hips", "Star Fruit", "Strawberries", "Sugar Baby Watermelon", "Tomato", "Tangerine", "Tamarind", "Tart Cherries", "Ugli Fruit", "Uniq Fruit", "Ugni", "Vanilla Bean", "Velvet Pink Banana", "Voavanga", "Watermelon", "Wolfberry", "White Mulberry", "Xigua", "Ximenia caffra fruit", "Xango Mangosteen Fruit Juice", "Yellow Passion Fruit", "Yunnan Hackberry", "Yangmei", "Zig Zag Vine fruit", "Zinfandel Grapes", "Zucchini"]
random.shuffle(list1)
printing = list1[0]
input1 = list1[0].split(" ")
answer = ""
usedletters = ""

if len(input1) > 1:
    for h in input1:
        answer += h
else:
    answer = input1[0]





board = []
for s in range(0,len(answer)):
    board.append("_")

        


def isGuessAllowed(guess):
    if "0" in guess or "1" in guess or "2" in guess:
        print("Invalid Guess, Try Again")
        guess = input("Letter : ")
def adding(guess, usedletters):
    if guess in usedletters:
        print("You already used that letter")

lives = 5
number = 0
length = len(answer) + 6
answer.split()
print("---------------------------------------------------")
print("Lives : " + str(lives))
print("You already used these letters: " + usedletters)
print(board)
guess = input("Letter : ")
isGuessAllowed(guess)
adding(guess, usedletters)


def checkLetter(guess, answer, lives, number, board, length, printing, usedletters):
    answer = answer.lower()
    for q in range(0, length):
        if guess in answer:
            for x in answer:
                number += 1
                if number > len(answer):
                    number = len(answer)
                if x == guess:
                    board[number-1] = guess
            number = 0
        else:
            lives -= 1
        print("---------------------------------------------------")
        print("Lives : " + str(lives))
        usedletters += " " + guess
        print("You already used these letters:" + usedletters)
        print(board)
        if "_" not in board:
            print(printing)
            print("Correct!")
            print("Great Job")
            query = input("Would you like to play again? y/n: ")
            if query == "y":
                list1 = ["Apples", "Apricots", "Avocados", "Bananas", "Boysenberries", "Blueberries", "Bing Cherry", "Cherries", "Cantaloupe", "Crab apples", "Clementine", "Cucumbers", "Damson plum", "Dinosaur Eggs", "Dates", "Dewberries", "Dragon Fruit", "Elderberry", "Eggfruit", "Evergreen Huckleberry", "Entawak", "Fig", "Farkleberry", "Finger Lime", "Grapefruit", "Grapes", "Gooseberries", "Guava", "Honeydew melon", "Hackberry", "Honeycrisp Apples", "Indian Prune", "Indonesian" "Lime", "Imbe", "Indian Fig", "Jackfruit", "Java Apple", "Jambolan", "Kiwi", "Kaffir Lime", "Kumquat", "Lime", "Longan", "Lychee", "Loquat", "Mango", "Mandarin Orange", "Mulberry", "Melon", "Nectarine", "Navel Orange", "Nashi Pear", "Olive", "Oranges", "Ogeechee Limes", "Oval Kumquat", "Papaya", "Persimmon", "Paw Paw", "Prickly Pear", "Peach", "Pomegranate", "Pineapple", "Passion Fruit", "Quince", "Queen Anne Cherry", "Quararibea cordata", "Rambutan", "Raspberries", "Rose Hips", "Star Fruit", "Strawberries", "Sugar Baby Watermelon", "Tomato", "Tangerine", "Tamarind", "Tart Cherries", "Ugli Fruit", "Uniq Fruit", "Ugni", "Vanilla Bean", "Velvet Pink Banana", "Voavanga", "Watermelon", "Wolfberry", "White Mulberry", "Xigua", "Ximenia caffra fruit", "Xango Mangosteen Fruit Juice", "Yellow Passion Fruit", "Yunnan Hackberry", "Yangmei", "Zig Zag Vine fruit", "Zinfandel Grapes", "Zucchini"]
                random.shuffle(list1)
                printing = list1[0]
                input1 = list1[0].split(" ")
                answer = ""
                usedletters = ""
                if len(input1) > 1:
                    for h in input1:
                        answer += h
                else:
                    answer = input1[0]
                    answer = answer.lower()
                board = []
                for s in range(0,len(answer)):
                    board.append("_")
                lives = 5
                number = 0
                length = len(answer) + 6
                answer.split()
                print("---------------------------------------------------")
                print("Lives : " + str(lives))
                print("You already used these letters:" + usedletters)
                print(board)
                guess = input("Letter : ")
                isGuessAllowed(guess)
                adding(guess, usedletters)
                checkLetter(guess, answer, lives, number, board, length, printing, usedletters)
            else:
                break
        if lives == 0:
            print("Game Over")
            print("The word was " + answer)
            break
        else:
            guess = input("Letter : ")
            isGuessAllowed(guess)
            adding(guess, usedletters)

checkLetter(guess, answer, lives, number, board, length, printing, usedletters)