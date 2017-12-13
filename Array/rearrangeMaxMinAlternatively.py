# Time complexity : O(n)
# Space complexity : O(n)
def rearrange_max_min(arr):
    """
    Algorithm: Use an auxiliary array. Maintain two pointers one to leftmost or smallest element and other to rightmost
    or largest element. We more both pointers toward each other and alternatively copy elements at these pointers to an
    auxiliary array.
    :param arr:
    :return: Rearranged array.
    """
    aux_arr = [None] * len(arr)
    flag = True; low = 0; high = len(arr) - 1
    for i in range(0, len(arr)):
        if flag:
            aux_arr[i] = arr[high]
            high -= 1
        else:
            aux_arr[i] = arr[low]
            low += 1
        flag = not flag
    return aux_arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    arr = rearrange_max_min(arr)
    print arr