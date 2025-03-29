speed1=int(input("Enter the speed of 1st cyclist in km/h. "))
speed2=int(input("Enter the speed of 2nd cyclist in km/h. "))
speed3=int(input("Enter the speed of 3rd cyclist in km/h. "))

average=((speed1+speed2+speed3)/3)
print(average,"is the average speed")

if (speed1<average):
    print("1st cylcist is slower than the average")
if (speed2<average):
    print("2nd cyclist is slower than the average")
if (speed3<average):
    print("3rd cyclist is slower than the average.")
