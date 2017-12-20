def max_sum_subarray(arr):
    curr_max = global_max = 0
    for elt in arr:
        curr_max = curr_max + elt
        if curr_max < 0:
            curr_max = 0
        if curr_max > global_max:
            global_max = curr_max

    return global_max


if __name__ == "__main__":
    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    global_max = max_sum_subarray(arr)
    print "Max sum :", global_max