from Array import empty_2d_array, empty_1d_array,MAX

def is_safe(board, n, row, col):
    # Same row, upper cols (vertical)
    for r in range(0, row):
        if board[r][col] == 1:
            return False

    # Left diagonal
    r = row; c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1; c-= 1

    # Right diagonal
    r = row; c = col
    while r < n and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1; c -= 1

    return True

"""
[
    [0, 1, 0, 0], 
    [0, 0, 0, 1], 
    [1, 0, 0, 0], 
    [0, 0, 1, 0]
]
"""
# https://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/
def place_queens_v1(board, n, row=0):
    if row >= n:
        return True
    for col in range(0, n):
        if is_safe(board, n, row, col):
            board[row][col] = 1
            if place_queens_v1(board, n, row + 1):
                return True
            board[row][col] = 0     # Backtracking


# https://www.youtube.com/watch?v=xouin83ebxE
def place_queens_v2(positions, n, row=0):
    if row >= n:
        return True
    for col in range(0, n):
        found_safe = True
        for queen in range(0, row):
            position = positions[queen]

            r = position[0]
            c = position[1]
            if c == col or  r+c == row + col or r-c == row-col:
                found_safe = False
                break

        if found_safe:
            positions[row] = (row, col)
            if place_queens_v2(positions, n , row+1):
                return True
    return False


if __name__ == '__main__':
    n = 4
    print "\n********** V1 **********\n"
    board = empty_2d_array(n, n, fill_default=0)
    place_queens_v1(board, n)
    print board

    print "\n********** V2 **********\n"
    positions = empty_1d_array(n)
    place_queens_v2(positions, n)
    print positions