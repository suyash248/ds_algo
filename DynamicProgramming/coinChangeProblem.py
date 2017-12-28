from Array import empty_2d_array


def coin_change(coin_max_denomination, max_total_sum):
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
    return table[coin_max_denomination][max_total_sum]


if __name__ == '__main__':
    max_total_sum = 5
    coin_max_denomination = 5
    ways =  coin_change(coin_max_denomination, max_total_sum)
    print "There are {} ways to get the total of {} by using coins of denomination from 0 to {}".format(ways, max_total_sum, coin_max_denomination)