# 1 5 9  13
# 2 6 10 14
# 3 7 11 15
# 4 8 12 16

def find(table, rows, cols, key):
    row = 0                             # first row
    col = cols-1                        # last col
    while row < rows and col >= 0:
        if key < table[row][col]:
            col -= 1
        elif key > table[row][col]:
            row += 1
        else:                           # key == table[row][col]:
            return (row, col)
    return (-1, -1)

if __name__ == "__main__":
    table = [
        [1, 5, 9,  13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
        [4, 8, 12, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24],
        [25, 26, 27, 28]
    ]
    rows = len(table)
    cols = len(table[0])
    key = input("Please enter key/element you want to search: ")
    i_tup = find(table, rows, cols, key)
    if i_tup[0] < 0 and i_tup[1] < 0:
        print "{} is not present.".format(key)
    else:
        print "{} is present at position -> {}".format(key, i_tup)