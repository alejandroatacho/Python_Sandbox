import os
# you can also move folders
source = "main//file//placeholder//move.txt"
destination = "main//file//placeholder_test//move.txt"
try:
    if os.path.exists(destination):
        print("that location exists!")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
