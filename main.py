#SNAKE, WATER, GUN GAME

'''
snake =  1
water = -1
gun   =  0

'''
import random
youstr = input("Enter your choice: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youDict[youstr]

computer = random.choice([-1, 0, 1])
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("It's a draw")
else:
    if (computer == -1 and you == 1):
        print("You win")
    elif (computer == -1 and you == 0):
        print("You lose")
    elif (computer == 1 and you == -1):
        print("You lose")
    elif (computer == 1 and you == 0):
        print("You win")
    elif (computer == 0 and you == -1):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You lose")
    else:
        print("Something went wrong")