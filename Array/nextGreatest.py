def next_greatest(arr):
    n = len(arr)
    max_so_far = arr[-1]                                    # Last element
    print "{} -> {}".format(max_so_far, max_so_far)
    for i in range(n-2, -1, -1):                            # for i=n-2 to 0
        cur_elt = arr[i]
        if max_so_far > cur_elt:
            print "{} -> {}".format(cur_elt, max_so_far)
        else:
            print "{} -> {}".format(cur_elt, cur_elt)
            max_so_far = cur_elt

def replace_with_next_greatest(arr):
    n = len(arr)
    max_so_far = arr[-1]            # Last element
    for i in range(n-2, -1, -1):    # for i=n-2 to 0
        cur_elt = arr[i]
        if max_so_far > cur_elt:
            arr[i] = max_so_far
        else:
            max_so_far = cur_elt

if __name__ == '__main__':
    arr = [3, 4, 20, 6, 15, 2, 1, 7]
    next_greatest(arr)

    print "\nAfter replacing every element with it's next greatest element - \n"
    replace_with_next_greatest(arr)
    print arr