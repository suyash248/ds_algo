# Time complexity: O(n)
# Using sliding window strategy.
def flip_m_zeroes_largest_subarray_with_max_ones(arr, m):
    """

    :param arr: Input array.
    :param m: Maximum number of 0's that can be flipped in `arr` in order to get largest window/sub-array of 1's.
    :return:
    """
    w_left = w_right = best_w_left = best_w_size = zeroes_count = 0

    while w_right < len(arr):
        if zeroes_count <= m:
            if arr[w_right] == 0:
                zeroes_count += 1
            w_right += 1

        if zeroes_count > m:
            if arr[w_left] == 0:
                zeroes_count -= 1
            w_left += 1

        curr_w_size = w_right - w_left
        if curr_w_size > best_w_size:
            best_w_left = w_left
            best_w_size = curr_w_size

    best_w_right = best_w_left + best_w_size - 1
    best_w = (best_w_left, best_w_right)
    flip_zero_at_indices = []

    for i in xrange(best_w_left, best_w_right+1): # for i=0; i < best_w_size; i++
        if arr[i] == 0:
            flip_zero_at_indices.append(i)

    return {
        "largestWindow": best_w,
        "largestWindowSize": best_w_size,
        "flipZeroAtIndices": flip_zero_at_indices
    }


if __name__ == '__main__':
    arr = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
    m = input("Maximum number of 0's allowed to be flipped -> ")
    window_details = flip_m_zeroes_largest_subarray_with_max_ones(arr, m)
    print "Flip 0's at indices {flipZeroAtIndices} to get the maximum window/sub-array of size {largestWindowSize} " \
          "where window start & end indices are {largestWindow}".format(**window_details)
