"""A shop gives discounts based on purchase amount:
Above 5000 → 20% discount
Above 2000 → 10% discount
Above 1000 → 5% discount
1000 or below → no discount"""
amt=float(input("Enter your amount"))
if amt>5000:
    discount =20
elif amt>2000:
    discount =10
elif amt>1000:
    discount =10
else:
    print("no discount")

discount_amt=amt*(discount/100)
final_amt= amt-discount_amt
    