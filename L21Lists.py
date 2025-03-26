fruits=["mango","orange","guava","peach","watermelon","apple","watermelon","mango","dragonfruit"]
print(fruits)
print(fruits[0])
print(fruits[2])

numbers=[23,43,132,455,35,3,59,9,78,12,23,45,67,90]
print(numbers)
print(type(numbers))
print(len(numbers))  #len is for count of total items
print(len(fruits))   

for i in fruits:
    print(i)

for j in numbers:
    print(j)

fruits.append("banana")   #to add something
print(fruits)
print(fruits.count("watermelon"))
fruits.reverse()
print(fruits)