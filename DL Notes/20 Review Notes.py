'''
Grady Glauser
Digital Literacy
12/3/2021 Notes
Review Notes
'''

#Bell ringer
numbers = [int(n) for n in input().split()]
numbers.sort()
sum = numbers[0] + numbers[-1]
Idk = sum/2
print(round(Idk))

'''Review
Data Types:
    1. Str
    2. Int
    3. Float
    4. Bool

Grouping Data Types:
    1. List
    2. Dictionary
    3. Set
    4. Tuple

Numbers:
    1. Int - numbers with out decimals
    2. Float - numbers with decimals
    3. Operators:
        +,-, *, /, %

Strings:
    1. Methods:
        a. str.lower()
        b. str.upper()
        c. str.len()
        d. str.title()
        e. Operators:
            + concatonation
            * prints a tring that many times
            str[num] returns number at that index
            < > with strings will sort by letters

Constructs:
    1. Condistionals
    2. Loops
'''