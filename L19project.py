import random
no1=random.randint(1,5)
no2=random.randint(6,10)
result=no1*no2
guess=0


while guess!=result:
    result=int(input("Guess the product"))
    if no1*no2==result:
        print("COngratulations, its correct")
    else:
        print("Try again")