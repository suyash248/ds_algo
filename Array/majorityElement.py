"""
Algorithm - Moore's voting algorithm
This is a two step process.
1. The first step gives the element that may be majority element in the array. If there is a majority element in
    an array, then this step will definitely return majority element, otherwise it will return any other element.
2. Check/Verify if the element obtained from above step is majority element.This step is necessary as we are not always
    sure that element return by first step is majority element.
"""

# Time complexity: O(n)
def majority_element(arr):
    # Step 1 -> Checking for the candidate of `Majority Element`
    count = 0; majority_index=0
    n = len(arr)
    for i in range(0, n):
        if arr[i] == arr[majority_index]:
            count += 1
        else:
            count -= 1

        if count == 0:
            majority_index = i
            count = 1

    majority_candidate = arr[majority_index]

    # Step 2 -> Verifying whether or not `majority_candidate` is a majority element.
    majority_element = majority_candidate if arr.count(majority_candidate) > n/2 else None
    return majority_element


if __name__ == '__main__':
    arr = [2, 2, 3, 5, 2, 2, 6]
    print majority_element(arr)