answer = ""
S1 = False
S2 = False

while answer != "q":
    answer = input("Flip a switch (or quit) Type: 1, 2, or q: ") #input

    if answer == "1": #swich 1
        if S1 == False:
            S1 = True
        else:
            S1 = False

    elif answer == "2": #swich 2
        if S2 == False:
            S2 = True
        else:
            S2 = False

    elif answer == "q": #quit
        print("Quitting")

    else: #invalid input
        print(answer + " is an invalid input!")


    if S1 == S2: #output
        print("The light is off")
    else:
        print("The light in on")