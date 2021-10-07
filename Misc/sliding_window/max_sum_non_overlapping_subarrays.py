# 1031. Maximum Sum of Two Non-Overlapping Subarrays
# Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
#
# The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
# Example 2:
#
# Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
# Example 3:
#
# Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
#
#
# Constraints:
#
# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000

from typing import List

def maxSumTwoNoOverlap(nums: List[int], firstLen: int, secondLen: int) -> int:
    sum1, l1, r1 = _max_sum_subarray_(nums, firstLen)
    sum2 = 0
    if len(nums) - 1 - r1 >= secondLen:
        sum1_r, l1_r, r1_r = _max_sum_subarray_(nums[r1+1:], secondLen)
        sum2 = max(sum2, sum1_r)

    if l1 >= secondLen:
        sum1_l, l1_l, r1_l = _max_sum_subarray_(nums[:l1], secondLen)
        sum2 = max(sum2, sum1_l)

    sum_first = sum1 + sum2

    sum1, l1, r1 = _max_sum_subarray_(nums, secondLen)
    sum2 = 0
    if len(nums) - 1 - r1 >= firstLen:
        sum1_r, l1_r, r1_r = _max_sum_subarray_(nums[r1 + 1:], firstLen)
        sum2 = max(sum2, sum1_r)

    if l1 >= firstLen:
        sum1_l, l1_l, r1_l = _max_sum_subarray_(nums[:l1], firstLen)
        sum2 = max(sum2, sum1_l)

    sum_second = sum1 + sum2

    return max(sum_first, sum_second)

def _max_sum_subarray_(nums: List[int], k: int):
    w_sum = 0
    max_w_l = 0
    for i in range(0, min(k, len(nums))):
        w_sum += nums[i]

    max_sum = w_sum

    for i in range(0, len(nums) - k):
        w_sum = w_sum - nums[i] + nums[i + k]
        if w_sum > max_sum:
            max_sum = w_sum
            max_w_l = i + 1

    return max_sum, max_w_l, max_w_l + k - 1

if __name__ == '__main__':
    # nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    # firstLen = 1
    # secondLen = 2
    # max_sum = maxSumTwoNoOverlap(nums, firstLen, secondLen)
    # print(max_sum)
    #
    # nums = [3, 8, 1, 3, 2, 1, 8, 9, 0]
    # firstLen = 3
    # secondLen = 2
    # max_sum = maxSumTwoNoOverlap(nums, firstLen, secondLen)
    # print(max_sum)
    #
    # nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
    # firstLen = 4
    # secondLen = 3
    # max_sum = maxSumTwoNoOverlap(nums, firstLen, secondLen)
    # print(max_sum)

    nums = [8, 20, 6, 2, 20, 17, 6, 3, 20, 8, 12]
    firstLen = 5
    secondLen = 4
    max_sum = maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(max_sum)