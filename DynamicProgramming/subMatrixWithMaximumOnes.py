from Array import empty_2d_array

"""
sum sub-matrix ->
[
    [0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0], 
    [1, 1, 2, 2, 0], 
    [1, 2, 2, 3, 1], 
    [0, 0, 0, 0, 0]
]
"""
def sub_matrix_with_max_ones(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Sum matrix
    sum_matrix = empty_2d_array(rows, cols)
    max_i = max_j = max_size = 0

    for row in xrange(0, rows):
        for col in xrange(0, cols):

            # Copy first row & first col as it is from `matrix` to `sum_matrix`.
            if row == 0 or col == 0:
                sum_matrix[row][col] = matrix[row][col]
                continue
            elif matrix[row][col] == 1:
                sum_matrix[row][col] = min(sum_matrix[row][col-1], sum_matrix[row-1][col], sum_matrix[row-1][col-1]) + 1
            elif matrix[row][col] == 0:
                sum_matrix[row][col] = 0

            if sum_matrix[row][col] > max_size:
                max_size = sum_matrix[row][col]
                max_i = row
                max_j = col

    #print sum_matrix
    return max_size, (max_i, max_j)


def print_sub_matrix_with_max_ones(matrix, max_size, coordinates):
    max_i = coordinates[0]; max_j = coordinates[1]

    for i in xrange(max_i, max_i-max_size, -1):
        for j in xrange(max_j, max_j-max_size, -1):
            print matrix[i][j],
        print

if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    max_sub_matrix_info = sub_matrix_with_max_ones(matrix)
    max_size = max_sub_matrix_info[0]
    coordiantes = max_sub_matrix_info[1]
    print "Sub-matrix of 1's with maximum size {max_size} is - ".format(max_size=max_size)
    print_sub_matrix_with_max_ones(matrix, max_size, coordiantes)