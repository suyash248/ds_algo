def reverse_arr(arr, start=0, end=-1):
    from Array import swap
    alen = len(arr)
    end = (alen-1) if end <0 else end

    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    reverse_arr(arr)
    print arr