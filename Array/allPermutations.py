from copy import deepcopy
from Array import empty_1d_array

def to_str(arr):
    return "".join(arr)


# This solution doesn't take care of duplicates, but if we use Set to store permutations, there will not be duplicate
# permutations.
def all_permutations_v1(arr, l, r):
    if l == r:
        all_permutations_v1.permutations.add(to_str(arr))
    for i in xrange(l, r+1):
        #original_arr = deepcopy(arr)
        arr[l],arr[i] = arr[i],arr[l]
        all_permutations_v1(arr, l+1, r)
        # Backtracking
        arr[i], arr[l] = arr[l], arr[i]
        #arr = original_arr


# This solution takes care of duplicates as well.
# https://www.youtube.com/watch?v=nYFd7VHKyWQ
# Time Complexity: O(2^n)
def all_permutations_v2(input_arr, counts, result, level):
    n = len(input_arr)
    if level == len(result):
        print to_str(result),
        return
    for i in xrange(0, n):
        if counts[i] == 0:
            continue
        result[level] = input_arr[i]
        counts[i] -= 1
        all_permutations_v2(input_arr, counts, result, level+1)
        counts[i] += 1                      # Backtracking


if __name__ == '__main__':
    arr = ["A", "A", "B", "C"]
    print "\n------------ V1 ------------\n"

    all_permutations_v1.permutations = set()    # Using set in order to take care of duplicates.
    all_permutations_v1(arr, 0, len(arr)-1)
    for perm in all_permutations_v1.permutations: print to_str(perm),

    print "\n\n------------ V2 ------------\n"

    ch_counts = {ch : arr.count(ch) for ch in arr}
    all_permutations_v2(ch_counts.keys(), ch_counts.values(),empty_1d_array(len(arr)), 0)
