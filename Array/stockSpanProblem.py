from Array import empty_1d_array

# References - https://www.geeksforgeeks.org/the-stock-span-problem/
def stock_span(prices):
    # Stores index of closest greater element/price.
    stack = [0]
    spans = empty_1d_array(len(prices))

    # Stores the span values, first value(left-most) is 1 as there is no previous greater element(price) available.
    spans[0] = 1

    # When we go from day i-1 to i, we pop the days when the price of the stock was less than or equal to price[i] and
    # then push the value of day i back into the stack.
    for i in range(1, len(prices)):
        cur_price = prices[i]
        while len(stack) != 0 and prices[stack[-1]] <= cur_price:
            stack.pop()

        spans[i] = (i+1) if len(stack) == 0 else (i-stack[-1])
        stack.append(i)
    return spans


if __name__ == '__main__':
    prices = [10, 4, 5, 90, 120, 80]
    spans = stock_span(prices)
    print "Prices:", prices
    print "Spans:", spans