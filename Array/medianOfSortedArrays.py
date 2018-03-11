from Array import MIN, MAX

"""
x_arr: x1, x2, |  x3, x4, x5, x6
y_arr: y1, y2, y3, y4, y5, |  y6

where `|` denotes partition, partition(s) must be such that - (x2 <= y6) AND (y5 <= x3) and then median
can be found as -
case-1: len(x_arr) + len(y_arr) is even, then median = avg(max(x2, y5), min(x3, y6))
case-2: len(x_arr) + len(y_arr) is odd, then median = max(x2, y5), because left sub-array will have an extra element.

Time complexity: O(log(size of smaller array))

Algo: 
    x = len(x_arr)
    y = len(y_arr)
    
    Note: x <= y
    
    partition_x + partition_y = (x+y+1)/2
    
    if x_max_left <= y_min_right && y_max_left <= x_min_right:
        if (x+y) is even, then median = avg(max(x2, y5), min(x3, y6))
        elif (x+y) is odd, then median = max(x2, y5), because left sub-array will have an extra element
    elif x_max_left > y_min_right:
        Move towards left in x_arr
    else:
        Move towards right in x_arr
"""
# Time complexity: O(log(size of smaller array))
def find_median(x_arr, y_arr):
    x = len(x_arr)
    y = len(y_arr)
    if x > y:
        x_arr, y_arr = y_arr, x_arr

    median = None
    low = 0; high = x-1

    while low <= high:
        partition_x = (low + high)/2
        # partition_x + partition_y = (x + y + 1) / 2
        partition_y = (x + y + 1)/2 - partition_x

        # If partition_x = 0, means nothing in left sub-array in x_arr after partition, so x_max_left = -INF
        x_max_left = MIN if partition_x == 0 else x_arr[partition_x-1]
        # If partition_x = len(x_arr), means nothing in right sub-array in x_arr after partition, so x_min_right = +INF
        x_min_right = MAX if partition_x == x else x_arr[partition_x]

        # If partition_y = 0, means nothing in left sub-array in y_arr after partition, so y_max_left = -INF
        y_max_left = MIN if partition_y == 0 else y_arr[partition_y - 1]
        # If partition_y = len(y_arr), means nothing in right sub-array in y_arr after partition, so y_min_right = +INF
        y_min_right = MAX if partition_y == y else y_arr[partition_y]

        if x_max_left <= y_min_right and y_max_left <= x_min_right:
            # Found partition(s)
            if (x + y) % 2 == 0:
                # Even length
                median = float(max(x_max_left, y_max_left) + min(x_min_right, y_min_right))/2
            else:
                median = float(max(x_max_left, y_max_left))
            return median
        elif x_max_left > y_min_right:
            # Move towards left in x_arr
            high = partition_x - 1
        else:
            # Move towards right in x+arr
            low = partition_x + 1

if __name__ == '__main__':
    print "\n *********** Test case - 1 ***********\n"
    x_arr = [1, 3, 8, 9, 15]
    y_arr = [7, 11, 19, 21, 18, 25]

    median = find_median(x_arr, y_arr)
    print "x_arr", x_arr
    print "y_arr", y_arr
    print "Median:", median

    print "\n *********** Test case - 2 ***********\n"
    x_arr = [23, 26, 31, 35]
    y_arr = [3, 5, 7, 9, 11, 16]

    median = find_median(x_arr, y_arr)
    print "x_arr", x_arr
    print "y_arr", y_arr
    print "Median: ", median