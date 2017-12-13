from Array import swap

# O(n)
def segregate_v1(arr):
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

def segregate_v2(arr):
    start = 0; end = len(arr) - 1
    mid = (start + end)/2

    while start < end:
        if arr[mid] == 0:
            swap(arr, mid, start)
            start += 1
        elif arr[mid] == 1:
            swap(arr, mid, end)
            end -= 1


# O(log(n))
if __name__ == "__main__":
    from copy import deepcopy

    arr = [1, 0, 1, 1, 0, 0, 1, 0]
    arr_copy = deepcopy(arr)

    print "\n ---- Using V1 ---- \n"
    pivot_index = segregate_v1(arr)
    zeros_count = pivot_index + 1
    ones_count = len(arr) - zeros_count
    print "0's -> {} & 1's -> {}".format(zeros_count, ones_count)
    print "Rearranged array: ", arr

    print "\n ---- Using V2 ---- \n"
    segregate_v2(arr_copy)
    print "Rearranged array: ", arr_copy
