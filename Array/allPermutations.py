from copy import deepcopy


def to_str(arr):
    return "".join(arr)


def perm(arr, l, r):
    if l == r:
        print to_str(arr)
    for i in xrange(l, r+1):
        original_arr = deepcopy(arr)
        arr[l],arr[i] = arr[i],arr[l]
        perm(arr, l+1, r)
        arr = original_arr


if __name__ == '__main__':
    arr = ["A", "B", "C"]
    perm(arr, 0, len(arr)-1)
