temperature=int(input("What is today's temperature in Celcius? "))

if (temperature>=30):
    print("You can wear light coloured clothes today.")
elif (temperature>20) and (temperature<30):
    print("You can wear light coloured clothes but preferably with a jacket. ")
else:
    print("Today may not be the best day to wear light coloured clothes.")