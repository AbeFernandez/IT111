import os

loopControl = True
while loopControl:
    print()
    print("                Menu")
    print("PRESS A - Append to 'Project2Update.txt' ")
    print("PRESS C - Saves a copy of the file with a different file name ")
    print("PRESS D - Delete the original file ")
    print("PRESS E - For 'EXIT' ")
    print()

    userSelection = input("Choose from the menu: ")

    if userSelection == "A" or userSelection == "a":
        # Opens a file for append
        myFile = open("Project2Update.txt", "a")
        myFile.write("\n")

        # The user add text to the file through command line input
        userInput = input("Add a text to the file 'Project2Update.txt': ")
        myFile.write(userInput)
        myFile.close()
        print("Your text have been added to 'Project2Update.txt'")

    if userSelection == "C" or userSelection == "c":
        # Saves a copy of the file with a different file name
        userFileCopy = input("Enter the name of your file copy: ")
        userFileCopy = userFileCopy + ".txt"
        fileCopy = open(userFileCopy, "x")
        fileCopy.close()

        myFile = open("Project2Update.txt", "r")
        fileCopy = open(userFileCopy, "a")
        for line in myFile:
            fileCopy.write(line)

        fileCopy.close()
        myFile.close()
        print("-------Once you exit, you will be able to see this file.-------")

    if userSelection == "D" or userSelection == "d":
        # Deletes the original file
        if os.path.exists("Project2Update.txt"):
            os.remove("Project2Update.txt")
            print("-------Once you exit, the file will appear erased.-------")
        else:
            print("File don't exist!")

    if userSelection == "E" or userSelection == "e":
        loopControl = False


