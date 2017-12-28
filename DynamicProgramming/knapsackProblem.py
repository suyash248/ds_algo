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


if __name__ == '__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]
    w_limit = 50
    max_value = knapsack_rec(weights, values, w_limit, len(weights))
    print max_value
