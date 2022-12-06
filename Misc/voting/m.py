"""
abcde'
'Abcd'
"""

from collections import defaultdict

def getDiffChar(s1: str, s2: str):
    larger, smaller = s1, s2
    if len(s1) < len(s2):
        larger = s2
        smaller = s1

    hm = defaultdict(int)

    for ch in larger:
        hm[ch] += 1

    for ch in smaller:
        if ch in larger:
            hm[ch] -= 1

            if hm[ch] == 0:
                hm.pop(ch)
        else:
            return ch

    if len(hm) == 0:
        return None

    return list(hm.keys())[0]



