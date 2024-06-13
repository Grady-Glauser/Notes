name = input("please type your name: ")

answer = input ("Is your name " + name + "? Type Yes if it is and No if it is not")

if answer == "Yes":
    age = input ("What is your age?")
    print ("Youur name is " + name + " and your age is " + age + "?")
elif  answer == "No":
    print ("please start the program again and check your in put")