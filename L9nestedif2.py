age=int(input("What is your age?"))

if age==15:
    mh=input("Are you mentally well? y,n")
    if mh=="y":
        print("You are elected as the leader")
    else:
        print("You cannot be the leader")

else:
    print("You cannot become the leader as you are underage")