'''-----------------------
Grady Glauser
10/12/2021 Notes
Review Strings
-----------------------'''

#Bellringer
base = int(input("Base: "))
hight = int(input("Hight: "))
for h in range(0,hight):
    print("#" * base)

#More loop review

multipules = int(input("What number: "))
index = int(input("How many multipules: "))
for x in range(0,index + 1):
    print(x * multipules)

print("Factorial")
factorial = int(input("Number to multiply: "))
result = 0
for n in range(0,factorial):
    result = (n + 1) * result
print(result)

#str methods review
'''
Methods: str.methodName()
    1. str.format()
    2. str.replace()
    3. str.find()
    4. str.rfind()
    5. str.upper()
    6. str.lower()
    subStr in str

Function:
    1. len(str)
    2. print(str)
'''

greatting = "Hello World"
sentence = "I have {} kinds of {} in my garden."
print(sentence.format(6, "Pumkens"))
print(greatting.replace("World", "People"))
print("HI" in greatting)
print(len(greatting))