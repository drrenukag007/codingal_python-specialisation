weight=float(input("Enter your weight in kg "))
height=float(input("Enter your height in m "))

BMI=weight/(height)**2
print("Your BMI is", BMI)

if BMI<=18.4:
    print("you are underweight")
elif (BMI>=18.5) and (BMI<=24.9):
    print("your BMI is normal")
elif (BMI>=25.0) and (BMI<=39.9):
    print("you are overweight")
elif BMI>=40.0:
    print("you are obese. ")