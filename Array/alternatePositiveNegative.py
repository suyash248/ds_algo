def rearrange_v1(arr):
    from Array import swap

    # Partitioning array same as quick sort partition by taking 0 as pivot so that all the -ve numbers
    # will be at left and +ve numbers will be at right.
    pindex = -1; pivot = 0
    for i in xrange(0, len(arr)):
        if arr[i] < pivot:
            pindex += 1
            swap(arr, i, pindex)

    print pindex
    print arr
    # Since -ve and +ve numbers are separated, we start from the first -ve number and first +ve number,
    # and swap every alternate negative number with next positive number
    i_pos = pindex + 1
    for i in xrange(0, len(arr), 2):
        if i_pos >= len(arr) or arr[i] > 0:
            break
        swap(arr, i, i_pos)
        i_pos += 1

if __name__ == "__main__":
    arr = [-2, 1, 0, 9, -8, -4, 8, 2, -7, 7, -6, 5, 4, 12, 14]
    rearrange_v1(arr)
    print arr