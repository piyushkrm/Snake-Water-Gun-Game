'''
1 for Snake
-1 for water
0 for gun
'''

import random

computer = random.choice([0, 1, -1])
yourChoice = input("Enter your choice : ")
dict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = dict[yourChoice]

# By now we have 2 numbers(variable), you and computer
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you :
    print("Its Draw")
else:
    if (computer - you) == -1 or (computer - you) == 2:
        print("You lose!")
    else:
        print("You win!")
    '''
    if computer == -1 and you == 1:                 
        print("You win!")                                           # -1 - (1) = -2
    elif computer == -1 and you == 0:
        print("You lose!")                                         # -1 - (0) =   -1
    elif computer == 1 and you == -1:
        print("You lose!")                                         #  1 - (-1) = 2
    elif computer == 1 and you == 0:
        print("You win!")                                          #  1 - 0 = 1
    elif computer == 0 and you == -1:
        print("You win!")                                          #  0 - (-1) = 1
    elif computer == 0 and you == 1:
        print("You lose!")                                         #  0 - 1 = -1
    else:
        print("Something went wrong!")
    '''