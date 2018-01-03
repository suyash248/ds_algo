from Array import empty_1d_array

# What is ugly number?
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,
# shows the first 11 ugly numbers. By convention, 1 is included.

# Problem: To find out `Kth` ugly number.


def max_divisible(a, b):
    """
    Keep dividing(a/b) till it's divisible(a % b == 0)
    e.g.
    Input: a = 300; b = 2
    Output: 75

    :param a:
    :param b:
    :return:
    """
    while a % b == 0:
        a = a / b
    return a


def is_ugly(num):
    num = max_divisible(num, 2)
    num = max_divisible(num, 3)
    num = max_divisible(num, 5)
    return num == 1


def get_kth_ugly_number(k):
    """
    Algorithm -

    Loop for all positive integers until ugly number count is smaller than `n`, if an integer is ugly than increment
    ugly number count.
    To check if a number is ugly, divide the number by greatest divisible powers of 2, 3 and 5, if the number becomes 1
    then it is an ugly number otherwise not.

    For example, let us see how to check for 300 is ugly or not. Greatest divisible power of 2 is 4, after dividing 300 by 4 we get 75. Greatest divisible power of 3 is 3, after dividing 75 by 3 we get 25. Greatest divisible power of 5 is 25, after dividing 25 by 25 we get 1. Since we get 1 finally, 300 is ugly number.
    :param k:
    :return:
    """
    count = 0; i = 0
    while count < k:
        i += 1
        if is_ugly(i):
            count += 1
    return i


def get_kth_ugly_number_dp(k):
    ugly_nums = empty_1d_array(k)
    ugly_nums[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in xrange(1, k):
        ugly_nums[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        if ugly_nums[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly_nums[i2] * 2
        if ugly_nums[i] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly_nums[i3] * 3
        if ugly_nums[i] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly_nums[i5] * 5

    #print ugly_nums
    return ugly_nums[-1]


if __name__ == '__main__':
    k = input("To find out 'Kth' ugly number, please enter the value of K: ")
    kth_ugly_num = get_kth_ugly_number(k)

    print "\n------- Using iterative approach -------\n"
    print "{}th ugly number is:".format(k), kth_ugly_num

    print "\n------- Using DP -------\n"
    kth_ugly_num = get_kth_ugly_number_dp(k)
    print "{}th ugly number is:".format(k), kth_ugly_num
