# Time complexity: O(2^n)
# Space complexity: O(n)
def is_subset_sum(arr, n, half_sum):
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

