def rearrange_v1(arr):
    """
    Algorithm: Modified insertion sort -
    for i = 1 to n - 1.
      a) If the current element is +ve, do nothing.
      b) If the current element arr[i] is -ve, we insert it into sequence arr[0..i-1] such that all +ve elements in
         arr[0..i-1] are shifted one position to their right and arr[i] is inserted at index of first +ve element.
    :param arr:
    :return:
    """
    from Array import swap
    for i in xrange(0, len(arr)):
        curr = arr[i]
        if curr >= 0:
            continue
        j = i - 1
        while j >= 0 and arr[j] >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr

if __name__ == "__main__":
    arr = [-2, 1, 0, 9, -8, -4, 8, 2, -7, 7, -6, 5, 4, 12, 14]
    rearrange_v1(arr)
    print arr