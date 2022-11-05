from typing import List, Any

def print_subsequences(arr: List[Any], i = 0, sub = ""):
    if i >= len(arr):
        print(sub)
        return
    print_subsequences(arr, i + 1, sub)
    # sub.append(arr[i])
    sub += arr[i]
    print_subsequences(arr, i + 1, sub)
    # sub.remove(arr[i])

if __name__ == '__main__':
    print_subsequences(['a', 'b', 'c'])