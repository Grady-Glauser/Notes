name = input("Hello I am your computer adventure companyin. Please tell me your name so I know what to call you. : ")
input(name + ' right? Press "Enter"')
adventure = input('Ok now that we are done with that lets begin. Lets start our adventure. We can go to The jungle, or a mountin! If you want Mountan press "1", for Junjle press "2" do this for all the questunes.')

m1, m2, m3, j1, j2, j3 = 0, 0, 0, 0, 0, 0
#1
if adventure == '1':
    print('So you want to go to the mountan?')
    print("Ok now we are here let's get started!")
    m1 = input('Do you want to put up a tent or find a cave?')

if adventure == '2':
    print('So you want to go to the jungle? ')
    print("Ok now we are here let's get started!")
    j1 = input('Do you want to build a shelter or find a cave?')

#2

if m1 == '1':
    print('Ok now we have a base!')
    print("Now lets find water")
    m2 = input('Do you want to find a spring or use the rain?')

if j1 == '1':
    print('Ok now we have a base!')
    print("Now lets find water")
    j2 = input('Do you want to find a spring or a river?')

if m1 == '2':
    print('Ok now we have a base!')
    print("Now lets find water")
    m2 = input('Do you want to find a spring or use the rain?')

if j1 == '2':
    print('Ok now we have a base!')
    print("Now lets find water")
    j2 = input('Do you want to find a spring or a river?')

#3

if m2 == '1':
    print('Ok now we have water')
    print("Now lets explore")
    m3 = input('Do you want to go east or west?')

if j2 == '1':
    print('Ok now we have water')
    print("Now lets explore")
    j3 = input('Do you want to go east or west?')

if m2 == '2':
    print('Ok now we have water')
    print("The rain was toxic you died!!!")

if j2 == '2':
    print('Ok now we have water')
    print("The water was sus you died!!!")


#4




