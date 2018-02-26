#Program for snake n ladder game.
import random
count=0
print("Welcome ")
print("Your current position is",count)
while(count<100):
     i=random.randint(1,6)
     j=input("Press enter to continue")
     count=count+i
     print("Your current position is",count)
     if count==8:
         count=37
         print("You climbed the ladder")
     elif count==11:
           count=2
           print("Snake bite")
     elif count==13:
           count=34
           print("You climbed the ladder")
     elif count==25:
           count=4
           print("Snake bite")
     elif count==38:
           count=9
           print("Snake bite")
     elif count==40:
           count=68
           print("You climbed the ladder")
     elif count==52:
           count=81
           print("You climbed the ladder")
     elif count==65:
           count=46
           print("Snake bite")
     elif count==76:
           count=97
           print("You climbed the ladder")
     elif count==89:
           count=70
           print("Snake bite")
     elif count==93:
           count=64
           print("Snake bite")
     elif count==100:
           print("YOU WON")
           break
     while(count>100):
          count=count-i
          print("Try again")
          break
