import random

# Turn variable
turn = 1
print(turn)
input("Press 'ENTER' to roll the dice! ")
roll = 0
while roll < 2 or roll > 12:
    roll = int(input("Enter a number: "))

    # Check for input out of range
    if roll < 2:
        print("Too low!")

    if roll > 12:
        print("Too high")


if turn == 1 and roll == 7 or roll == 11:
    print(roll)
    print("Player wins!")

if turn == 1 and roll == 2 or roll == 3 or roll == 12:
    print(roll)
    print("Player loses!")
