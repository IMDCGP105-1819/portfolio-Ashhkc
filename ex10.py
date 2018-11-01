highValue = int(input("Enter a value greater than 50: "))
lowValue =  int(input("Enter a value lower than 50: "))


for a in range(lowValue, highValue):
    if a % 3 and a % 5:
        print("FizzBuzz: ", a)
    elif a % 3:
        print("Fizz: ", a)
    elif a % 5:
        print("Buzz: ", a)
    else:
        print("None: "a)
