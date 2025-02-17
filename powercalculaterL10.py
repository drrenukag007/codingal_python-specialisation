x=int(input("Which numbers power do you want to calculate?"))
y=int(input("To which do you want to raise it?"))
result=1

for i in range(1,x**y):
    result=result+i
    print(result)
