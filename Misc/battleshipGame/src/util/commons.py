def to_index(c):
    """
    Returns the sequence/index corresponding to a character. e.g. A -> 1, B -> 2
    :param c:
    :return:
    """
    index = 0
    if type(c) == str:
        if c.isupper():
            index = ord(c) - 64
        else:
            index = ord(c) - 96
    return index

def get_battlearea_location(alphanumeric_loc):
    """
    Converts `alphanumeric` location/co-ordinates to matrix indices. e.g. B4 -> (4, 4)
    :param alphanumeric_loc:
    :return: tuple of matrix index
    """
    return (to_index(alphanumeric_loc[0]), int(alphanumeric_loc[1]))

def empty_1d_array(size, fill_default=None):
    """
    Create and return 1-D array
    :param size:
    :param fill_default: Default value to be filled in cells.
    :return:
    """
    return [fill_default] * size

def empty_2d_array(rows, cols, fill_default=None):
    """
    Create and return 2-D array
    :param size:
    :param fill_default: Default value to be filled in cells.
    :return:
    """
    arr_2d = []
    for row in xrange(0, rows):
        col_arr = empty_1d_array(cols, fill_default)
        arr_2d.append(col_arr)
    return arr_2d