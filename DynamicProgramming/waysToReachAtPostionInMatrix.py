from Array import empty_2d_array

"""
[
        0  1  2   3   4
   0  [ 1, 1, 1,  1,  1 ]
   1  [ 1, 2, 3,  4,  5 ]
   2  [ 1, 3, 6,  10, 15]
   3  [ 1, 4, 10, 20, 35]
]

"""
def ways_to_reach_position(rows, cols, position=(0, 0)):
    table = empty_2d_array(rows, cols, fill_default=0)

    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0:
                table[row][col] = 1
                continue
            table[row][col] = table[row-1][col] + table[row][col-1]

    #print table
    return table[position[0]][position[1]]

if __name__ == '__main__':
    rows = 4
    cols = 5
    position = (3, 4)
    num_ways = ways_to_reach_position(rows, cols, position)
    print ("Number of ways to reach {} from (0, 0) are - {}".format(position, num_ways))