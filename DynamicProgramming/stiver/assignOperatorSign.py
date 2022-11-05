from typing import List

def targetSum(arr: List[int], target: int) -> int:
    n = len(arr)
    def f(i, t, dp):
        if i < 0:
            if t == 0:
                return 1
            return 0
        else:
            if (i, t) not in dp:
                dp[(i,t)] = f(i-1, t-arr[i], dp) + f(i-1, t+arr[i], dp)
            return dp[(i,t)]
    dp = dict()
    return f(n-1, target, dp)

if __name__ == '__main__':
    print(targetSum([1, 2, 3, 1], 3))