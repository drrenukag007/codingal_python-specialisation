no=int(input("Enter a number?"))
number=6
for i in range(6,1):
    for j in range(6,i-1):
        print(number,end=" ")
        number=number-1
    print()