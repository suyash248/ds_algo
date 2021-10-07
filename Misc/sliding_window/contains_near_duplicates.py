'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:

    if len(nums) <= 1:
        return False

    hm = dict()
    w_len = min(k+1, len(nums))
    for i in range(0, w_len):
        if nums[i] in hm:
            return True
        hm[nums[i]] = 1

    for i in range(1, len(nums) - w_len + 1):
        last_elt = nums[i + w_len - 1]

        hm.pop(nums[i-1])
        if last_elt in hm:
            return True
        else:
            hm[last_elt] = 1
    return False

if __name__ == '__main__':
    nums = [1, 2]
    k = 2
    res: bool = containsNearbyDuplicate(nums, k)
    print(res)

    nums = [1, 2, 3, 1]
    k = 3
    res: bool = containsNearbyDuplicate(nums, k)
    print(res)

    nums = [1, 0, 1, 1]
    k = 1
    res: bool = containsNearbyDuplicate(nums, k)
    print(res)

    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    res: bool = containsNearbyDuplicate(nums, k)
    print(res)


