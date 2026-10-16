"""
Q2: Take a number as input. Print whether it is even or odd using the %
operator .
"""
a = int(input("Enter a no."))
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")