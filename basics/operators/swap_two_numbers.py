"""given two numbers a and b, you need to swap their values so a holds the value of b and b holds the value of a. python"""
a=int(input("Enter 1st no.: "))
b=int(input("Enter 2nd no.: "))
temp=a
a=b
b=temp
print(f"a={a} \t b={b}")