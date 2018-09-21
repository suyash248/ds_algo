def fact_rec(n):
    if n <= 1: return 1
    return n * fact_rec(n-1)

def fact_itr(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

if __name__ == '__main__':
    print (fact_rec(5))
    print (fact_itr(5))