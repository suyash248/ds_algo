"""
LCS Problem Statement: Given two sequences, find the length of longest sub-sequence present in both of them.
A sub-sequence is a sequence that appears in the same relative order, but not necessarily contiguous.
e.g. "abc", "abg", "bdf", "aeg", "acefg", .. etc are sub-sequences of "abcdefg".
So a string of length n has 2^n different possible sub-sequences.

LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.
"""

from Array import empty_2d_array


# Time complexity: O(2^n)
def lcs_recursive(p, q, plen, qlen):
    if plen == 0 or qlen == 0:
        return 0

    if p[plen-1] == q[qlen-1]:
        return 1 + lcs_recursive(p, q, plen-1, qlen-1)
    else:
        return max(lcs_recursive(p, q, plen-1, qlen), lcs_recursive(p, q, plen, qlen-1))


"""
         "" a  b  c  d  e  f  g  h
            
    ""   0  0  0  0  0  0  0  0  0
    k    0  0  0  0  0  0  0  0  0
    l    0  0  0  0  0  0  0  0  0
    b    0  0  1  1  1  1  1  1  1
    m    0  0  1  1  1  1  1  1  1
    e    0  0  1  1  1  2  2  2  2
    f    0  0  1  1  1  2  3  3  3
    z    0  0  1  1  1  2  3  3  3
    h    0  0  1  1  1  2  3  3  4
"""
# Time complexity: O(mn), where m, n are lengths of sub-sequences
def lcs_dp(p, q):
    rows = len(p)+1; cols = len(q)+1
    table = empty_2d_array(rows, cols)
    for row in xrange(0, rows):
        for col in xrange(0, cols):
            if row == 0 or col == 0:        # If either of 2 sequence is empty, lcs is 0.
                table[row][col] = 0
                continue

            if p[row-1] == q[col-1]:
                table[row][col] = table[row-1][col-1] + 1
            else:
                table[row][col] = max(table[row-1][col], table[row][col-1])
    #print table
    lcs_seq = get_lcs_seq(p, q, table)
    return table[rows-1][cols-1], lcs_seq

def get_lcs_seq(p, q, table):
    """
    Algorithm -
    Traverse the 2D array(table) starting from table[rows][cols](bottom right). Do following for every
    cell table[row][col] ->
        a) If characters (in P and Q) corresponding to table[row][col] are same (Or P[row-1] == Q[col-1]),
            then include this character as part of LCS.
        b) Else compare values of table[row-1][col] and table[row][col-1] and go in direction of greater value.
    """
    lcs_seq = []
    plen = len(p); qlen = len(q)

    while plen > 0 and qlen > 0:
        if p[plen-1] == q[qlen-1]:
            lcs_seq.append(p[plen-1])
            plen -= 1
            qlen -= 1
        elif table[plen-1][qlen] > table[plen][qlen-1]:
            plen -= 1
        elif table[plen-1][qlen] <= table[plen][qlen-1]:
            qlen -= 1
    return lcs_seq[::-1]

if __name__ == '__main__':
    p = "abcdefgh"
    q = "klbmefzh"

    print "\n------- Using recursive approach -------\n"
    lcs_len = lcs_recursive(p, q, len(p), len(q))
    print "Length of LCS for sequences '{}' & '{}' is {}".format(p, q, lcs_len)

    print "\n------- Using DP approach -------\n"
    lcs_len_and_seq = lcs_dp(p, q)
    print "Length of LCS for sequences '{}' & '{}' is {} and the seq is - {}".format(p, q, lcs_len_and_seq[0], lcs_len_and_seq[1])