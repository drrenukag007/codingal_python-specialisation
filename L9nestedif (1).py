x=input("Are you a medical student? y,n")

if x=="y":
    attendance=input("Is your attendance 75%? y,n")
    if attendance=="y":
        print("You are eligible to attend the exam")
    else:
        print("You are not eligible to attend the exam")

else:
    print("You cannot give the exam")
