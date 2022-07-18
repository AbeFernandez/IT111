import random
import string

solutionFile = open("solution.txt", "r")


# Word randomizer
guess = []
solutionList = []
for word in solutionFile:
    solutionList.append(word.strip("\n"))


solution = solutionList[random.randint(0, len(solutionList) - 1)]
solutionInList = [char for char in solution]
solutionInList = list(dict.fromkeys(solutionInList))
print("The word contain", len(solution), "of blanks")

print("\n-----------Wheel of Fortune Simulation-----------\n")


# Game loop
treatedLetters = []
while sorted(guess) != sorted(solutionInList):
    print("A list of the letters that you already utilize is shown below.")
    print(treatedLetters)
    print()
    # print("[ " + ("_ " * len(solution)) + "]")
    userGuess = input("Enter a letter: ")
    treatedLetters.append(userGuess)

    if userGuess in solution:
        guess.append(userGuess)

    # Print your progress
    for letter in solution:
        if letter in guess:

            print(letter)
        else:
            print("?")

solutionFile.close()
print("\nGreat job! You complete the word " + solution + ".")
