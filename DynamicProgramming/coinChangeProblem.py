from Array import empty_2d_array


"""
max_total_sum = 5
coins = [2, 3]

[       
        0  1  2  3  4  5
 C   0 [1, 0, 0, 0, 0, 0], 
 2   1 [1, 0, 1, 0, 1, 0], 
 3   2 [1, 0, 1, 1, 1, 1]
]
"""
def coin_change(coins, max_total_sum):
    """
    Formulae - table[row][col] = table[row-1][col] + table[row][col-row], Where `row` denotes `coin`, `col` denotes `sum`.
    :param coin_max_denomination:
    :param max_total_sum:
    :return:
    """
    rows = len(coins) + 1
    cols = max_total_sum + 1
    table = empty_2d_array(rows, cols)

    # Number of ways to get the total_sum = 0 by using coin(s) of denomination [0] is 1.
    table[0][0] = 1

    # Number of ways to get the total_sum(>0) by using coin(s) of denomination [0] is 0.
    for first_row_elt in xrange(1, max_total_sum+1):
        table[0][first_row_elt] = 0

    for i_coin in xrange(1, rows):
        for s in xrange(0, cols):
            coin_val = coins[i_coin-1]
            excl_coin = table[i_coin-1][s]
            if coin_val > s:
                table[i_coin][s] = excl_coin
            else:
                incl_coin = table[i_coin][s - coin_val]
                table[i_coin][s] = excl_coin + incl_coin
    #print table
    return table[rows-1][cols-1]


if __name__ == '__main__':
    max_total_sum = 5
    coins = [2, 3]
    ways =  coin_change(coins, max_total_sum)
    print "There is/are {} way(s) to get the total of {} by using coins {}".format(ways, max_total_sum, coins)