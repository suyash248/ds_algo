from Array import empty_2d_array


# [       s u m
#      c [1, 0, 0, 0, 0, 0],
#      o [1, 1, 1, 1, 1, 1],
#      i [1, 1, 2, 2, 3, 3],
#      n [1, 1, 2, 3, 4, 5],
#      s [1, 1, 2, 3, 5, 6],
#        [1, 1, 2, 3, 5, 7]
# ]
def coin_change(coin_max_denomination, max_total_sum):
    """
    Formulae - table[row][col] = table[row-1][col] + table[row][col-row], Where `row` denotes `coin`, `col` denotes `sum`.
    :param coin_max_denomination:
    :param max_total_sum:
    :return:
    """
    table = empty_2d_array(coin_max_denomination+1, max_total_sum+1)

    # Number of ways to get the total_sum = 0 by using coin(s) of denomination [0] is 1.
    table[0][0] = 1

    # Number of ways to get the total_sum(>0) by using coin(s) of denomination [0] is 0.
    for first_row_elt in xrange(1, max_total_sum+1):
        table[0][first_row_elt] = 0

    for coin in xrange(1, coin_max_denomination+1):
        for s in xrange(0, max_total_sum+1):
            excl_coin = table[coin-1][s]
            if coin > s:
                table[coin][s] = excl_coin
            else:
                incl_coin = table[coin][s - coin]
                table[coin][s] = excl_coin + incl_coin
    print table
    return table[coin_max_denomination][max_total_sum]


if __name__ == '__main__':
    max_total_sum = 5
    coin_max_denomination = 5
    ways =  coin_change(coin_max_denomination, max_total_sum)
    print "There are {} ways to get the total of {} by using coins of denomination from 0 to {}".format(ways, max_total_sum, coin_max_denomination)