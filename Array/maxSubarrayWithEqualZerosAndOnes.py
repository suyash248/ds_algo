def max_subarray_with_equal_zeros_ones_v1(arr):
    sum_arr = [None] * len(arr)
    sum_arr[0] = 1 if arr[0] == 1 else -1

    # Construct sum_array
    for i in xrange(1, len(arr)):
        curr = 1 if arr[i] == 1 else -1
        sum_arr[i] = sum_arr[i-1] + curr

    max_len = 0; hm = dict(); i = 0

    for sum in sum_arr:
        if sum == 0:
            max_len = max(max_len, i+1)

        if hm.has_key(sum):
            max_len = max(max_len, i - hm[sum])
        else:
            hm[sum] = i
        i += 1

    return max_len


if __name__ == "__main__":
    arr = [0, 0, 0, 1, 0, 0, 1, 1, 1]
    max_len = max_subarray_with_equal_zeros_ones_v1(arr)
    print "Max length {}".format(max_len)