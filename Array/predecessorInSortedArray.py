from Array import MAX
def predecessor(arr, key, low, high):
    if high < low:
        return None
    mid = (low + high)/2

    if key == arr[mid] and mid > 0:
        return arr[mid-1]
    prev = arr[mid-1] if mid > 0 else -1            # previous element to mid
    next = arr[mid+1] if mid < len(arr)-1 else MAX  # next element to mid

    if key > prev and key < next and arr[mid] <key:
        return arr[mid]

    if key < arr[mid]:
        return predecessor(arr, key, low, mid-1)
    else:
        return predecessor(arr, key, mid+1, high)

if __name__ == '__main__':
    arr = [2, 3, 5, 9, 12, 15, 17, 20, 25, 30, 35]
    key = 20
    pred = predecessor(arr, key, 0, len(arr)-1)
    print(pred)
