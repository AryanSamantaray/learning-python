"""Take a student's marks as input. Print their grade based on this Scale
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F"""

marks=int(input("Enter your marks: "))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
elif marks>=40:
    print("D")
else:
    print("F")
    