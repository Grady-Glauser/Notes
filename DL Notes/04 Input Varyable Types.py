'''
Grady Glauser
9/13/2021 Notes
Input Varyable types
'''

#contan - combining strings

fName = str(input("First name: "))
lName = str(input("Last name: "))
age = int(input("Age: "))
hight = str(input("Hight: "))
male = str(input("Male y/n: "))

print("Record: ")
print("Name: " + fName + " " + lName)
print("Age: " + age)
print("Hight: " + hight)
print("Male? " + male)


print("You are " + age + " years old")
result = int(age) + 10
print("In 10 years you will be " + str(result))