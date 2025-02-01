name=input("Hey! what is you name:  ")
print("welcome", name ,"to the journey")

answer=input("You are infront a dirt road.there are two road avilable choose you want to go right or left: ").lower()

if answer=="right":
    answer=input("Now ,you have rached near a bridge .you can swim or go form bridge(up for go from bridge /down for a swim): ")
    if answer=="up":
        answer==input("you have cross a bridge and reach the main road  .Now you can wait for a lift or start walking(walk/wait): ").lower()
        if answer=="walk":
            print("You got hit by the truck .....You died")
        elif answer=="wait":
            print("Ha,you got attack by bear ..you died")
        else:
            print("sucide....why bro why...")
    elif answer=="swim":
           print("You got eaten by an aligator! you dies")
    else:
        print("invalid option ! Sucide....?")




elif answer=="left":
    print("you won")
else:
    print("you died")
