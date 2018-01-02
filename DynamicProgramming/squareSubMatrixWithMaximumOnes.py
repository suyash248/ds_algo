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
def square_sub_matrix_with_max_ones(matrix=[]):
    """
    Algorithm -
    1) Construct a sum matrix S[R][C] for the given M[R][C]. And initialize max_size, max_i, max_j to 0.
         a) Copy first row and first columns as it is from M[][] to S[][]
         b) For other entries, use following expressions to construct S[][]
            If M[i][j] is 1 then
                S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
            Else If M[i][j] is 0
                S[i][j] = 0
        c) Update max_size, max_i, max_j (if required) as follows -
            If S[i][j] > max_size:
                max_size = S[i][j]
                max_i = i; max_j = j
    2) Using the max_size and coordinates(max_i, max_j) of maximum entry in S[i], print sub-matrix of M[][]
    :param matrix:
    :return:
    """
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


def print_square_sub_matrix_with_max_ones(matrix, max_size, coordinates):
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
    max_sub_matrix_info = square_sub_matrix_with_max_ones(matrix)
    max_size = max_sub_matrix_info[0]
    coordiantes = max_sub_matrix_info[1]
    print "Sub-matrix of 1's with maximum size {max_size} is - ".format(max_size=max_size)
    print_square_sub_matrix_with_max_ones(matrix, max_size, coordiantes)