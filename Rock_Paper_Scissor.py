import random
game = {"rock":1,"paper":2,"scissor":3}
x = str(input("enter rock, paper or scissor "))
y = random.randint(1,3)
if x == "rock" and y == 1:
    print('Its a tie')
elif x == "rock" and y == 3:
    print('you won!')
elif x == "rock" and y == 2:
    print('sorry, you lost')
elif x == "paper" and y == 2:
    print('Its a tie')
elif x == "paper" and y == 1:
    print('you won!')
elif x == "paper" and y == 3:
    print('sorry, you lost')
elif x == "scissor" and y == 3:
    print('Its a tie')
elif x == "scissor" and y == 2:
    print('you won!')
elif x == "rock" and y == 1:
    print('sorry, you lost')
else:
    print('This is a very basic game that everybody knows how play, so stop trying to mess around and pls enter either rock, paper or scissor')  

