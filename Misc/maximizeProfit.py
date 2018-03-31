import random

# Given an array containing stock prices in increasing order of time. For example -
# price1 = arr[2], price2 = arr[7]
# price1 is the price at time t1 & price2 is the price at time t2. And t1 < t2
# Item can be bought and sold. It must be bought first then only it can be sold.
# When should one buy & when to sell in order to maximize the profit.

def maximize_profit(prices):
    """
    Algorithm:
        1. Find MINIMUM price in whole array (0 to `len - 1`), say, `min_price` at index `i_min`.
            Now find MAXIMUM price in array segment (`i_min + 1` to `len - 1`), say, `max_price` at index `i_max`,
            profit1 = arr[i_max] - arr[i_min]
        1. Find MAXIMUM price in whole array (0 to `len - 1`), say, `max_price` at index `i_max`.
            Now find MINIMUM price in array segment (0 to `i_max - 1`), say, `min_price` at index `i_min`,
            profit2 = arr[i_max] - arr[i_min]
        max_profit = max(profit1, profit2)
    :param prices: Array containing prices of item at different instances(increasing order of time).
    :return: Tuple containing maximum profit, buy_index(when to buy) & sell_index(when to sell).
    """

    from Array import min_in_subarray, max_in_subarray

    min_price1, i_min1 = min_in_subarray(prices)
    max_price1, i_max1 = max_in_subarray(prices, start=i_min1+1, end=len(prices))
    profit1 = max_price1 - min_price1

    max_price2, i_max2 = max_in_subarray(prices)
    min_price2, i_min2 = min_in_subarray(prices, start=0, end=i_max2) # end is exclusive
    profit2 = max_price2 - min_price2

    if profit1 > profit2:
        return {
            "max_profit": profit1,
            "buy": {
                "index": [i_min1],
                "price": [min_price1]
            },
            "sell": {
                "index": [i_max1],
                "price": [max_price1]
            }
        }
    if profit1 < profit2:
        return {
            "max_profit": profit2,
            "buy": {
                "index": [i_min2],
                "price": [min_price2]
            },
            "sell": {
                "index": [i_max2],
                "price": [max_price2]
            }
        }
    else:
        return {
            "max_profit": profit1,
            "buy": {
                "index": [i_min1, i_min2],
                "price": [min_price1, min_price2]
            },
            "sell": {
                "index": [i_max1, i_max2],
                "price": [max_price1, max_price2]
            }
        }
if __name__ == '__main__':
    currency = "INR"
    #prices = [2, 11, 10, 6, 9, 7, 16, 8, 3, 4, 14, 1, 10, 2]
    #prices = [random.randint(1, 2000) for x in range(0, 1000000)]
    prices = [5, 4, 3, 2, 1]
    res = maximize_profit(prices)
    print """Maximum profit is {max_profit}, 
    Buy at price {currency} {buy_price} at index/time {buy_index}.
    Sell at price {currency} {sell_price} at index/time {sell_index}
    """.format(max_profit=res['max_profit'], currency=currency,
                       buy_price=res['buy']['price'], buy_index=res['buy']['index'],
                       sell_price=res['sell']['price'], sell_index=res['sell']['index'])