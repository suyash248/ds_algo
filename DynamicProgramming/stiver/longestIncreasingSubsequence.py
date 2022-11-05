from sys import stdin
import sys

sys.setrecursionlimit(10 ** 7)


def lowerBound(arr, k):
    n = len(arr)
    s, e, lb = 0, n - 1, -1
    while s <= e:
        mid = int(e - (e - s) / 2)

        if k < arr[mid]:
            e = mid - 1
        elif k > arr[mid]:
            s = mid + 1
        else:
            return mid
    return s


def longestIncreasingSubsequence(arr, n):
    #     def f(i, p, dp):
    #         if i == n:
    #             return 0
    #         else:
    #             if dp[i][p+1] == -1:
    #                 if p == -1 or arr[p] < arr[i]:
    #                     dp[i][p+1] = max(1 + f(i+1, i, dp), f(i+1, p, dp))
    #                 else:
    #                     dp[i][p+1] = f(i+1, p, dp)
    #             return dp[i][p+1]
    #     dp = [[-1 for p in range(n+1)] for i in range(n+1)]
    #     return f(0, -1, dp)

    #     dp = [[0 for p in range(n+1)] for i in range(n+1)]
    #     for i in range(n-1, -1, -1):
    #         for p in range(i-1, -2, -1):
    #             if p == -1 or arr[p] < arr[i]:
    #                 dp[i][p+1] = max(1 + dp[i+1][i+1], dp[i+1][p+1])
    #             else:
    #                 dp[i][p+1] = dp[i+1][p+1]
    #     return dp[0][0]

    temp = [arr[0]]
    for i in range(1, n):
        if arr[i] > temp[-1]:
            temp.append(arr[i])
        else:
            lb = lowerBound(temp, arr[i])
            temp[lb] = arr[i]
    return len(temp)


if __name__ == '__main__':
    arr = [0, 1, 0, 3, 2, 3]
    print(longestIncreasingSubsequence(arr, len(arr)))
