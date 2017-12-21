from Array import empty_1d_array, empty_2d_array

# Time complexity: O(2^n)
# Space complexity: O(n)
def is_subset_sum(arr, n, half_sum):
    """
    Algorithm ->

    Case 1: If sum of all the elements in array is odd, array can't be partitioned into 2 subsets of equals sum.
            So return `False`.

    Case 2: If sum of all the elements in array is even then,
        The is_subset_sum problem can be divided into two sub-problems
         a) is_subset_sum() without considering last element. i.e. (reducing n to n-1)
         b) is_subset_sum() considering the last element. i.e. (reducing n to n-1 and half_sum by arr[n-1])

        If any of the above the above sub-problems return true, then return true.
        isSubsetSum (arr, n, half_sum) = isSubsetSum (arr, n-1, half_sum) || isSubsetSum (arr, n-1, half_sum - arr[n-1])

    :param arr: Input array
    :param n: Array size, i.e. number of elements
    :param half_sum: sum/2
    :return:
    """
    if half_sum == 0:
        return True

    if n == 0 and half_sum != 0:
        return False

    return is_subset_sum(arr, n-1, half_sum) or is_subset_sum(arr, n-1, half_sum-arr[n-1])


# table[i][j] = table[i][j-1] or table[i - arr[k-1]][j-1]
# https://upload.wikimedia.org/wikipedia/commons/1/10/Partition_Prob_DP_table_example.jpg
def is_subset_sum_dp(arr, n, half_sum):

    rows = half_sum + 1
    cols = n + 1

    table = empty_2d_array(rows, cols)

    # initialize first row as True
    for col in range(0, cols):
        table[0][col] = True

    # initialize first column as False, except table[0][0]
    for row in range(1, rows):
        table[row][0] = False

    for row in xrange(1, rows):
        for col in xrange(1, cols):
            table[row][col] = table[row][col-1] or table[row - arr[col-1]][col-1]

    return table[half_sum][n]


def is_sum_even(arr):
    s = reduce(lambda a, b: a + b, arr)
    return s, s % 2 == 0


if __name__ == "__main__":
    arr = [3, 1, 1, 2, 2, 1, 8]

    sum_and_is_even = is_sum_even(arr)
    sum = sum_and_is_even[0]
    is_even = sum_and_is_even[1]

    print "\n----------------------- Using recursive solution -----------------------\n"
    res = is_even and is_subset_sum(arr, len(arr), sum/2)
    print "Does 2 subsets of equal sum exists?", res

    print "\n----------------------- Using DP solution -----------------------\n"
    res = is_even and is_subset_sum_dp(arr, len(arr), sum / 2)
    print "Does 2 subsets of equal sum exists?", res
