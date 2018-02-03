#ask for input
#prime is > 1 and divisible 1 and itself
n = input("Enter a number:")
n = int(n)

def testforprime(n):
    if (n==1):
        return ("This is not a prime number")
    elif (n==2): 
        return ("This is a prime number");
    else:
        for x in range (2,n):
            if (n%x==0):
                return print("This is not a prime number")
            return ("This is a prime number")
print(testforprime(n))
            