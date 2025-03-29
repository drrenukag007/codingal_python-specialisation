English=int(input("Enter marks out of 100 in English "))
Maths=int(input("Enter marks out of 100 in Maths "))
Physics=int(input("Enter marks out of 100 in Physics "))
Chemistry=int(input("Enter marks out of 100 in Chemistry "))
It=int(input("Enter marks out of 100 in It "))

percentage=((English+Maths+Physics+Chemistry+It)/500)*100
print("Your percentage is",percentage)

if (percentage>90) and (percentage<95):
    print("Your grade is A2")
elif (percentage>95) and (percentage<=100):
    print("Your grade is A1")
elif (percentage>80) and (percentage<85):
    print("Your grade is B2")
elif (percentage>90) and (percentage<95):
    print("Your grade is A2")
else:
    print("Your grade is C or below")