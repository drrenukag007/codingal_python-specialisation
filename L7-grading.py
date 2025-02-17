maths=int(input("Enter the marks for maths"))
english=int(input("Enter the marks for english"))
science=int(input("Enter the marks for science"))
sst=int(input("Enter the marks for sst"))
it=int(input("Enter the marks for it"))

sum=maths+english+science+sst+it
percentage= (sum/500)*100

print("You have scored",percentage,"%")

if percentage>90:
    print("Grade A")
elif percentage>80:
    print("Grade B")
elif percentage>70:
    print("Grade C")
elif percentage>60:
    print("Grade D")
else:
    print("Grade F")