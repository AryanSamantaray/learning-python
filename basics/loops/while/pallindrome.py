"""Wap to check the given no is pallindrome."""
num=int(input("Enter Number"))
q=num
rev=0
while num!=0:
    rem=num%10
    num=num//10
    rev=rev*10+rem
if q==rev:
    print(f"{q} is a pallindrome")
else:
    print(f"{q} is not a pallindrome")