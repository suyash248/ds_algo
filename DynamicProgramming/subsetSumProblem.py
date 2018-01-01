from Array import empty_2d_array


"""
elt_set = [2, 4, 1]
total_sum = 3
    
[
        i  0  1  2  3   (sum)
        0 [T, F, F, F], 
    2   1 [T, F, T, F], 
    4   2 [T, F, T, F], 
    1   3 [T, T, T, T]
  (elt) 
]
"""
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def subset_sum_dp(elt_set, total_sum):
    rows = len(elt_set) + 1; cols = total_sum + 1
    table = empty_2d_array(rows, cols)

    # Set each cell in first col as `True`, because total_sum = 0  can be formed if we have 0 in subset.
    for row in xrange(0, rows):
        table[row][0] = True

    # Except (0, 0), set each cell in first row as `False`, because using subset {0} we can't form total_sum>0
    for col in xrange(1, cols):
        table[0][col] = False

    for i_elt in xrange(1, rows):
        for s in xrange(1, cols):
            elt = elt_set[i_elt-1]
            excl_elt = table[i_elt-1][s]

            # If current elt > current sum, we can't include current elt in subset.
            if elt > s:
                table[i_elt][s] = excl_elt
            else:
                incl_elt = table[i_elt-1][s-elt]
                table[i_elt][s] = excl_elt or incl_elt

    #print table
    return table[rows-1][cols-1]

if __name__ == '__main__':
    elt_set = [2, 4, 1]
    total_sum = 3
    res = subset_sum_dp(elt_set, total_sum)
    print "Can we form a subset having sum {}? - {}".format(total_sum, res)