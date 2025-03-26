square=[1,4,9,16,25,36,49,64,81,100]
evennos=[]
oddnos=[]

for i in (square):
    if i %2==0:
        evennos.append(i)
    else:
        oddnos.append(i)
print(evennos)
print(oddnos)