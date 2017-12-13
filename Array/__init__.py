def print_array(arr, start=-1, end=-1):
    """
    :param arr: Source array to be printed.
    :param start: OPTIONAL: start index (inclusive), 0 if not given or if given value is greater than equals to len(arr)
    :param end: OPTIONAL: end index (inclusive), len(arr)-1 if not given or if given value is greater than equals to len(arr)
    """
    alen = len(arr)
    start = 0 if start < 0 or start >= alen else start
    end = alen if end < 0 or end >= alen else end
    for i in range(start, end):
        print arr[i],

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp