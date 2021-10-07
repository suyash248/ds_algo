'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

from typing import List

def longestSubarray(nums: List[int], threshold: int = 1):
    l, r, zc = 0, 0, 0
    max_w_len, max_w_l= 0, 0

    while r < len(nums):
        if zc <= threshold:
            if nums[r] == 0:
                zc += 1
            r += 1

        if zc > threshold:
            if nums[l] == 0:
                zc -= 1
            l += 1

        w_len = r - l
        if w_len > max_w_len:
            max_w_len = w_len
            max_w_l = l

    # (max_w_len - threshold), becuase the zero bit we flipped above, should be deleted.
    return max_w_len - threshold, max_w_l, max_w_l + max_w_len - 1

if __name__ == '__main__':
    idxs = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1] # r - 1 - l - threshold

    threshold = 1
    max_w_len, max_w_l, max_w_r = longestSubarray(nums, threshold)
    print(max_w_len, max_w_l, max_w_r)