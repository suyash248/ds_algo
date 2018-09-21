from math import sqrt, ceil

def is_prime(n):
    till = int(ceil(sqrt(n)))
    for i in range(2, till):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = input("Enter number - ")
    res = is_prime(n)
    print("{} is {}".format(n, "prime" if res else "not prime"))