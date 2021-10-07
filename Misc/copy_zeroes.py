"""
Array having random numbers: 0-9

For each 0 in the list, add one more 0 next to it and and righ shift
all the values after the 0. Discard the last value so that the list size
remains unchanged.

Input:  [1, 0, 7, 3, 0, 9, 5, 0, 1]
Output: [1, 0, 0, 7, 3, 0, 0, 9, 5]
"""
from typing import List


def copy_zeroes(input: List[int]) -> List[int]:
    output = []
    l = len(input)
    ip_idx = 0
    while len(output) < l:
        if input[ip_idx] == 0:
            output.append(0)
        output.append(input[ip_idx])
        ip_idx += 1
    return output

if __name__ == '__main__':
    input = [1, 0, 7, 3, 0, 9, 5, 0, 1]
    output = copy_zeroes(input)
    print(output)


