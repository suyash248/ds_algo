import sys

MAX = sys.maxint
MIN = 1 - MAX

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
    arr[i], arr[j] = arr[j], arr[i]


def empty_1d_array(size, fill_default=None):
    return [fill_default] * size


def empty_2d_array(rows, cols, fill_default=None):
    """
    Caution: If we will use - [[None * cols]] * rows, then all the columns will have same reference and changing a column
            will reflect to all the columns. So it's better to have separate inner-array for each column.
    :param rows:
    :param cols:
    :param fill_default:
    :return:
    """
    arr_2d = []
    for row in xrange(0, rows):
        col_arr = empty_1d_array(cols, fill_default)
        arr_2d.append(col_arr)
    return arr_2d

def max_in_subarray(arr, start=0, end=None):
    """
    Finds max element within a segment(start to end) of `arr`
    :param arr:
    :param start: Starting point of segment (Inclusive)
    :param end: Ending point of segment (Exclusive)
    :return: max element in segment along with index as tuple.
    """
    if end is None:
        end = len(arr)

    max_so_far = MIN
    i_max_so_far = -1
    for i in xrange(start, end):
        if arr[i] > max_so_far:
            max_so_far, i_max_so_far = arr[i], i
    return max_so_far, i_max_so_far

def min_in_subarray(arr, start=0, end=None):
    """
    Finds min element within a segment(start to end) of `arr`
    :param arr:
    :param start: Starting point of segment (Inclusive)
    :param end: Ending point of segment (Exclusive)
    :return: min element in segment along with index as tuple.
    """
    if end is None:
        end = len(arr)

    min_so_far = MAX
    i_min_so_far = -1
    for i in xrange(start, end):
        if arr[i] < min_so_far:
            min_so_far, i_min_so_far = arr[i], i
    return min_so_far, i_min_so_far