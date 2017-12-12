def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# O(n)
def left_rotate_v1(arr, d):
    n = len(arr)
    g = gcd(n, d)

    for i in xrange(0, g):
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

#O(n)
def left_rotate_v2(arr, d):
    """
    Algorithm -
        For arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2 and n = 7
        A = [1, 2] and B = [3, 4, 5, 6, 7]
        Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
        Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
        Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]

    :param arr:
    :param d:
    :return:
    """
    n = len(arr)
    from reverse import reverse_arr
    reverse_arr(arr, 0, d-1)
    reverse_arr(arr, d, n-1)
    reverse_arr(arr, 0, n-1)

# O(nd)
def left_rotate_v3(arr, d):
    from Array import swap
    n = len(arr)
    for di in xrange(0, d):
        first = arr[0]
        for i in xrange(1, n):
            swap(arr, i, i-1)
        arr[n-1] = first

if __name__ == "__main__":
    from copy import deepcopy
    d = 2
    arr = [1, 2, 3, 4, 5, 6, 7]
    arr_dup1 = deepcopy(arr)
    arr_dup2 = deepcopy(arr)

    print arr

    print "\n---- Using V1 ----\n"
    left_rotate_v1(arr, d)
    print arr

    print "\n---- Using V2 ----\n"
    left_rotate_v2(arr_dup1, d)
    print arr_dup1

    print "\n---- Using V3 ----\n"
    left_rotate_v3(arr_dup2, d)
    print arr_dup2