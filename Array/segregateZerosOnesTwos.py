def dutch_national_flag(arr):
    """
    Algorithm - Dutch national flag or three way partitioning
    Lo := 1; Mid := 1; Hi := N;
    while Mid <= Hi do
        Invariant: a[1..Lo-1]=0 and a[Lo..Mid-1]=1 and a[Hi+1..N]=2; a[Mid..Hi] are unknown.
        case a[Mid] in
            0: swap a[Lo] and a[Mid]; Lo++; Mid++
            1: Mid++
            2: swap a[Mid] and a[Hi]; Hi--
    :param arr:
    """
    from Array import swap
    mid = low = 0; high = len(arr) - 1
    while mid <= high:
        curr = arr[mid]
        if curr == 0:
            swap(arr, low, mid)
            low += 1
            mid += 1
        elif curr == 1:
            mid += 1
        else:
            swap(arr, mid, high)
            high -= 1

if __name__ == "__main__":
    arr = [2, 0, 0, 1, 1, 1, 2, 0, 1, 0, 2, 2, 0, 0, 1, 0]
    dutch_national_flag(arr)
    print "Rearranged array: ", arr