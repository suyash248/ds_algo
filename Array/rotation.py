def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def left_rotate_v1(arr, d):
    n = len(arr)
    g = gcd(n, d)

    for i in xrange(0, g+1):
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    left_rotate_v1(arr, d)
    print arr