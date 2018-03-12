from Array import empty_2d_array

"""
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
"""

def is_safe(board, n, row, col):
    for r in range(0, row):
        if board[r][col] == 1:
            return False

    r = row; c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1; c-= 1

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
    [0, 0, 1, 0]]

"""
def place_queens(board, n, row=0):
    if row >= n:
        return True
    for col in range(0, n):
        if is_safe(board, n, row, col):
            board[row][col] = 1
            if place_queens(board, n, row + 1):
                return True
            board[row][col] = 0

if __name__ == '__main__':
    n = 4
    board = empty_2d_array(n, n, fill_default=0)
    place_queens(board, n)
    print board