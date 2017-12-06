def total_trees(n):
    list = [0] * (n+1)
    list[0] = list[1] = 1
    for i in xrange(2, n+1):                    # for i=2 to i<=n
        for j in xrange(i):                         # for j=0 to j<i
            list[i] += list[j] * list[i-j-1]
    return list[n]

if __name__ == "__main__":
        n = 4
        count = total_trees(n)
        print "Total {count} tree(s) can be formed with {n} distinct keys".format(count=count, n=n)