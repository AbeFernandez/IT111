import random


# Instructions on how to play the game
print("\n--------------- Instructions ------------------------\n")
print("In the first round, you choose the number of the dice.")
print("  - To win: 7 or 11.")
print("  - To lose: 2, 3, or 12.")
print("  - to go to the next round: 4, 5, 6, 8, 9, or 10.")
print("If you proceed to the second round, the game automatically rolls the dice and "
      "\ngenerates a winning point using the first number entered.")
print("  - If rolled the wining point you wins")
print("  - If rolled 7 you lose \n")

# Turn variable
turn = 1

# Input validation
roll = 0
while roll < 2 or roll > 12:
    roll = int(input("Enter a number for the first turn: "))
    if roll < 2:
        print("Too low!")
        print("Try again")

    if roll > 12:
        print("Too high")
        print("Try again")

# First part of the game
if turn == 1 and roll == 7 or roll == 11:
    print("Turn = ", turn)
    print(roll)
    print("Player wins!")

elif turn == 1 and roll == 2 or roll == 3 or roll == 12:
    print("Turn = ", turn)
    print(roll)
    print("Player loses!")

# Second part of the game
elif turn == 1 and roll != 2 or roll != 3 or roll != 7 or roll != 11 or roll != 12:
    print("Turn = ", turn)
    print(roll)

    pointNumber = roll
    turn += 1

    print("Player goes to the next round and to wins need a", pointNumber)

    loopControl = True
    result = ""
    sumOfDice = 0
    while loopControl:
        roll = random.randint(2, 12)
        if turn > 1 and roll == 7:
            result = "Player loses!"
            sumOfDice = sumOfDice + roll
            loopControl = False

        elif turn > 1 and roll == pointNumber:
            result = "Player wins!"
            sumOfDice = sumOfDice + roll
            loopControl = False

        else:
            print("Turn = ", turn)
            print(roll)
            turn += 1
            sumOfDice = sumOfDice + roll

    print("Turn = ", turn)
    print(roll)
    print("\n" + result + " in turn", turn, "with a", roll)
    print("\nReport: ")
    print("Total of turns =", turn)
    print("Sum of the dice total =", sumOfDice)
