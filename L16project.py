def shutdown(battery,heat_generated):

    battery=int(input('What is the remaining battery?'))
    heat_generated=input("IS there heat coming out of your PC? y,n")


    if battery>90:
        print("Its better to shut down")
    if heat_generated=="y":
        print("Shut Off")

    else:
        print("You can countinue using it")
        


shutdown(battery=,heat_generated)