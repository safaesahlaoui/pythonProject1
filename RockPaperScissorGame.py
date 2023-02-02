import random
choices =['rock','papper','scissors']
computer = random.choice(choices)
player=None
while player not in choices:
    player = input("rock , papper or scissors ?:")
print("computer : ",computer)
print("player : " ,player)
if player==computer:
    print('play again')
elif player=="rock":
    if computer=="papper":
        print('you Loose :(')
    elif computer=="scissors":
        print('You Win :)')
elif player =='papper':
    if computer=='rock':
        print('You Win :)')
    elif computer=='scissors':
        print("You Loose :( ")
elif player =='scissors':
    if computer=='papper':
        print("You Win :)")
    elif computer=='rock':
        print("You Loose :(")

