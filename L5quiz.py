score=0
var1="Welcome to the Quiz, by the quiz master Noor"
print(var1)
Q1=input("What is the capital of India? a-Mumbai,b-Kashmir,c-New Delhi")
if Q1=="c":
    print("correct answer, bravo")
    score+=10
    print("you have scored",score)
else:
    print("Try again")

Q2=input("Which state is known for its beaches in India? a-goa,b-Mumbai,c-Kerala")
if Q2=="a":
   print("Correct Answer, way to go") 
   score+=10
   print("you have scored",score)   
else: 
    print("Wrong Answer")

Q3=input("Who is known as the 'Father of the Nation' in India? a-Jawaharlal Nehru,b-Mahatma Gandhi,c-Subhas Chandra Bose")
if Q3=="b":
   print("Great, the answer is correct")
   score+=10
   print("you scored",score)
else:
   print("Try again")
Q4=input("Which river is considered the longest in India? a-Ganga,b-Brahmaputra,c-Godavari")
if Q4=="a":
    print("Good Job")
    score+=10
    print("You scored",score)
else:
    print("Error")
Q5=input("What is the national animal of India? a-lion,b-Tiger,c-Leopard")
if Q5=="b":
    print("You are trippin bruh")
    score+=10
    print("You have scored",score)
else:
    print("where your mind at?")

