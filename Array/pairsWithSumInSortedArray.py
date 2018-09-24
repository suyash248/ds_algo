def find_pair(arr, sum):
    start = 0
    end = len(arr)-1
    pairs = []
    while start < end:
        curr_sum = arr[start] + arr[end]
        if curr_sum < sum:
            start += 1
        elif curr_sum > sum:
            end -= 1
        else:
            # print("({}, {})".format(arr[start], arr[end]))
            pairs.append((arr[start], arr[end]))
            start += 1
            end -= 1
    return pairs

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    sum = 7
    pairs = find_pair(arr, sum)
    print("Pair(s) with sum equals to {sum} are {pairs}".format(sum=sum, pairs=pairs))