userName = input("Enter you name: ")
userAge = int(input("Enter your age: "))
userHeight = int(input("Enter your height (in cm): "))
userWeight = int(input("Enter your weight (in kg): "))
userEyes = input("Enter your eye colour: ")
userHair = input("Enter your eye colour: ")

if userAge >= 18:
    print("Wow you're a Legal Adult..!")
if userHeight > 190:
    print("Welcome home fellow, Giant!")
if userWeight >= 180:
    print("Damn hit the gym, lose some weight...")
if userHair == "Brown" or userHair == "brown" and userEyes == "Brown" or userHair == "brown":
    print("We have the same eye and hair colour! YAAAY!")
    
