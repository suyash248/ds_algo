from Array import swap

# O(n^2)
# Original order of elements will be preserved.
def separate_v1(arr):
    """
    Algorithm: Modified insertion sort -
    for i = 1 to n - 1.
      a) If the current element is +ve, do nothing.
      b) If the current element arr[i] is -ve, we insert it into sequence arr[0..i-1] such that all +ve elements in
         arr[0..i-1] are shifted one position to their right and arr[i] is inserted at index of first +ve element.
    :param arr:
    :return:
    """
    for i in range(0, len(arr)):
        curr = arr[i]
        if curr >= 0:
            continue
        j = i - 1
        while j >= 0 and arr[j] >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = curr

# O(n)
# Original order of elements will NOT be preserved.
def separate_v2(arr):
    # Similar to quick-sort partition.
    ip = -1; pivot = 0
    for i in range(0, len(arr)):
        if arr[i] < pivot:  # if we use `arr[i] <= pivot`, then `0` will be placed somewhere between the -ve numbers.
            ip += 1
            swap(arr, i, ip)

if __name__ == "__main__":
    arr1 = [-2, 1, 0, 9, -8, -4, 8, 2, -7, 7, -6, 5, 4, 12, 14]
    separate_v1(arr1)
    print("Using v1(Orignal ordering)", arr1)

    arr2 = [-2, 1, 0, 9, -8, -4, 8, 2, -7, 7, -6, 5, 4, 12, 14]
    separate_v2(arr2)
    print("Using v2(Random ordering)", arr2)