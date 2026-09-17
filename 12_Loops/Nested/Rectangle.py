rows = int(input("Enter the # of Rows: "))
columns = int(input("Enter the # of Columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end = "")
    print()