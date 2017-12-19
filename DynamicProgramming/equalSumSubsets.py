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



def is_sum_even(arr):
    s = reduce(lambda a, b: a + b, arr)
    return s, s%2 == 0


if __name__ == "__main__":
    arr = [3, 1, 1, 2, 2, 1, 8]

    sum_and_is_even = is_sum_even(arr)
    sum = sum_and_is_even[0]
    is_even = sum_and_is_even[1]

    res = is_even and is_subset_sum(arr, len(arr), sum/2)
    print "Does 2 subsets of equal sum exists?", res

