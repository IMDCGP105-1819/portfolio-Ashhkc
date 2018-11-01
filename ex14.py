nterms = int(input("Enter the Number of Terms: "))

n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Invalid Number\nPlease Enter a Positive Interger")
elif nterms == 1:
    print("Fibonacci sequence up to",nterms,": ")
    print(n1)
else:
    print("Fibonacci sequence upto",nterms,": ")
    while count < nterms:
        print(n1,end=' , ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
#MAKE RECURSIVE USING A FUNCTION AND A FOR LOOP
