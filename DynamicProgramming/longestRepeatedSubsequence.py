"""
Example -
Input: AABEBCDJHD
Output: ABD

Algorithm -
This problem is just the modification of Longest Common Sub-sequence problem. The idea is to find the LCS(str, str)
where str is the input string with the restriction that when both the characters are same, they shouldn't be on
the same index in the two strings.
"""

from Array import empty_2d_array


# Time complexity: O(2^n)

def lrs_recursive(p):
    return lrs_recursive_util(p, p, len(p), len(p))

def lrs_recursive_util(p, q, plen, qlen):
    if plen == 0 or qlen == 0:
        return 0

    if p[plen-1] == q[qlen-1] and (plen-1) != (qlen-1):
        return 1 + lrs_recursive_util(p, q, plen-1, qlen-1)
    else:
        return max(lrs_recursive_util(p, q, plen-1, qlen), lrs_recursive_util(p, q, plen, qlen-1))


"""
[
       ""  A  A  B  E  B  C  D  J  H  D
    "" [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    A  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    A  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    B  [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2], 
    E  [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2], 
    B  [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2], 
    C  [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2], 
    D  [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3], 
    J  [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3], 
    H  [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3], 
    D  [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
]
"""
# Time complexity: O(n^2), where n is the length of sub-sequence.
def lrs_dp(p):
    rows = cols = len(p) + 1
    table = empty_2d_array(rows, cols)
    for row in xrange(0, rows):
        for col in xrange(0, cols):
            if row == 0 or col == 0:        # If either of 2 sequence is empty, lcs is 0.
                table[row][col] = 0
                continue

            if p[row-1] == p[col-1] and row != col:
                table[row][col] = table[row-1][col-1] + 1
            else:
                table[row][col] = max(table[row-1][col], table[row][col-1])
    #print table
    return table[rows-1][cols-1]

if __name__ == '__main__':
    p = "AABEBCDJHD"

    print "\n------- Using recursive approach -------\n"
    lrs_len = lrs_recursive(p)
    print "Length of LRS for sequence '{}' is {}".format(p, lrs_len)

    print "\n------- Using DP approach -------\n"
    lrs_len = lrs_dp(p)
    print "Length of LRS for sequence '{}' is {}".format(p, lrs_len)