weight=int(input("Enter your weight"))
height=float(input("Enter your height"))

bmi=float(weight/ (height/100) **2)
print(bmi)

if (bmi<18.5):
    print("You are underweight")
if (bmi>18.5) and (bmi<24.9):
    print("You are healthy")  
elif (bmi>25):
    print("You are overweight")
elif (bmi>30):
    print("You are suffering from Obesity")