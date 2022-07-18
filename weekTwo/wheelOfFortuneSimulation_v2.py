

solutionFile = open("solution.txt", "r")
solution = solutionFile.readline()
solution = [char for char in solution]
guess = ["_"] * len(solution)


print(*guess)
# Game loop
while guess != solution:
    userGuess = input("Enter a letter: ")

    # Print your progress
    index = 0
    for letter in solution:
        if userGuess == letter:
            guess[index] = userGuess

            print(letter)
        else:
            print("?")

        index += 1
    print(*guess)

solutionFile.close()
