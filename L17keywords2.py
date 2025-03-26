#countinue: even if a condition is true or false but you have to countinue with it.. it will not stop the process
#even if the condition is true. notify.. a sort of warning but not stopping wiht the process

for i in range(1,11):
    if i==3:
        print("I has become 3.")
        continue
    print(i)

#break: stops the process. opp of countinue. 

for i in range(1,11):
    if i==3:
        print("I has become 3.")
        break
    print(i)

