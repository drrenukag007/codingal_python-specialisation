actual=int(input("Enter the actual product price in rupees. "))
sales=int(input("Enter the sales amount in rupees. "))
if actual>sales:
    amount=actual-sales
    print("profit of",amount)
else:
    print("loss")