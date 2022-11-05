from typing import List

MAX = pow(10, 9)

def f(i, tar, nums, dp):
    if i == 0:
        if tar % nums[0] == 0:
            return int(tar / nums[0])
        return MAX
    if dp[i][tar] > 0:
        return dp[i][tar]
    not_pick = f(i - 1, tar, nums, dp)
    pick = MAX
    if nums[i] <= tar:
        pick = 1 + f(i, tar - nums[i], nums, dp)
    dp[i][tar] = min(not_pick, pick)
    return dp[i][tar]

def tabulation(nums, target, dp):
    n = len(nums)
    for tar in range(0, target+1):
        if tar % nums[0] == 0:
            dp[0][tar] = int(tar / nums[0])
        else:
            dp[0][tar] = MAX
    for i in range(1, n):
        for tar in range(0, target+1):
            not_pick = dp[i - 1][tar]
            pick = MAX
            if nums[i] <= tar:
                pick = 1 + dp[i, tar - nums[i]]
            dp[i][tar] = min(not_pick, pick)
    return dp[n-1][target]

def minimumElements(nums: List[int], tar: int) -> int:
    n = len(nums)

    dp = []
    for i in range(0, n):
        r = []
        for t in range(0, tar + 1):
            r.append(-1)
        dp.append(r)

    ans = f(n - 1, tar, nums, dp)
    return -1 if ans >= MAX else ans

if __name__ == '__main__':
    res = minimumElements([1,2,3], 7)
    print(res)