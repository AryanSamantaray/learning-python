"""Take three numbers as input. Print the largest of the three without using any
built-in function."""
num1=int(input("Enter no.: "))
num2=int(input("Enter no.: "))
num3=int(input("Enter no.: "))
if num1>=num2 and num1>=num3:
    largest=num1
elif num2>=num1 and num2>=num3:
    largest = num2
else:
    largest=num3

print(f"largest no is {largest}")