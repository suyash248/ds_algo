from Array import empty_1d_array

def fib_rec(n):
    """
    Series - 1, 1, 2, 3, 5, 8, 13
    `n` starts from 0.
    :param n:
    :return:
    """
    if n < 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def fib_dp(n):
    """
    Series - 1, 1, 2, 3, 5, 8, 13
    `n` starts from 0.
    :param n:
    :return:
    """
    fib_arr = empty_1d_array(n)
    if n < 2:
        return 1
    if fib_arr[n-1] is None:
        fib_arr[n-1] = fib_rec(n-1)
    if fib_arr[n-2] is None:
        fib_arr[n-2] = fib_rec(n-2)

    return fib_arr[n-1] + fib_arr[n-2]

def fib_itr(n):
    """
    Series - 1, 1, 2, 3, 5, 8, 13
    `n` starts from 1.
    :param n:
    :return:
    """
    if n < 2:
        return 1
    a = b = 1
    for i in range(2, n):
        a, b = b, a+b
    return b

if __name__ == '__main__':
    n = 6

    # As `n` starts from 0 in case of recursive versions. so n-1 is passed as an argument.
    print fib_rec(n-1)
    print fib_dp(n-1)

    print fib_itr(n)
