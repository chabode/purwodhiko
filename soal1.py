rows = input("Enter number of rows ")
rows = int (rows)
for i in range (rows):
    for j in range(rows,i, -1):
        print("*", end=' ')
    print("\r")