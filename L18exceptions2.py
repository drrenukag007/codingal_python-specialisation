
try:
    age=int(input("Enter your age"))
    if age<18:
        raise ValueError
    else:
        print("The age is valid")

except ValueError:
    print("The age is not valid")

finally:
    print("End of the program")