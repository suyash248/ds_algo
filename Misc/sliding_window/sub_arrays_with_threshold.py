'''
Given an array of integers arr and two integers k and threshold.

Return the number of sub-arrays of size k and average greater than or equal to threshold.



Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [1,1,1,1,1], k = 1, threshold = 0
Output: 5
Example 3:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
Example 4:

Input: arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
Output: 1
Example 5:

Input: arr = [4,4,4,4], k = 4, threshold = 1
Output: 1


Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^4
1 <= k <= arr.length
0 <= threshold <= 10^4
'''
from typing import List


def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    res = 0
    w_sum = 0
    for i in range(min(k, len(arr))):
        w_sum += arr[i]
    if w_sum/k >= threshold:
        res += 1

    for i in range(0, len(arr) - k):
        right_elt = arr[i + k]
        w_sum = w_sum - arr[i] + right_elt
        if w_sum / k >= threshold:
            res += 1
    return res

if __name__ == '__main__':
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    res = numOfSubarrays(arr, k, threshold)
    print(arr, k, threshold, res)

    arr = [1, 1, 1, 1, 1]
    k = 1
    threshold = 0
    res = numOfSubarrays(arr, k, threshold)
    print(arr, k, threshold, res)

    arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    k = 3
    threshold = 5
    res = numOfSubarrays(arr, k, threshold)
    print(arr, k, threshold, res)

    arr = [7, 7, 7, 7, 7, 7, 7]
    k = 7
    threshold = 7
    res = numOfSubarrays(arr, k, threshold)
    print(arr, k, threshold, res)

    arr = [4, 4, 4, 4]
    k = 4
    threshold = 1
    res = numOfSubarrays(arr, k, threshold)
    print(arr, k, threshold, res)
