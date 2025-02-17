temp1=int(input("Enter the temperature"))

if (temp1>30):
    print("You have to wear loose clothes")
if (temp1<30) and (temp1>20):
    print("Wear cotton clothes")
if (temp1<20) and (temp1>10):
    print("You would want to wear a sweater")  
elif (temp1<10):
    print("Its freezing, go wear something warm")
