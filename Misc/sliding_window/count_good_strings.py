'''
A string is good if there are no repeated characters.

Given a string s and integer k, return the number of good substrings of length k in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "xyzzaz", k = 3
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc", k = 3
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".


Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.
'''
from typing import List


def count_good_strings(chars: List[str], k: int) -> int:
    l, gc, r = 0, 0, k
    substr = dict()
    for i in range(min(k, len(chars))):
        substr[chars[i]] = substr.get(chars[i], 0) + 1
    if len(substr) == k:
        gc += 1

    while r < len(chars):
        substr[chars[r]] = substr.get(chars[r], 0) + 1
        if substr[chars[l]] > 1:
            substr[chars[l]] -= 1
        else:
            substr.pop(chars[l])

        if len(substr) == k:
            gc += 1

        r += 1
        l += 1
    return gc


def brute_force(chars: List[str], k: int) -> int:
    gc = 0
    for i in range(len(chars)):
        sub_str = chars[i: i + k]
        if len(set(sub_str)) == 3:
            gc += 1
    return gc


if __name__ == '__main__':
    k = 3
    chars = ['a', 'a', 'b', 'a', 'b', 'c', 'a', 'b', 'c']  # ['a', 'b', 'c', 't']

    gc = count_good_strings(chars, k)
    print(chars, gc)

    gc = brute_force(chars, k)
    print(chars, gc)

    chars = ['o', 'w', 'u', 'x', 'o', 'e', 'l', 's', 'z', 'b']
    gc = count_good_strings(chars, k)
    print(chars, gc)

    gc = brute_force(chars, k)
    print(chars, gc)

    chars = ['x']
    gc = count_good_strings(chars, k)
    print(chars, gc)

    gc = brute_force(chars, k)
    print(chars, gc)
