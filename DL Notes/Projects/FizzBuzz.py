for n in range(1,100):
    if n % 3 != 0 and n % 5 != 0:
        print(n)
    elif n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    elif n % 3 != 0 and n % 5 == 0:
        print("Buzz")
    elif n % 7 == 0:
        print("Bazz")
    else:
        print("FizzBuzz")