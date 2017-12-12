def count_pair(arr, sum):
    hm = dict()
    for elt in arr:
        hm[elt] = hm.get(elt, 0) + 1

    count = 0
    for elt in arr:
        remaining = sum - elt
        count += hm.get(remaining, 0)
    return count/2

if __name__ == "__main__":
    arr = [7, 5, 1, -1, 5]
    sum = 6
    pair_count = count_pair(arr, sum)
    print "Number of pair(s) with sum equals to {sum} is {pair_count}".format(sum=sum, pair_count=pair_count)