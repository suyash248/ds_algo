'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.


Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''
from typing import List


def find_max_avg(nums: List[int], k: int) -> List[int]:
    window_sum = 0
    for i in range(0, k):
        window_sum += nums[i]

    window_avg = float(window_sum)/k
    max_avg = window_avg

    for i in range(0, len(nums)-k):
        last_elt = nums[i + k]
        window_sum = window_sum - nums[i] + last_elt
        window_avg = float(window_sum)/k
        max_avg = max(window_avg, max_avg)
    return round(max_avg, ndigits=5)

if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    max_avg = find_max_avg(nums, k)
    print(max_avg)

    nums = [5]
    k = 1
    max_avg = find_max_avg(nums, k)
    print(max_avg)

    nums = [0, 1, 1, 3, 3]
    k = 4
    max_avg = find_max_avg(nums, k)
    print(max_avg)