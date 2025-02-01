import random

top_of_range =input("type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Enter the number greater than 0 please")
        quit()
else:
        print("please enter the number next time")
        quit()

random_number=random.randrange(0,top_of_range)
guesses=0

while True:
        guesses +=1
        user_guess=input("make a guess: ")
        if user_guess.isdigit():
            user_guess=int(user_guess)
  
        else:
           print("please enter the number next time")
           continue

        if user_guess ==random_number:
           print("You got it bro!")
           break
        else:
             if user_guess > random_number:
                  print("you aere above the number!")
                  
             else :
                  print("you are below the number")




print("you got in ", guesses , "guesses")
          
         
     



