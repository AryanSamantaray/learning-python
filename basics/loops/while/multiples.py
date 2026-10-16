"""Ask a number from the user, print the multiplication table upto 10."""

a = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{a}X{i}={a*i}")
    i += 1
