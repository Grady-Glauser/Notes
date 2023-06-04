'''---------------------------
Math & Modulus
9/16/2021 Notes
Grady Glauser
---------------------------'''

#review
cash = 5.96     #float
bank = 250      ##int
#code convention is to help other programers like putting comments near varyables
print(cash + bank) #255.96

'''
+ addition
- subtraction
* multiply
/ divition
() to group
'''
print((5 + 5) * 3)
#use prenths
print(5/2)
#output 2.5
print(4/2)
#output 2.0
age = (int(12/2)) #age is float

money = 6
bonus = 2
overtime = 10
print(money * bonus + 2 * overtime)
#32 as int
print("Hello" * 5)
#output: Hello Hello Hello Hello

# % is modlus

'''
4 = monday
5 = tuesday
6 = wednessday
0 = thursday
1 = fryday
2 = saterday
3 = sunday
'''

userQuery = input("how long")
result = int(userQuery)%7
print("In " + userQuery + " days, it will be " + str(result))