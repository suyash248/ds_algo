from Array import empty_2d_array


# Time Complexity : O(2^n)
def knapsack_rec(weights, values, w_limit, n):
    if n == 0 or w_limit == 0:
        return 0

    excl = knapsack_rec(weights, values, w_limit, n-1)

    # If current weight is greater than the weight limit, we can't include it.
    if weights[n-1] > w_limit:
        return excl

    incl = knapsack_rec(weights, values, w_limit - weights[n-1], n-1)

    return max (excl, incl + values[n-1])


# [
#       V          sum of weight (sow)
#   v           w [0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0],
#   a   1       e [0, 1, 1, 1, 1, 1, 1, 1,  1,  1,  1],
#   l   4       i [0, 1, 4, 5, 5, 5, 5, 5,  5,  5,  5],
#   u   4       g [0, 1, 4, 5, 5, 8, 9, 9,  9,  9,  9],
#   e   5       h [0, 1, 4, 5, 5, 8, 9, 10, 10, 13, 14],
#   s   7       t [0, 1, 4, 5, 5, 8, 9, 11, 12, 13, 15]
# ]
def knapsack_dp(weights, values, w_limit):
    n = len(weights)  # Number of items.
    table = empty_2d_array(n+1, w_limit+1)
    for w in xrange(0, n+1):
        for sow in xrange(0, w_limit+1):                            # sow stands for sum of weights
            # Max value we can get is 0 when either of `w` or `sow` is 0. `w` represents current weight.
            if w == 0 or sow == 0:
                table[w][sow] = 0
            elif w > sow:
                table[w][sow] = table[w-1][sow]
            else:
                table[w][sow] = max (
                    table[w-1][sow],                                # excluding the current weight `w`
                    values[w-1] + table[w-1][sow-weights[w-1]]      # including the current weight `w`
                )

    return table[n][w_limit]

if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5] # [10, 20, 30]
    values = [1, 4, 4, 5, 7] # [60, 100, 120]
    w_limit = 10 # 50

    print "\n------- Using recursive approach -------\n"
    max_value = knapsack_rec(weights, values, w_limit, len(weights))
    print max_value

    print "\n------- Using DP approach -------\n"
    max_value = knapsack_dp(weights, values, w_limit)
    print max_value
