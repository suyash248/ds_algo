# Time complexity: O(n)
# Space complexity: O(n)
def max_subarray_with_equal_zeros_ones_count(arr):
    """
    :param arr:
    :return: `Length` of the longest sub-array with equal 0s and 1s
    """
    sum_arr = [None] * len(arr)
    sum_arr[0] = 1 if arr[0] == 1 else -1

    # Construct sum_array
    for i in xrange(1, len(arr)):
        curr = 1 if arr[i] == 1 else -1
        sum_arr[i] = sum_arr[i-1] + curr

    max_len = 0; hm = dict(); i = 0

    for sum_elt in sum_arr:
        if sum_elt == 0:
            max_len = max(max_len, i+1)

        if hm.has_key(sum_elt):
            max_len = max(max_len, i - hm[sum_elt])
        else:
            hm[sum_elt] = i
        i += 1

    return max_len


# Time complexity: O(n)
# Space complexity: O(n)
def max_subarray_with_equal_zeros_ones(arr):
    """
    :param arr:
    :return: Tuple containing -
        1. `Length` of the longest sub-array with equal 0s and 1s.
        2. Longest sub-array with equal 0s and 1s, (start, end).
        3. All sub-array(s) with equal 0s and 1s.
    """
    sum_arr = [None] * len(arr)
    sum_arr[0] = 1 if arr[0] == 1 else -1

    # Construct sum_array
    for i in xrange(1, len(arr)):
        curr = 1 if arr[i] == 1 else -1
        sum_arr[i] = sum_arr[i-1] + curr

    max_len = 0; hm = dict(); i = 0; all_sub_arrays = []; max_sub_array = ()

    for sum in sum_arr:
        if sum == 0:
            curr_len = i + 1
            if curr_len > max_len:
                max_sub_array = (0, i)
            max_len = max(max_len, curr_len)
            all_sub_arrays.append((0, i))

        if hm.has_key(sum):
            prev_index = hm[sum]
            curr_len = i - hm[sum]

            if curr_len > max_len:
                max_sub_array = (prev_index+1, i)

            max_len = max(max_len, curr_len)
            all_sub_arrays.append((prev_index+1, i))
            #print "sum:", sum, "at i:", i, (prev_index+1, i), " curr_len:", curr_len, "max_len:", max_len
        else:
            hm[sum] = i
        i += 1

    return max_len, max_sub_array, all_sub_arrays


if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    #arr = [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1]
    max_len, max_sub_array, all_sub_arrays = max_subarray_with_equal_zeros_ones(arr)
    print "Max length sub array is of length {}.".format(max_len)
    print "Max sub-array (start, end) - ", max_sub_array
    print "All the sub-arrays (start, end) are -", all_sub_arrays
