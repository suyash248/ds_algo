def longestCommonSubstring(s, t):
    m = len(s)
    n = len(t)

    def tabulation():
        maxLen = 0
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                        maxLen = max(maxLen, dp[i][j])
                    else:
                        dp[i][j] = 0
        return maxLen

    # def solve(i, j, currLen):
    #     if i < 0 or j < 0:
    #         return currLen
    #     if s[i] == t[j]:
    #         currLen = f(i - 1, j - 1, currLen + 1)
    #     diff1 = solve(i - 1, j, 0)
    #     diff2 = solve(i, j - 1, 0)
    #     return max(currLen, diff1, diff2)
    #
    # return solve(m-1, n-1, 0)

    ans = [0]
    def f(i, j):
        if i < 0 or j < 0:
            return 0
        if s[i] == t[j]:
            ans[0] = max(ans[0], 1 + f(i - 1, j - 1))
        ans[0] = max(ans[0], f(i - 1, j), f(i, j - 1))
        return ans[0]
    # dp = [[-1 for j in range(n + 1)] for i in range(m + 1)]
    return f(m - 1, n - 1)




if __name__ == '__main__':
    print(longestCommonSubstring('tyfg', 'cvbnuty'))
    print(longestCommonSubstring('cd', 'ed'))
