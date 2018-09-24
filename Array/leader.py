from Array import MIN

def leader(arr):
    n = len(arr)
    max_so_far = MIN
    for elt in arr[::-1]:  # for i=n-1 to 0
        if elt > max_so_far:
            print(elt, end=',')
            max_so_far = elt

if __name__ == '__main__':
    arr = [15, 16, 3, 2, 6, 1, 4]
    leader(arr)