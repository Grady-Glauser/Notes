#Leap Year Hint
'''
if year is divisible by 4:
    if year ends in 00 (divisible by 100):
        if year is divisible by 400:
            print "Leap Year!"
        else "Not a Leap Year"
    else "Not a Leap Year"
else "Not a Leap Year"
'''

year = int(input("Year: "))

if year%4 == 0:
    print("Leap Year!")
else:
    print("Not a Leap Year")