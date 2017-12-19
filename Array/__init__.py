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
    return [fill_default] *  size


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