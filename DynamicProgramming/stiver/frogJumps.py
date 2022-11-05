from typing import List

def frogJump(n: int, heights: List[int]) -> int:
    # def f(i):
    #     if i == 0:
    #         return 0
    #     if i == 1:
    #         return abs(heights[0] - heights[1])
    #     return min(abs(heights[i] - heights[i-1]) + f(i-1),
    #                abs(heights[i] - heights[i-2]) + f(i-2)
    #               )
    # return f(n-1)

    dp = [0 for i in range(n + 1)]
    for i in range(0, n):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = abs(heights[0] - heights[1])
        else:
            dp[i] = min(abs(heights[i] - heights[i - 1]) + dp[i - 1],
                        abs(heights[i] - heights[i - 2]) + dp[i - 2]
                        )
    return dp[n - 1]

if __name__ == '__main__':
    print(frogJump(4, [10, 20, 30, 10]))