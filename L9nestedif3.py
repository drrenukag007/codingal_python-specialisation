x=input("Are you hungry? y,n")
if x=="y":
   a=input("What would you like to have? b=burger,p=pizza,n=noodles")
   if a=="b":
      print("Okay lets get burger for you")
   elif a=="p":
      print("Okay, lets have pizza for you")
   elif a=="n":
      print("Okay, lets have noodles for you")
   else:
      print("Select the right option")

else:
   print("Okay, come back when you are hungry")
