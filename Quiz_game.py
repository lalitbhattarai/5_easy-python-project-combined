print("Welcome to My computer quiz")

playing=input("OD you want to play? ")

if playing .lower() != "yes" :
    quit()

print("Okey !lets play:)")
score=0

answer= input("What is The capital of nepal? ")
if answer.lower() == "kathmandu":
    print("correct")
    score+=1
else:
    print("Incorrect!")

answer= input("What is the highest peak in Nepal? ")
if answer.lower() == "mt.everest"  :
    print("correct")
    score+=1
else:
    print("Incorrect!")

answer= input("what is the most beautiful city in nepal? ")
if answer.lower()== "pokhara" :
    print("correct")
    score+=1
else:
    print("Incorrect!")

answer= input("Is nepal landlock country? ")
if answer.lower() == "yes" :
    print("correct")
    score+=1
else:
    print("Incorrect!")

print("you got " + str(score) + " Questions correct!  ")
print("you got " + str((score/4) *100) + " % ")