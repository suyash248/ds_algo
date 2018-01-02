from Array import empty_1d_array, MAX


# Time complexity: O(n^2)
def min_jumps(arr):
    n = len(arr)
    path = set()
    jumps = empty_1d_array(n, MAX)
    jumps[0] = 0

    for i in xrange(1, n):
        for j in xrange(0, i):
            if i <= j + arr[j]:                 # Checking if `i` can be reached from `j`
                if jumps[j] + 1 < jumps[i]:
                    jumps[i] = jumps[j] + 1     # jumps[i] = min(jumps[i], jumps[j] + 1)
                    path.add(j)

    path.add(arr[-1])                           # adding last element(destination) to path
    #print jumps, path
    return path


if __name__ == '__main__':
    arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
    path = min_jumps(arr)
    minimum_jumps = len(path) - 1
    path = " -> ".join(map(lambda x: str(x), path))
    print "To reach at the end, at least {} jump(s) are required and path(indices): {}".format(minimum_jumps, path)