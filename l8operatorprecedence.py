a=54
b=33
c=21
d=89
e=60
f=73

answer=(((a/b)*(e/f**3)+(c**2+d))/b)
print("the answer is",answer)


year=int(input("Enter a year. "))

if (year%4)==0:
    if (year%100)==0:
        print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")