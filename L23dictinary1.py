#Dictinary is a data structure which stores group values. It is divided into two parts: Keys:Values

groceries={"fruits":5,"vegies":7,"cleaning":6,"school":3,"clothes":2}
print(groceries)
print(type(groceries))

groceries["chocolates"]=13
print(groceries)

print(len(groceries))
groceries["school"]=1
print(groceries)

groceries.pop("cleaning")
print(groceries)

