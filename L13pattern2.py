number=1
for i in range(1,6):
    for j in range(1,i+1):
        print(number,end=" ")
        number=number+1
    print()




num=input("Enter the pattern type")

for i in range(1,11):
    for j in range(1,i+2):
        print(num*i,end=" ")
    print()
        

num=input("Enter the pattern type")

for i in range(1,11):
    for j in range(1,i+2):
        print(num*j,end=" ")
    print()
        
        