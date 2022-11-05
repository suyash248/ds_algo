from sys import maxsize
from math import exp,pow

MIN = int(pow(-10, 9))

def recursive(i, j, m, n, matrix, dp):
    if j < 0 or j >= n:
        return MIN
    if i == 0:
        return matrix[i][j]
    if dp[i][j] != None:
        return dp[i][j]
    dl = matrix[i][j] + recursive(i-1, j-1, m, n, matrix, dp)
    dr = matrix[i][j] + recursive(i-1, j+1, m, n, matrix, dp)
    u = matrix[i][j] + recursive(i-1, j, m, n, matrix, dp)
    dp[i][j] = max(dl, dr, u)
    return dp[i][j]


def tabulation(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[None for j in range(n)] for i in range(m)]
    for j in range(0, n):
        dp[0][j] = matrix[0][j]
    for i in range(1, m):
        for j in range(0, n):
            dl = matrix[i][j] + (MIN if j - 1 < 0 else dp[i - 1][j - 1])
            dr = matrix[i][j] + (MIN if j + 1 >= n else dp[i - 1][j + 1])
            u = matrix[i][j] + dp[i - 1][j]
            dp[i][j] = max(dl, dr, u)

    # print(dp)
    maxPathSum = MIN
    for j in range(0, n):
        maxPathSum = max(maxPathSum, dp[m - 1][j])
    return maxPathSum

if __name__ == '__main__':
    # 1 2 10 4
    # 100 3 2 1
    # 1 1 20 2
    # 1 2 2 1
    matrix = [
        [1, 2, 10, 4],
        [100, 3, 2, 1],
        [1, 1, 20, 2],
        [1, 2, 2, 1]
    ]
    m = len(matrix)
    n = len(matrix[0])

    maxPathSum = tabulation(matrix)
    print(maxPathSum)

    maxPathSum = -exp(9)
    for j in range(0, n):
        dp = [[None for j in range(n)] for i in range(m)]
        currSum = recursive(m - 1, j, m, n, matrix, dp)
        maxPathSum = max(maxPathSum, currSum)
        # print(currSum)
    print(maxPathSum)