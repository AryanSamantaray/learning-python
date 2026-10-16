"""Take two numbers as input. Without using *, calculate and print their product
using += in a way that adds the first number to itself the second number of times."""
a=int(input("Enter first no."))
b=int(input("Enter second no."))
prod=((a+b)**2-a**2-b**2)//2
print(prod)