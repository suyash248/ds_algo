from Array import empty_2d_array

"""
prices = [2, 5, 9, 6]
rod_len = 5
[
                0  1  2  3  4   5    (rod_len)
    0        0 [0, 0, 0, 0, 0,  0], 
    2        1 [0, 2, 4, 6, 8,  10], 
    5        2 [0, 2, 5, 7, 10, 12], 
    9        3 [0, 2, 5, 9, 11, 14], 
    6        4 [0, 2, 5, 9, 11, 14]
 (profit)  (pcs)
]
"""
def max_profit_dp(prices, rod_len):
    rows = len(prices) + 1; cols = rod_len + 1
    table = empty_2d_array(rows, cols)

    for piece_len in xrange(0, rows):
        for r_len in xrange(0, cols):
            if piece_len == 0 or r_len == 0:
                table[piece_len][r_len] = 0
                continue

            excl = table[piece_len-1][r_len]
            if piece_len > r_len:
                table[piece_len][r_len] = excl
            else:
                incl = prices[piece_len-1] + table[piece_len][r_len-piece_len]
                table[piece_len][r_len] = max(excl, incl)

    print table
    return table[rows-1][cols-1]

if __name__ == '__main__':
    prices = [2, 5, 9, 6]
    rod_len = 5
    max_profit = max_profit_dp(prices, rod_len)
    print "Maximum profit - {}".format(max_profit)