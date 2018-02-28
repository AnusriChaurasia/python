import random
computer=None
comp=0
score=0
print("start the game")
print("ur score is",score)
print("computer's score is",comp)
l=["paper","rock","scissor"]
print(computer)
while score<=5 or comp<=5:
    computer=random.choice(l)
    print("rock, paper, scissor")
    user=input("enter ur choice:")
    if computer==user:
        print("its a tie")
        print("ur score is", score)
        print("computer's score is",comp)
    elif computer=="rock" and user=="paper":
        print("user wins")
        score+=1
        print("ur score is", score)
        print("computer's score is", comp)
    elif computer=="paper" and user=="rock":
        print("computer wins")
        comp+=1
        print("ur score is", score)
        print("computer's score is", comp)
    elif computer=="paper" and user=="scissor":
        print("user wins")
        score+=1
        print("ur score is", score)
        print("computer's score is", comp)
    elif computer=="scissor" and user=="paper":
        print("computer wins")
        comp+=1
        print(" ur score is", score)
        print("computer's score is", comp)
    elif computer=="rock" and user=="scissor":
        print("computer wins")
        comp+=1
        print("ur score is",score)
        print("computer's score is", comp)
    elif computer=="scissor" and user=="rock":
        print("usre wins")
        score+=1
        print("ur score is ", score)
        print("computer's score is ", comp)
        break
while score>5:
    print("game over")
    break
