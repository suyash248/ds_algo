from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)

    # def f(i, dp):
    #     if i == 0:
    #         return nums[i]
    #     if dp[i] == -1:
    #         notTake = f(i-1, dp)
    #         take = nums[i]
    #         if i - 2 >= 0:
    #             take += f(i-2, dp)
    #         dp[i] = max(notTake, take)
    #     return dp[i]
    # dp = [-1 for i in range(n+1)]
    # return f(n-1, dp)

    dp = [0 for i in range(n + 1)]
    for i in range(n):
        if i == 0:
            dp[i] = nums[i]
        else:
            notTake = dp[i - 1]
            take = nums[i]
            if i - 2 >= 0:
                take += dp[i - 2]
            dp[i] = max(notTake, take)
    return dp[n - 1]

if __name__ == '__main__':
    rob([1, 2])
