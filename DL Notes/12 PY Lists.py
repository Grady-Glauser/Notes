'''-------------------------------
Grady Glauser
9/27/2021 Notes
PY Lists
-------------------------------'''

#Review
'''
Data types
    1. str = "Hi"
    2. int = 9
    3. float = 3.14
    4. bool = True
    5. List = ["John", "Mark", "Doe"]
'''

# Lists
'''
Use [] to make a list
Ex: fruits = [] Empity List
Ex: fruits = ["apple", "orrange", "banana"]
Each peice of data has a comma
Each peice is called and element
Each element is in order, starting with "0"
'''
fruits = ["apple", "orrange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[1].upper())
phoneNumber = ["8019317616", "8015185177" "(brothers number)"]
print(fruits[1][0])
print(phoneNumber)

'''
Colections
    String, List, Tuple, Dictionary, Sets
    List has an order
    Tuple has an order but can not be changed
    Set has no order which means no index
    Dictionary has named-indexes (called keys)

Split Method
    The split method we learded returns a list
'''

sentence = "I like to crash my bike."
words = sentence.split()
print(words[0])
print(words[-1])
print(len(words))

number = 123
#print(len.(number)) #type err