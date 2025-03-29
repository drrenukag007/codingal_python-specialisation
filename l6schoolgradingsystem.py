English=int(input("Enter marks out of 100 in English "))
Maths=int(input("Enter marks out of 100 in Maths "))
Physics=int(input("Enter marks out of 100 in Physics "))
Chemistry=int(input("Enter marks out of 100 in Chemistry "))
It=int(input("Enter marks out of 100 in It "))

percentage=((English+Maths+Physics+Chemistry+It)/500)*100
print("Your percentage is",percentage)

if percentage>90:
    print("Your grade is A+")
elif percentage>80:
    print("Your grade is B")
elif percentage>70:
    print("Your grade is C")
elif percentage>60:
    print("Your grade is D")
else:
    print("Please contact the school for further information")