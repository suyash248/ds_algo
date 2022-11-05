def recursive(i, target, arr, dp):
    if target == 0: return True
    if i == 0: return target == arr[0]
    if dp[i][target] is not None:
        return dp[i][target]
    not_pick = recursive(i - 1, target, arr, dp)
    pick = False
    if arr[i] <= target:
        pick = recursive(i - 1, target - arr[i], arr, dp)
    dp[i][target] = pick or not_pick
    return dp[i][target]


def tabulation(n, k, arr):
    dp = []
    for i in range(0, n):
        row = []
        for target in range(0, k+1):
            row.append(False)
        dp.append(row)
    for i in range(0, n):
        dp[i][0] = True
    for target in range(1, k):
        dp[0][target] = target == arr[0]

    # if arr[0] <= k:
    #     dp[0][arr[0]] = True
    for i in range(1, n):
        for target in range(1, k + 1):
            not_pick = dp[i - 1][target]
            pick = False
            if arr[i] <= target: pick = dp[i - 1][target - arr[i]]
            dp[i][target] = pick or not_pick
    print(dp[0])
    return dp[n - 1][k]


def subsetSumToK(n, k, arr):
    dp = []
    for i in range(0, n):
        row = []
        for target in range(0, k + 1):
            row.append(None)
        dp.append(row)
    return recursive(n - 1, k, arr, dp)


cnt = 0
class Solution:
    def f(self, i, l, v):
        global cnt
        if i == 0:
            cnt += 1
            return
        for j in range(l, len(v)):
            self.f(i - 1, j, v)

    def countVowelStrings(self, n: int) -> int:
        global cnt
        self.f(n, 0, ['a', 'e', 'i', 'o', 'u'])
        return cnt

def generateParenthesis( n: int) :
    def f(o, c, op, res):
        if o == 0 and c == 0:
            res.append(op)
            return

        if o > 0:
            op1 = op + "("
            f(o - 1, c, op1, res)
        if o < c:
            op2 = op + ")"
            f(o, c - 1, op2, res)

    res = []
    f(n, n, "", res)
    return res

def numberOfArithmeticSlices(nums):
    n = len(nums)

    # 1 3 5 7 9
    def isAP(arr):
        if len(arr) <= 2:
            return True
        d = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != d:
                return False
        return True

    def f():
        cnt = 0

        for i in range(n - 2):
            for j in range(i + 2, n):
                subArr = nums[i:j + 1]
                print(subArr, isAP(subArr))
                if isAP(subArr):
                    cnt += 1
        return cnt

    return f()

if __name__ == '__main__':
    # arr = [6, 1, 2, 1]
    # arr = list(map(int, "6 1 2 1".split(" ")))
    # k = 4
    # n = 4
    # print(subsetSumToK(n, k, arr))
    # print(tabulation(n, k, arr))
    numberOfArithmeticSlices([1,2, 3, 4])