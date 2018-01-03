# What is ugly number?
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,
# shows the first 11 ugly numbers. By convention, 1 is included.

# Problem: To find out `Kth` ugly number.


def max_divisible(a, b):
    while a % b == 0:
        a = a / b
    return a


def is_ugly(num):
    num = max_divisible(num, 2)
    num = max_divisible(num, 3)
    num = max_divisible(num, 5)
    return num == 1


def get_kth_ugly_number(k):
    count = 0; i = 0
    while count < k:
        i += 1
        if is_ugly(i):
            count += 1
    return i


# TODO - Implement it using DP.
def get_kth_ugly_number_dp(k):
    pass


if __name__ == '__main__':
    k = input("To find out 'Kth' ugly number, please enter the value of K: ")
    kth_ugly_num = get_kth_ugly_number(k)
    print "{}th ugly number is:".format(k), kth_ugly_num
