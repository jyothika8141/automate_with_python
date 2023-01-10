def printTable(table):
    rows = len(table)
    cols = len(table[0])

    for i in range(cols):
        for j in range(rows):
            data = table[j][i]
            space = len(max(table[j], key=len)) - len(data)
            print(" " * space, end="")
            print(data, end=" ")
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
