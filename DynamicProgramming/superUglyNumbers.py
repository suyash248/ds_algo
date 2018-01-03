from Array import empty_1d_array


# Note: Please refer uglyNumbers.py to get better understanding.
def get_kth_ugly_number_dp(k, primes):
    ugly_nums = empty_1d_array(k)
    ugly_nums[0] = 1
    i_primes = empty_1d_array(len(primes), 0)
    next_multiples_of_primes = [p for p in primes]

    for i in xrange(1, k):
        ugly_nums[i] = min(next_multiples_of_primes)
        for j in xrange(0, len(next_multiples_of_primes)):
            if ugly_nums[i] == next_multiples_of_primes[j]:
                i_primes[j] += 1
                next_multiples_of_primes[j] = ugly_nums[i_primes[j]] * primes[j]

    #print ugly_nums
    return ugly_nums[-1]


if __name__ == '__main__':
    primes = map(lambda x: int(x), raw_input("Please enter prime numbers separated via white-space: ").split(" "))
    k = input("To find out 'Kth' ugly number, please enter the value of K: ")
    #primes = [2, 5]

    kth_ugly_num = get_kth_ugly_number_dp(k, primes)
    print "{}th ugly number is:".format(k), kth_ugly_num
