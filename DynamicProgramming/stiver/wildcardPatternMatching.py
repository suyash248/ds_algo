def wildcardMatching(pat, txt):
    m, n = len(pat), len(txt)

    # def f(i, j, dp):
    #     if i < 0 and j < 0: # pat & txt both exahusted.
    #         return True
    #     if i < 0 and j >= 0: # pat exhausted, txt remaining.
    #         return False
    #     if i >= 0 and j < 0: # path remaining, txt exhausted.
    #         for k in range(i+1):
    #             if pat[k] != '*':
    #                 return False
    #         return True
    #     else:
    #         if not dp[i][j]:
    #             if pat[i] == txt[j] or pat[i] == '?':
    #                 dp[i][j] = f(i - 1, j - 1, dp)
    #             elif pat[i] == '*':
    #                 dp[i][j] = f(i - 1, j, dp) or f(i, j - 1, dp)
    #             else:
    #                 dp[i][j] = False
    #         return dp[i][j]
    #
    # dp = [[False for j in range(n)] for i in range(m)]
    # return f(m - 1, n - 1, dp)

    dp = [[False for j in range(n + 1)] for i in range(m + 1)]
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if i == 0 and j == 0:
                dp[0][0] = True
            elif i == 0 and j > 0:
                dp[i][j] = False
            elif i > 0 and j == 0:
                flag = True
                for k in range(1, i + 1):
                    if pat[k - 1] != '*':
                        flag = False
                        break
                dp[i][j] = flag
            else:
                if pat[i - 1] == txt[j - 1] or pat[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pat[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
    return dp[m][n]

if __name__ == '__main__':
    # print(wildcardMatching("**", "abcdefhjo"))
    print(wildcardMatching("*a*b", "adceb"))