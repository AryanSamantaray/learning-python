"""
Q4: A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string.
"""
a=int(input("Enter marks of sub1 :"))
b=int(input("Enter marks of sub2 :"))
c=int(input("Enter marks of sub3 :"))
total=a+b+c
avg=total/3
print(f"The total is {total} and the avg is {avg}")