game=int(input("How many lives do you have?"))
if game<1:
        print("You cannot play ")
while game>1:
    print("You can countinue playing")
    if game<1:
        print("You cannot play further as all your lives are gone")
    game=game-1
