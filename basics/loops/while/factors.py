"""Ask a number from the user, and print all the factors."""
a=int(input("Enter a number: "))
i=1
while i<=a:
    if (a%i==0):
        print(i)
    i+=1
