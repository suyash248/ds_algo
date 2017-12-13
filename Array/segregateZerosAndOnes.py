from Array import swap, print_array

# O(n)
def rearrange_v1(arr):
    """
    Similar to quick sort partition by considering 0 as pivot.
    :param arr:
    :return:
    """
    pivot = 0; ip = -1
    for i in xrange(0, len(arr)):
        if arr[i] <= pivot:
            ip += 1
            swap(arr, i, ip)
    return ip

if __name__ == "__main__":
    arr = [1, 0, 1, 1, 0, 0, 1, 0]
    pivot_index = rearrange_v1(arr)
    zeros_count = pivot_index + 1
    ones_count = len(arr) - zeros_count
    print "0's -> {} & 1's -> {}".format(zeros_count, ones_count)
    print "Rearranged array: ", arr