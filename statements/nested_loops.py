rows = int(input("How Many Rows?: "))
columns = int(input("How Many Colums?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")  # end= a for example
    print()
