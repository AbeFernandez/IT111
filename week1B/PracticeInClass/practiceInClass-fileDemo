# Practice in class: File Demo
import os

# Create a file
myFile = open("myFile.txt", "x")

# Write in a file
myFile = open("myFile.txt", "w")
myFile.write("Hello World")

# Append to a file
myFile = open("myFile.txt", "a")
myFile.write("\nHello, again")
myFile.close()

# Remove the file
if os.path.exists("myFile.txt"):
    os.remove("myFile.txt")
else:
    print("File don't exist!")

