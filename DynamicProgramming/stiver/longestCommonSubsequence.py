def f(i1, i2, s, t, dp):
    if i1 == 0 or i2 == 0:
        return 0
    if dp[i1][i2] != -1:
        return dp[i1][i2]
    if s[i1 - 1] == t[i2 - 1]:
        dp[i1][i2] = 1 + f(i1 - 1, i2 - 1, s, t, dp)
    else:
        dp[i1][i2] = max(f(i1 - 1, i2, s, t, dp), f(i1, i2 - 1, s, t, dp))
    return dp[i1][i2]


def lcs(s, t):
    n = len(s)
    m = len(t)
    dp = []
    for i in range(0, n + 1):
        dp.append([0 for j in range(0, m + 1)])

    for i1 in range(0, n + 1):
        for i2 in range(0, m + 1):
            if i1 == 0 or i2 == 0:
                dp[i1][i2] = 0
            else:
                if s[i1 - 1] == t[i2 - 1]:
                    dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
                else:
                    dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])
    #     return dp[n][m]
    #     return f(n, m, s, t, dp)
    print(getLCS(s, t, dp))


def getLCS(s, t, dp):
    lcs = ""
    n = len(s)
    m = len(t)
    i1 = n
    i2 = m
    while i1 > 0 and i2 > 0:
        if s[i1 - 1] == t[i2 - 1]:
            lcs += s[i1 - 1]
            i1 -= 1
            i2 -= 1
        elif dp[i1 - 1][i2] > dp[i1][i2 - 1]:
            i1 -= 1
        else:
            i2 -= 1
    return lcs[::-1]

if __name__ == '__main__':
    s = 'adebc'
    t = 'dcadb'
    lcs(s, t)