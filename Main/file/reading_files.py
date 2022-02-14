try:
    with open("main//file//placeholder//text.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file is not found: (")
print(file.closed)
