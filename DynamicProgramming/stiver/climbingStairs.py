def climbStairs(n: int) -> int:
    # dp = [-1 for i in range(n+1)]
    # def f(i, dp):
    #     if i <= 1:
    #         return 1
    #     if dp[i] != -1:
    #         return dp[i]
    #     dp[i] = f(i-1, dp) + f(i-2, dp)
    #     return dp[i]
    # return f(n, dp)

    dp = [0 for i in range(n + 1)]
    for i in range(n + 1):
        if i <= 1:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == '__main__':
    print(climbStairs(2))
