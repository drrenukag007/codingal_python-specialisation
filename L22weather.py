weather=(0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0)
print(weather)
rain=[]
sun=[]
for i in (weather):
    if i==0:
        print("Its raining")
        rain.append(i)
    else:
        print("Its sunny")
        sun.append(i)
print(len(rain))
noofrainydays=len(rain)
print(len(sun))
noofsunnydays=len(sun)

if noofrainydays>noofsunnydays:
    print("Maximum days of the month were raining")
else:
    print("Maximum days were sunny")