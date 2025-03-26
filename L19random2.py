import random
computer_no=random.randint(1,10)
guess=0


while computer_no!=guess:
    guess=int(input("Guess a number"))
    if guess==computer_no:
        print("You have guessed the number, Congratulations")
    else:
        print("The number is incorrect")






