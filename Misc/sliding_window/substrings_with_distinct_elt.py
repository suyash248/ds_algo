'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3:

Input: s = "abc"
Output: 1


Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''

def __num_substrings_brute_force__(s: str) -> int:
    k = 3
    res = 0
    substr = dict()

    for i in range(min(k, len(s))):
        substr[s[i]] = substr.get(s[i], 0) + 1
    if len(substr) == k:
        res += 1

    for i in range(0, len(s) - k):
        left_elt = s[i]
        right_elt = s[i + k]

        substr[right_elt] = substr.get(right_elt, 0) + 1
        if substr.get(left_elt) > 0:
            substr[left_elt] -= 1
        else:
            substr.pop(left_elt)

        if len(substr) == k:
            res += 1
    return res

def num_substrings_brute_force(s: str) -> int:
    res = 0
    for i in range(len(s)):
        res += __num_substrings_brute_force__(s[i:])
    return res

###############################################################################

def num_substrings_sliding_window(s: str) -> int:
    left = 0
    right = 0
    end = len(s) - 1
    hm = dict()

    count = 0

    while right != len(s):
        hm[s[right]] = hm.get(s[right], 0) + 1

        while hm.get('a', 0) > 0 and hm.get('b', 0) > 0 and hm.get('c', 0) > 0:
            count += 1 + (end - right)
            hm[s[left]] -= 1
            left += 1

        right += 1
    return count

if __name__ == '__main__':
    s = "abcabc"
    res = num_substrings_brute_force(s)
    print(s, res)
    res = num_substrings_sliding_window(s)
    print(s, res)

    s = "aaacb"
    res = num_substrings_brute_force(s)
    print(s, res)
    res = num_substrings_sliding_window(s)
    print(s, res)

    s = "abc"
    res = num_substrings_brute_force(s)
    print(s, res)
    res = num_substrings_sliding_window(s)
    print(s, res)