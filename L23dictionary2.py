cars={"Porshe":"red","Audi":"Black","Mercedes":"White","BMW":"Blue","Dodge":"blue","lamborgini":"green"}
print(cars.keys())
print(cars.values())
print(cars.items())

for i,j in cars.items():
    print(i,j)

carname=input("Enter the car name")
print(cars.get(carname))