def max_and_min_product_subarray(arr):
    """
    Assumption: Output is alway greater than or equal to 1.
    :param arr:
    :return:
    """
    curr_max = curr_min = global_max = global_min = 1
    for elt in arr:

        # If this element is positive, update curr_max.
        # Update curr_min only if curr_min is negative
        if elt > 0:
            curr_max = curr_max * elt
            curr_min = min(curr_min * elt, 1)
        elif elt < 0:
            prev_max = curr_max
            curr_max = max(curr_min * elt, 1)
            curr_min = prev_max * elt

        # If this element is 0, then the maximum product can't end here, make both curr_max and curr_min 0
        # Assumption: Output is always greater than or equal to 1.
        else:
            curr_max, curr_min = 1,1

        if curr_max > global_max:
            global_max = curr_max
        if curr_min < global_min:
            global_min = curr_min
    return global_max, global_min

if __name__ == "__main__":
    arr = [1, 0, -4, -2, 2, 3, -2]
    max_n_min = max_and_min_product_subarray(arr)
    print "Product of max-product-sub-array is {} & product of min-product-sub-array is {}".format(*max_n_min)
