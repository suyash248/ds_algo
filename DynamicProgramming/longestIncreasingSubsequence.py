from Array import empty_1d_array

"""
input array : [10, 22, 9, 33, 21, 50, 41, 60]

# Element at each index `i` is representing length of longest LIS from index 0 to i in input array.
output array: [1,  2,  1, 3,  2,  4,  4,  5]      
"""
# Time complexity: O(n^2)
# Space complexity: O(n)
def lis_dp(arr):
    # Length of LIS at each index is at least 1 (element itself).
    n = len(arr)
    lis_arr = empty_1d_array(n, 1)

    for i in xrange(1, n):                          # for i=1; i<n; i++
        for j in xrange(0, i):                      # for j=0; j<i; j++
            if arr[i] > arr[j] :                    # and lis_arr[i] < lis_arr[j]+1:
                prev_lis_till_i = lis_arr[i]
                curr_lis_till_i = lis_arr[j] + 1
                if curr_lis_till_i > prev_lis_till_i:
                    # Update lis_till_i
                    lis_arr[i] = curr_lis_till_i
    # print lis_arr
    return max(lis_arr)


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    max_lis = lis_dp(arr)
    print "Length of longest increasing sub-sequence for given array is {}".format(max_lis)